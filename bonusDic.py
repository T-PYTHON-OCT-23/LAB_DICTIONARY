def weatherDictionary():
    weather = {}

    for i in range(2):
        cityName = input("Enter the name of city: ")

        weather[cityName] = {}
        date = input("Enter date: ")
        temperature = input("Enter temperature: ")
        humidity = input("humidity: ")
        condition = input("condition: ")
   
    
        weather[cityName]["date"] = date
        weather[cityName]["temperature"] = humidity
        weather[cityName]["humidity"] = humidity
        weather[cityName]["condition"] = condition
    return weather  
#weather1 = weatherDictionary()
#print(weather1)

def weatherQuery():

    cityName = input("Enter the name of the city you want to query about: ")
    cityName = weather1.get(cityName)
    print(cityName)
    
def update():
    cityName = input("Enter the city name to update: ")
    if cityName in weather1: 
        newCity = input("Enter the new name of city: ")
        
        weather1[newCity] = {}
        date = input("Enter date: ")
        temperature = input("Enter temperature: ")
        humidity = input("humidity: ")
        condition = input("condition: ")
   
    
        weather1[cityName]["date"] = date
        weather1[cityName]["temperature"] = humidity
        weather1[cityName]["humidity"] = humidity
        weather1[cityName]["condition"] = condition
        print(weather1) 
def delete():
    cityName = input("Enter city name to delete: ")
    del weather1[cityName]
    print(weather1)
    
    
    
weather1 = weatherDictionary()
print(weather1)
   
weatherQuery()

update = int(input("Please Enter 1 to update or 2 to delete or 0 to exit: "))
if update == 1:
    update()
elif update == 2:
    delete()
else:
    print("thank you!")


    




