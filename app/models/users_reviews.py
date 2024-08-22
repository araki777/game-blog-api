from sqlalchemy import ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, ModelBaseMixinWithoutDeletedAt


class UserReview(ModelBaseMixinWithoutDeletedAt, Base):
  __tablename__ = "users_reviews"
  __table_args__ = (UniqueConstraint("user_id", "review_id", name="ix_users_reviews_user_id_review_id"),)

  id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
  user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
  review_id: Mapped[str] = mapped_column(ForeignKey("reviews.id"), index=True)