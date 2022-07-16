from src.notes.config import get_sqlite_path

def test_get_absolute_path_to_sqlite():
    assert get_sqlite_path() == 'sqlite://///Users/yozibak/utils/sea/sea.db' # 4 slashes total