from fastapi import FastAPI, APIRouter
from data_processing import DataExplorer

app = FastAPI()
router = APIRouter(prefix="/api/sales")   #slipper man skriva @app /api/sales kan man bara använda detta som en förkortning

@router.get("")  
async def read_sales():
    data_explorer = DataExplorer()
    return data_explorer.json_response()


@router.get("/summary")
async def read_summary_data():
    data_explorer = DataExplorer()
    return data_explorer.summary().json_response()

@router.get("/kpis")
async def read_kpis(country: str):
    data_explorer = DataExplorer()
    return data_explorer.kpis(country=country)
