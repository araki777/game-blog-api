from sqlalchemy import Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, ModelBaseMixin
from app.models.reviews import Review


class Score(ModelBaseMixin, Base):
  __tablename__ = "scores"

  gameplay: Mapped[int] = mapped_column(Integer, nullable=False)
  graphics: Mapped[int] = mapped_column(Integer, nullable=False)
  sound: Mapped[int] = mapped_column(Integer, nullable=False)
  story: Mapped[int] = mapped_column(Integer, nullable=False)
  replayability: Mapped[int] = mapped_column(Integer, nullable=False)

  __table_args__ = (
    CheckConstraint("gameplay BETWEEN 0 AND 10", name="check_gameplay_score"),
    CheckConstraint("graphics BETWEEN 0 AND 10", name="check_graphics_score"),
    CheckConstraint("sound BETWEEN 0 AND 10", name="check_sound_score"),
    CheckConstraint("story BETWEEN 0 AND 10", name="check_story_score"),
    CheckConstraint("replayability BETWEEN 0 AND 10", name="check_replayability_score")
  )

  review_id: Mapped[str] = mapped_column(ForeignKey("reviews.id"), nullable=False, index=True)
  review: Mapped[Review] = relationship("Review", back_populates="score")