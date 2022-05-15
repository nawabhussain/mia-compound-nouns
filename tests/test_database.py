from services.database_service import DatabaseService


def test_data_load():
    data = DatabaseService().get_data()
    assert data.shape[0] > 0


def test_column_text_exists():
    data = DatabaseService().get_data()
    assert 'text' in data.columns


def test_column_icd_exists():
    data = DatabaseService().get_data()
    assert 'icd_code' in data.columns
