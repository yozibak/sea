import abc
from domain import model

class AbstractRepository(abc.ABC):
    def __init__(self):
        pass

    def add(self, note: model.Note):
        self._add(note)

    def get(self, id) -> model.Note:
        note = self._get(id)
        return note

    @abc.abstractmethod
    def _add(self, note: model.Note):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, id) -> model.Note:
        raise NotImplementedError

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, note):
        self.session.add(note)

    def _get(self, id):
        return self.session.query(model.Note).filter_by(id=id).first()