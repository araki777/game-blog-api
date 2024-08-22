import datetime
from enum import Enum
from typing import Optional

from fastapi import Query
from pydantic import ConfigDict

from app.schemas.core import BaseSchema, PagingMeta, SortQueryIn


class ReviewBase(BaseSchema):
    title: str
    description: str


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(ReviewBase):
    pass


class ReviewResponse(ReviewBase):
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    deleted_at: Optional[datetime.datetime] = None

    model_config = ConfigDict(from_attributes=True)

class ReviewDetailsResponse(ReviewBase):
    from app.schemas.user import UserResponse
    from app.schemas.game import GameResponse
    review: Optional[ReviewResponse]
    user: UserResponse
    game: GameResponse


class ReviewsPagedResponse(BaseSchema):
    data: Optional[list[ReviewResponse]] = []
    meta: Optional[PagingMeta]


class ReviewSortFieldEnum(Enum):
    created_at = "created_at"
    title = "title"
    score = "score"


class ReviewSortQueryIn(SortQueryIn):
    sort_field: Optional[ReviewSortFieldEnum] = Query(ReviewSortFieldEnum.created_at)