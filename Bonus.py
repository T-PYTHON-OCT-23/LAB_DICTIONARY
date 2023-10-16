weather={}

for i in range(2):
    city_name = input("Enter city name: ")

    weather[city_name]={}
    temperature = input("Enter temperature: ")
    humidity=input("Enter humidity: ")
    date=input("Enter date: ")
    weather_condition= input("Enter weather condition: ")


    weather[city_name]["city_name"]=city_name
    weather[city_name]["temperature"]=temperature
    weather[city_name]["humidity"]=humidity
    weather[city_name]["date"]=date
    weather[city_name]["weather_condition"]=weather_condition

print(weather)

city_name=input("Do you want to Query by City about all weather info of the city: ")
city_name=weather.get(city_name)
print(city_name)

#Challenge
city_name=input("Do you want update or delete weather data for a specific city and date: ")
del weather[city_name]
print(weather)






