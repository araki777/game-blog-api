from datetime import datetime

from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, ModelBaseMixin
from app.models.reviews import Review


class Game(ModelBaseMixin, Base):
    __tablename__ = "games"

    title: Mapped[str] = mapped_column(String(150), index=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    release_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    developer: Mapped[str] = mapped_column(String(100))
    publisher: Mapped[str] = mapped_column(String(100))

    reviews: Mapped[list[Review]] = relationship(
        "Review",
        secondary="games_reviews",
        back_populates="games",
        lazy="joined"
    )