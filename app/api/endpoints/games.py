from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, schemas
from app.core.database import get_async_db
from app.core.logger import get_logger
from app.exceptions.core import APIException
from app.exceptions.error_messages import ErrorMessage
from app.schemas.core import PagingQueryIn

logger = get_logger(__name__)

router = APIRouter()


@router.get("/{id}", operation_id="get_game_by_id")
async def get_game_by_id(
  id: str,
  include_deleted: bool = False,
  db: AsyncSession = Depends(get_async_db),
) -> schemas.GameResponse:
  game = await crud.game.get_db_obj_by_id(
    db,
    id=id,
    include_deleted=include_deleted
  )
  if not game:
    raise APIException(ErrorMessage.ID_NOT_FOUND)
  return game