from itertools import permutations
from sys import maxsize

n = int(input())
distanceList = list()
for _ in range(n):
    dList = list(map(int, input().split()))
    distanceList.append(dList)

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

min_path, best_path = TSP(distanceList, 0)
print(min_path)