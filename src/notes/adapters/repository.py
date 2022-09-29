import abc
from operator import or_
from typing import List, Set
from sqlalchemy.orm.session import Session
from sqlalchemy import func

from notes.domain import model

class AbstractRepository(abc.ABC):

    def add(self, note: model.Note):
        self._add(note)

    def get(self, id) -> model.Note:
        note = self._get(id)
        return note
    
    def list(self, search='', pagination=0) -> List[model.Note]:
        return self._list(search, pagination)
    
    def count(self, search=''):
        return self._count(search)

    @abc.abstractmethod
    def _add(self, note: model.Note):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, id) -> model.Note:
        raise NotImplementedError
    
    @abc.abstractmethod
    def _list(self, search: str, pagination: int) -> List[model.Note]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def _count(self, search: str) -> int:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def _add(self, note):
        self.session.add(note)

    def _get(self, id):
        return self.session.query(model.Note).filter_by(id=id).first()
    
    def _list(self, search, pagination):
        query = self.session.query(model.Note).order_by(model.Note.updated)

        if search:
            query = query.filter(
                or_(
                    model.Note.title.like(f'%{search}%'),
                    model.Note.content.like(f'%{search}%'),
                )
            )

        query = query.offset(pagination).limit(10)
        
        return query.all()
    
    def _count(self, search):
        query = self.session.query(func.count(model.Note.id))
        if search:
            query = query.filter(
                or_(
                    model.Note.title.like(f'%{search}%'),
                    model.Note.content.like(f'%{search}%'),
                )
            )
        return query.scalar()