import abc
from operator import or_
from typing import List, Set
from sqlalchemy.orm.session import Session
from sqlalchemy import func
from sqlalchemy.orm import Query
from notes.domain import model


class AbstractRepository(abc.ABC):

    def add(self, note: model.Note):
        self._add(note)

    def get(self, idx: int, search='') -> model.Note:
        note = self._get(search, idx)
        return note
    
    def list(self, search='', pagination=0) -> List[model.Note]:
        return self._list(search, pagination)
    
    def count(self, search=''):
        return self._count(search)
    
    def delete(self, note: model.Note):
        self._delete(note)

    @abc.abstractmethod
    def _add(self, note: model.Note):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, search, idx) -> model.Note:
        raise NotImplementedError
    
    @abc.abstractmethod
    def _list(self, search: str, pagination: int) -> List[model.Note]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def _count(self, search: str) -> int:
        raise NotImplementedError
    
    @abc.abstractmethod
    def _delete(self, note: model.Note):
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def _add(self, note):
        self.session.add(note)

    def _get(self, search, idx):
        query = self.session.query(model.Note).order_by(model.Note.updated.desc())
        if search:
            query = search_query(query, search)
        return query.offset(idx).limit(1).first()
    
    def _list(self, search, pagination):
        query = self.session.query(model.Note).order_by(model.Note.updated.desc())
        if search:
            query = search_query(query, search)
        return query.offset(pagination).limit(10).all()
    
    def _count(self, search):
        query = self.session.query(func.count(model.Note.id))
        if search:
            query = search_query(query, search)
        return query.scalar()
    
    def _delete(self, note):
        self.session.delete(note)


def search_query(query: Query, word: str):
    res = query.filter(
        or_(
            model.Note.title.like(f'%{word}%'),
            model.Note.content.like(f'%{word}%'),
        )
    )
    return res

