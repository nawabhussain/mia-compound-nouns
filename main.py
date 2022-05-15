from typing import Dict

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

from services.database_service import DatabaseService
from services.model_service import ModelService


class Payload(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "Foo",
            }
        }


app = FastAPI()
model_service = ModelService()
ds = DatabaseService(model_service)


@app.post("/predict_icd")
def predict_icd(payload: Payload):
    """
    Retrieves ICD Code for input text by identifying similar entries in the database
    :rtype: Dict
    :param payload: A Dictionary
    :return: A Dictionary with the result ICD Code
    """
    if payload and payload.text:
        icd_code = ds.fetch_icd(payload.text)
        return {"icd_code": icd_code}
