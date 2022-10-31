from unittest import result
from model.model import RestTable, Rest, TravelTable, CafeTable
from database import SESSION
from route import getDistance

def allRestList():
    rests = SESSION.query(RestTable).order_by(RestTable.rank).all()
    restList = [rest for rest in rests]
    return restList

def getSomeRests(lat, long):
    restList = allRestList()
    resultList = list()
    tempResultList = list()
    for rest in restList:
        x = getDistance(lat, rest.latitude, long, rest.longitude)
        if x < 5: #임시 (실제값은 아마 3km 정도로)
            tempResultList.append(rest)
    for Rest in tempResultList:
        tempList= list()
        tempList.append(Rest.id)
        tempList.append(Rest.latitude)
        tempList.append(Rest.longitude)
        tempList.append(Rest.category)
        tempList.append(Rest.name)
        tempList.append(Rest.nearest)
        tempList.append(Rest.rank)
        resultList.append(tempList)
    return resultList

def allCafeList():
    rests = SESSION.query(CafeTable).order_by(CafeTable.rank).all()
    restList = [rest for rest in rests]
    return restList

def getSomeCafes(lat, long):
    cafeList = allCafeList()
    resultList = list()
    tempResultList = list()
    for rest in cafeList:
        x = getDistance(lat, rest.latitude, long, rest.longitude)
        if x < 5: #임시 (실제값은 아마 3km 정도로)
            tempResultList.append(rest)
    for Rest in tempResultList:
        tempList= list()
        tempList.append(Rest.id)
        tempList.append(Rest.latitude)
        tempList.append(Rest.longitude)
        tempList.append(Rest.category)
        tempList.append(Rest.name)
        tempList.append(Rest.nearest)
        tempList.append(Rest.rank)
        resultList.append(tempList)
    return resultList