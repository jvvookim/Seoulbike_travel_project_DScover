from typing import List
from fastapi import FastAPI
import uvicorn

from database import SESSION, ENGINE
from route import getRoute
from model.model import TravelTable, Travel, Input, Rest, RestTable, CafeTable, Cafe
from rest import getSomeRests, getSomeCafes
from starlette.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# @app.post("/travelInput")
# def create_user(travel : Travel):
#     return travel

@app.post("/getRoute")
def getTheRoute(input : Input):
    minVal, bestRoute = getRoute(input)
    return {"minVal":minVal, "bestRoute":bestRoute}

@app.post("/getRest")
def getRest(input: Input):
    resultList = getSomeRests(input.latitude, input.longitude)
    return {"resultList":resultList}

@app.post("/getCafe")
def getCafe(input: Input):
    resultList = getSomeCafes(input.latitude, input.longitude)
    return {"resultList":resultList}

@app.post("/travelInput")
def create_users(travel : Travel):
    travelObj = TravelTable()
    travelObj.latitude = travel.latitude
    travelObj.longitude = travel.longitude
    travelObj.nearest = str(travel.nearest)
    travelObj.rank = travel.rank
    travelObj.category = travel.category
    travelObj.time = travel.time
    travelObj.name = travel.name
    travelObj.id = travel.id
    SESSION.add(travelObj)
    SESSION.commit()
    return travel

@app.post("/restInput")
def create_rest(rest: Rest):
    restObj = RestTable()
    restObj.latitude = rest.latitude
    restObj.longitude = rest.longitude
    restObj.nearest =rest.nearest
    restObj.category = rest.category
    restObj.rank = rest.rank
    restObj.name = rest.name
    restObj.id = rest.id
    SESSION.add(restObj)
    SESSION.commit()
    return rest

@app.post("/cafeInput")
def create_rest(cafe: Cafe):
    restObj = CafeTable()
    restObj.latitude = cafe.latitude
    restObj.longitude = cafe.longitude
    restObj.nearest = cafe.nearest
    restObj.category = cafe.category
    restObj.rank = cafe.rank
    restObj.name = cafe.name
    restObj.id = cafe.id
    SESSION.add(restObj)
    SESSION.commit()
    return cafe

@app.get("/")
def root():
    return {"Hello":"World"}

@app.get("/travel")
def read_travel():
    travels = SESSION.query(TravelTable).all()
    return travels

@app.get("/travel/{travel_id}")
def read_one(travel_id:int):
    travel = SESSION.query(TravelTable).filter(TravelTable.id == travel_id).first()
    return travel

@app.put("/travelUpdate")
def update_users(travels: List[Travel]):
    for i in travels:
        travel = SESSION.query(TravelTable).filter(TravelTable.id == i.id).first()
        travel.latitude = i.latitude
        travel.longitude = i.longitude
        travel.nearest = i.nearest
        travel.rank = i.rank
        travel.category = i.category
        travel.time = i.time
        travel.name = i.name
        travel.uniq_id = i.uniq_id
    SESSION.commit()
    return "updated"

@app.delete("/travelDelete")
def delete_user(travel_id: int):
    travel = SESSION.query(TravelTable).filter(TravelTable.id == travel_id).delete()
    SESSION.commit()
    return read_travel()

@app.get("/insertIntoDB")
def insertData():
    # df1 = pd.read_csv("travel.csv", encoding="utf-8")
    # df1.to_sql(name="travel", con=ENGINE, index=False, if_exists="append", method="multi")
    # df2 = pd.read_csv("rest.csv", encoding="utf-8")
    # df2.to_sql(name="rest", con=ENGINE, index=False, if_exists="append", method="multi")
    # df3 = pd.read_csv("cafe.csv", encoding="utf-8")
    # df3.to_sql(name="cafe", con=ENGINE, index=False, if_exists="append", method="multi")
    return ""
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)