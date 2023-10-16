#BONUS
weatherData={
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
def dataInput(dictitionary_:dict)->dict:
    city = input("please enter the city name: ")
    date = input("please enter the date (DD-MM-YYYY): ")
    temperature = input("please enter the temperature: ")
    humidity = input("please enter the humidity percentage: ")
    condition = input("please enter the condition (e.g., sunny, rainy): ")
    input_={
        "date":date,
        "temperature":temperature,
        "humidity":humidity,
        "condition":condition
        }
    dictitionary_[city]=(input_)
    return dictitionary_

def queryData(city_:dict):
    if city_ in weatherData:
        print(f"City : {city_}, Date: {weatherData[city_]["date"]}, temperature: {weatherData[city_]["temperature"]}, humidity: {weatherData[city_]["humidity"]}, condition: {weatherData[city_]["condition"]}")
    else:
        print(f"Weather data for {city_} not found.\n")

def deleteData(city_:dict)->dict:
    if city_ in weatherData:
        del weatherData[city_]
        print(f"{city_} data is now deleted")
    else:
        print(f"{city_} not found")

def updateData(city_:dict)->dict:
    if city_ in weatherData:
        date = input("Enter updated date: ")
        temperature = input("Enter updated temperature: ")
        humidity = input("Enter updated humidity: ")
        condition = input("Enter updated weather condition: ")
        weatherData[city_]={
            "date" : date,
            "temperature": temperature,
            "humidity": humidity,
            "condition": condition
            }
    else:
        print(f"{city_} not found")

while True:
    print("if you want to add weather data type '1' :")
    print("if you want to query data type '2'")
    print("if you want to update data type '3'")
    print("if you want to delete data type '4'")
    print("if you want to print and EXIT type '5'")

    choice=input("please enter your choice : ")
    if choice=="1":
        dataInput(weatherData)
    elif choice=="2":
        cityName=input("Enter city name: ")
        queryData(cityName)
    elif choice=="3":    
        cityName=input("Enter city name: ")
        updateData(cityName)
    elif choice=="4":
        cityName=input("Enter city name: ")
        deleteData(cityName)
    elif choice=="5":
        print(weatherData)
        break
    else:
        print("Invalid choice. Please enter a valid option.\n")