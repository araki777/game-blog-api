from sqlalchemy import or_
from sqlalchemy.orm import Session, contains_eager

from app import crud, models, schemas

from .base import CRUDBase


class CRUDGame(
  CRUDBase[
    models.Game,
    schemas.GameResponse,
    schemas.GameCreate,
    schemas.GameUpdate,
    schemas.GamesPagedResponse,
    schemas.GameSortQueryIn
  ],
):
  def get_paged_list(
      self,
      db: Session,
      paging_query_in: schemas.PagingQueryIn,
      q: str | None = None,
      sort_query_in: schemas.SortQueryIn | None = None,
  ) -> schemas.GamesPagedResponse:
    where_clause = (
      [
        or_(
          models.Game.title.ilike(f"%{q}%"),
          models.Game.description.ilike(f"%{q}%")
        ),
      ]
      if q
      else []
    )
    return super().get_paged_list(
      db,
      paging_query_in=paging_query_in,
      where_clause=where_clause,
      sort_query_in=sort_query_in
    )