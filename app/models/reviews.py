from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base, ModelBaseMixin

class Review(ModelBaseMixin, Base):
    __tablename__ = "reviews"
    title: Mapped[str] = mapped_column(String(150), index=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    users = relationship(
        "User",
        secondary="users_reviews",
        back_populates="reviews",
        lazy="joined"
    )

    games = relationship(
        "Game",
        secondary="games_reviews",
        back_populates="reviews",
        lazy="joined"
    )

    score = relationship(
        "Score",
        uselist=False,
        back_populates="review",
        lazy="joined"
    )