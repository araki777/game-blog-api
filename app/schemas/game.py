import datetime
from enum import Enum
from typing import Optional

from fastapi import Query
from pydantic import ConfigDict

from app import schemas
from app.schemas.core import BaseSchema, PagingMeta


class GameBase(BaseSchema):
    title: str
    description: str
    release_date: Optional[datetime.date] = None
    developer: Optional[str] = None
    publisher: Optional[str] = None


class GameCreate(GameBase):
    pass


class GameUpdate(GameBase):
    pass


class GameResponse(GameBase):
    id: str
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None

    model_config = ConfigDict(from_attributes=True)


class GameDetailsResponse(GameBase):
    game: GameResponse

class GamesPagedResponse(BaseSchema):
    data: Optional[list[GameResponse]] = []
    meta: Optional[PagingMeta]


class GameSortFieldEnum(Enum):
    created_at = "created_at"
    title = "title"
    release_date = "release_date"
    developer = "developer"
    publisher = "publisher"


class GameSortQueryIn(schemas.SortQueryIn):
    sort_field: Optional[GameSortFieldEnum] = Query(GameSortFieldEnum.created_at)