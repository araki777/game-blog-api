from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import expression

from app.models.base import Base, ModelBaseMixin
from app.models.reviews import Review


class User(ModelBaseMixin, Base):
    __tablename__ = "users"

    full_name: Mapped[str] = mapped_column(String(64), index=True)
    email: Mapped[str] = mapped_column(
        String(200),
        unique=True,
        index=True,
        nullable=False,
    )
    email_verified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default=expression.false(),
    )
    hashed_password: Mapped[str] = mapped_column(Text, nullable=False)
    scopes: Mapped[str] = mapped_column(Text, nullable=True)

    reviews: Mapped[list[Review]] = relationship("Review", secondary="users_reviews", back_populates="users", lazy="joined")