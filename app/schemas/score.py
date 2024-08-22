import datetime
from enum import Enum
from typing import Optional

from fastapi import Query
from pydantic import ConfigDict

from app import schemas
from app.schemas.core import BaseSchema, PagingMeta


class ScoreBase(BaseSchema):
    gameplay: int
    graphics: int
    sound: int
    story: int
    replayability: int


class ScoreCreate(ScoreBase):
    pass


class ScoreUpdate(ScoreBase):
    pass


class ScoreResponse(ScoreBase):
    id: str
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    deleted_at: Optional[datetime.datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ScoresPagedResponse(BaseSchema):
    data: Optional[list[ScoreResponse]]
    meta: Optional[PagingMeta]


class ScoreSortFieldEnum(Enum):
    created_at = "created_at"
    gameplay = "gameplay"
    graphics = "graphics"
    sound = "sound"
    story = "story"
    replayability = "replayability"


class ScoreSortQueryIn(schemas.SortQueryIn):
    sort_field: Optional[ScoreSortFieldEnum] = Query(ScoreSortFieldEnum.created_at)