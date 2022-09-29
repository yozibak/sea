from datetime import date


class Note:
    def __init__(
        self, title: str, content: str,
        id: int = None,
        created: date = date.today(), 
        updated: date = date.today()
    ):
        self.id = id
        self.title = title
        self.content = content
        self.created = created
        self.updated = updated
    
    def __str__(self) -> str:
        return f'{date_format(self.updated)} - {self.title}'


def date_format(date: date):
    return date.strftime("%y/%m/%d")