from typing import Dict

from fastapi import FastAPI, status, HTTPException

from services.database_service import DatabaseService
from services.model_service import ModelService

app = FastAPI()
model_service = ModelService()
ds = DatabaseService(model_service)


@app.post("/predict_icd")
def predict_icd(payload: Dict):
    if payload and 'text' in payload.keys():
        text = payload['text']
        icd_code = ds.fetch_icd(text)
        return {"icd_code": icd_code}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'The parameter text was not found in the request')
