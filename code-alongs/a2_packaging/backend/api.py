from data_processing import cool_data
from fastapi import FastAPI


app = FastAPI()

import pprint


@app.get("/cool_data")
async def get_cool_data():
    return cool_data
print(cool_data)