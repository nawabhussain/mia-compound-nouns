from typing import Dict

from fastapi import FastAPI, status, HTTPException

app = FastAPI()


@app.post("/predict_icd")
def predict_icd(payload: Dict):
    if payload and 'text' in payload.keys():
        text = payload['text']
        return {"msg": text}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'The parameter text was not found in the request')
