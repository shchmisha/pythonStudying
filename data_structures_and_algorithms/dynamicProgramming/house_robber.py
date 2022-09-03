
def houseRobberTD(houses, currentIndex, tempDict):
    if currentIndex >= len(houses):
        return 0
    else:
        if currentIndex not in tempDict:
            stealFirstHouse = houses[currentIndex] + houses[currentIndex+2]
            skipFirstHouse = houses[currentIndex+1]
            tempDict[currentIndex] = max(stealFirstHouse, skipFirstHouse)
        return tempDict[currentIndex]


houses = [6, 7,1,30,8,2,4]
print(houseRobberTD(houses, 0, {}))

def houseRobberBU(houses, currentIndex):
    tempArr = [0] * (len(houses)+2)
    for i in range(len(houses)-1, -1, -1):
        tempArr[i] = max(houses[i]+tempArr[i+2], tempArr[i+1])
    return tempArr[0]
