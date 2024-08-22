from sqlalchemy import ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, ModelBaseMixinWithoutDeletedAt


class GameReview(ModelBaseMixinWithoutDeletedAt, Base):
  __tablename__ = "games_reviews"
  __table_args__ = (UniqueConstraint("game_id", "review_id", name="ix_games_reviews_game_id_review_id"),)

  id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
  game_id: Mapped[str] = mapped_column(ForeignKey("games.id"), index=True)
  review_id: Mapped[str] = mapped_column(ForeignKey("reviews.id"), index=True)