objDict = {}
objStr = input()
while objStr != "":
    objList = objStr.split()
    for i in objList:
        objDict[i] = objDict.get(i, 0) + 1
    objStr = input()
for i in objDict:
    print(i, objDict[i])
###
objDict = {}
objStr = input()
while objStr != "":
    objList = objStr.split()
    for i in objList:
        if i in objDict:
            objDict[i] += 1
        else:
            objDict[i] = 1
    objStr = input()
for i in objDict:
    print(i, objDict[i])
###
objDict = {}
objStr = input()
while objStr != "":
    objList = objStr.split()
    for i in range(len(objList)):
        if objList[i] in objDict:
            objDict[objList[i]] += 1
        else:
            objDict[objList[i]] = 1
    objStr = input()
for i in objDict:
    print(i, objDict[i])