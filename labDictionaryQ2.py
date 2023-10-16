#Q2
testList=[5, 0, 34, 9, 0, 13, 8]
def rearranger(_list:list)->list:
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

print(rearranger(testList))