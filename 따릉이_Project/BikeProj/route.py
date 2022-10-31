import math
import json
from operator import index
from unicodedata import name
from model.model import Travel, TravelTable, Input
from database import SESSION
from sys import maxsize
from itertools import permutations

#위도경도 계산식 준비1
def getX(wd1, gd1, gd2):
    return (math.cos(wd1)*6400*2*3.14/360) * abs(gd1 - gd2)

#위도경도 계산식 준비2
def getY(wd1, wd2):
    return 111*abs(wd1-wd2)

#위도경도 계산식
def getDistance(wd1, wd2, gd1, gd2):
    X = getX(wd1, gd1, gd2)
    Y = getY(wd1, wd2)
    return math.sqrt(X*X + Y*Y)

#TSP알고리즘
def TSP(distanceList, start): 
    vertex = list() 
    for i in range(len(distanceList)): 
        if i != start: 
            vertex.append(i) 
    min_path = maxsize 
    next_permutation = permutations(vertex)
    best_path = []
    
    for i in next_permutation:
        current_pathweight = 0
        k = start 
        for j in i: 
            current_pathweight += distanceList[k][j] 
            k = j 
        current_pathweight += distanceList[k][start] 
        if current_pathweight < min_path:
            min_path = current_pathweight
            best_path = [start]
            best_path.extend(list(i))
            best_path.append(start)
    return min_path, best_path


def getRoute(jsonInfo):
    travelIdList = jsonInfo.id #json 첫번째에 id들 리스트를 넣어서 보내주기
    currentLat = jsonInfo.latitude
    currentLong = jsonInfo.longitude
    travelObj = TravelTable()
    travelObj.latitude = currentLat
    travelObj.longitude = currentLong
    travelList = list() #Travel 객체들을 담을 List
    travelList.append(travelObj)   
    #받은 id 기준으로 Travel 객체를 DB에서 가져온 후 travelList에 Append해주기
    for i in travelIdList:
        aTravel = SESSION.query(TravelTable).filter(TravelTable.id == i).first()
        travelList.append(aTravel)
    nameList = list()
    for travelName in travelList:
        nameList.append(travelName.name)
    distanceList = list() #Travel 간 거리를 기록할 list
    for a in travelList:
        tempList = []
        for b in travelList:
            tempList.append(getDistance(a.latitude, b.latitude, a.longitude, b.longitude))
        distanceList.append(tempList)
    #TSP~
    minVal, routeList = TSP(distanceList, 0)
    resultList = list()
    for indexNum in routeList:
        if indexNum == 0:
            resultList.append("현재위치")
        else:
            resultList.append(nameList[indexNum])
    return minVal, resultList