from services.database_service import DatabaseService
from services.model_service import ModelService

model_service = ModelService()


def test_data_load():
    data = DatabaseService(model_service).get_data()
    assert data.shape[0] > 0


def test_columns_exist():
    data = DatabaseService(model_service).get_data()
    assert 'text' in data.columns
    assert 'icd_code' in data.columns
    assert 'embeddings' in data.columns

