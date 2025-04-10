from collections.abc import AsyncGenerator, Generator

from debug_toolbar.panels.sqlalchemy import SQLAlchemyPanel as BasePanel
from fastapi import Request
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import text

from app.core.config import settings
from app.core.logger import get_logger

logger = get_logger(__name__)


try:
    engine = create_engine(
        settings.get_database_url(),
        pool_pre_ping=True,
        echo=False,
        future=True,
    )
    session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as e:
    logger.error(f"DB connection error. detail={e}")


try:
    async_engine = create_async_engine(
        settings.get_database_url(is_async=True),
        pool_pre_ping=True,
        echo=False,
        future=True,
    )
    async_session_factory = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=async_engine,
        class_=AsyncSession,
    )
except Exception as e:
    logger.error(f"DB connection error. detail={e}")


def get_db() -> Generator[Session, None, None]:
    """endpointからアクセス時に、Dependで呼び出しdbセッションを生成する
    エラーがなければ、commitする
    エラー時はrollbackし、いずれの場合も最終的にcloseする.
    """
    db = None
    try:
        db = session_factory()
        yield db
        db.commit()
    except Exception:
        if db:
            db.rollback()
    finally:
        if db:
            db.close()


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """async用のdb-sessionの作成."""
    async with async_session_factory() as db:
        try:
            yield db
            await db.commit()
        except Exception:
            await db.rollback()
        finally:
            await db.close()


def drop_all_tables() -> None:
    logger.info("start: drop_all_tables")
    """
    全てのテーブルおよび型、Roleなどを削除して、初期状態に戻す(開発環境専用)
    """
    if settings.ENV != "local":
        # ローカル環境でしか動作させない
        logger.info("drop_all_table() is ENV local only.")
        return

    metadata = MetaData()
    metadata.reflect(bind=engine)

    with engine.connect() as conn:
        # 全テーブルを削除
        for table in reversed(metadata.sorted_tables):
            conn.execute(text(f"DROP TABLE IF EXISTS {table.name} CASCADE"))
        logger.info("end: drop_all_tables")


if settings.DEBUG:

    class SQLAlchemyPanel(BasePanel):
        async def add_engines(self, request: Request) -> None:
            self.engines.add(async_engine.sync_engine)