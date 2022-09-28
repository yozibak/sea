import abc
from typing import List, Set
from domain import model
from sqlalchemy.orm.session import Session


class AbstractRepository(abc.ABC):

    def add(self, note: model.Note):
        self._add(note)

    def get(self, id) -> model.Note:
        note = self._get(id)
        return note
    
    def list(self, search='', pagination=0) -> List[model.Note]:
        return self._list(search, pagination)

    @abc.abstractmethod
    def _add(self, note: model.Note):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, id) -> model.Note:
        raise NotImplementedError
    
    @abc.abstractmethod
    def _list(self, search: str, pagination: int) -> List[model.Note]:
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
            query = query # later

        if pagination:
            query = query.offset(pagination).limit(10)
        
        return query.all()