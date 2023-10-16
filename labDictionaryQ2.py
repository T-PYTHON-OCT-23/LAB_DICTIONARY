#Q2
testList=[5, 0, 34, 9, 0, 13, 8]

#old solution
def oldRearranger(_list:list)->list:

    newList=[]
    count=0
    for i in _list:
        if i!=0:
            newList.append(i)
        elif i==0:
            count+=1
    else:
        while count!=0:
            newList.append(0)
            count-=1
    return newList
print(oldRearranger(testList))

#new solution
def rearranger(_list:list)->list:
    newList=[]
    for index, i in enumerate(_list):
        if i==0:
            newList.append(_list.pop(index)) 
    for index, i in enumerate(newList):
        _list.append(newList[index]) 
    return _list

print(rearranger(testList))

