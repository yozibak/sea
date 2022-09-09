import abc
from typing import List, Set
from domain import model
from sqlalchemy.orm.session import Session


class AbstractRepository(abc.ABC):
    def __init__(self):
        self.seen = set() # type: Set[model.Note]

    def add(self, note: model.Note):
        self._add(note)
        self.seen.add(note)

    def get(self, id) -> model.Note:
        note = self._get(id)
        if note:
            self.seen.add(note)
        return note
    
    def list(self, *args) -> List[model.Note]:
        return self._list(*args)

    @abc.abstractmethod
    def _add(self, note: model.Note):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, id) -> model.Note:
        raise NotImplementedError
    
    @abc.abstractmethod
    def _list(self, **kwargs) -> List[model.Note]:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def _add(self, note):
        self.session.add(note)

    def _get(self, id):
        return self.session.query(model.Note).filter_by(id=id).first()
    
    def _list(self, **kwargs):
        return self.session.query(model.Note).order_by(model.Note.updated).all()