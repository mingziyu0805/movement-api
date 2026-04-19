from fastapi import FastAPI, UploadFile
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/analyze")
async def analyze(file: UploadFile):
    df = pd.read_csv(file.file)

    result = {}

    if 'knee_angle' in df.columns:
        rom = df['knee_angle'].max() - df['knee_angle'].min()
        result['knee_ROM'] = float(rom)

    return result
