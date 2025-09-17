import fastapi
from data_processing import cool_data
import pprint

app = fastapi.FastAPI()

#@app.get("/cool_data")
#async def get_cool_data():
 #   return cool_data
print(cool_data)