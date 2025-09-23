from fastapi import FastAPI
from constant import MODELS_PATH, DATA_PATH
from data_processing import IrisData, IrisInput, PredictionOutput
import pandas as pd
import joblib

app = FastAPI()
iris = IrisData()


@app.get("/api/")
def read_data():
    return iris.to_json()

@app.post("/api/predict", response_model=PredictionOutput)  ##payload är det man postar in och man tvingar att den ska irisinput, så man måste följa dom valideringarna
def predict_flower(payload: IrisInput):
    data_to_predict = pd.DataFrame([payload.model_dump()]) #payload är en pydantic modell, deseriliza den så att det blir en pandas dataframe
    clf = joblib.load(MODELS_PATH / "iris_classifier.joblib")  #laddar in modellen
    prediction = clf.predict(data_to_predict)  #gör prediktionen
    return {"predicted_flower": prediction[0]}  #returnerar det som en dictionary, måste vara samma som i response_model