myDictionary= {
    "dammam": {
        "date":"07-07-1996",
        "temperature":"34",
        "humidity":"21",
        "condition":"sunny"
        },
    
    "khobar": {
        "date":"08-08-2012",
        "temperature":"45",
        "humidity":"73",
        "condition":"windy"
        }
    }

def queryData(city_:dict):
    if city_ in myDictionary:
        print(f"City : {city_}, Date: {myDictionary[city_]["date"]}, temperature: {myDictionary[city_]["temperature"]}, humidity: {myDictionary[city_]["humidity"]}, condition: {myDictionary[city_]["condition"]}")
    else:
        print(f"Weather data for {city_} not found.\n")

queryData("dammam")

def deleteData(city_:dict)->dict:
    if city_ in myDictionary:
        del myDictionary[city_]
deleteData("khobar")
print(myDictionary)
