n=0
weather= {}
while n >= 0:
    if n >= 2:
        
        break
    else:
        print(" ")
        city = input("enter the city name: ")
        print(" ")
        today_date = input("Enter today date: ")
        print(" ")
        temperature = input("Enter the temperature of that city: ")
        print(" ")
        humidity = input("How match humidity rate in that city: ")
        print(" ")
        weather_condition = input("what is the weather condition in that city (e.g., sunny, rainy): ")
    n +=1
    weather[city] = {today_date,temperature,humidity,weather_condition}
new_weather= weather 
print(" ")  
user_city = input("Enter a city for quary the weather data: ")
if user_city in weather:
    print(" ")
    print(f"The quary of the weather datat for this city {user_city} is {weather[user_city]}")
else:
    print(" ")
    print("Sorry that city not found.")
if user_city in weather:
    print(" ")
    delet_city = input("if you want delet a city enter the name of the city if not press enter: ")
    print(" ")
    update_date=input("if you want update the date enter your update if not press enter: ")
    print(" ")
    update_temperature = input("if you want update the temperature enter your update if not press enter: ")
    print(" ")
    update_humidity=input("if you want update the humidity enter your update if not press enter: ")
    print(" ")
    update_weather_condition = input("if you want update the weather condition enter your update if not press enter: ")
    print(" ")
key_1= input("ente char: (a) to make the update or press enter: ") 
if  key_1 == "a":
    new_weather.update({city : {update_date,update_temperature,update_humidity,update_weather_condition}})
    print(" ")
key_2 = input("enter word: (delete) to make the delete or press enter: ")
if key_2 == "delete":  
   del new_weather[delet_city]
print(" ")
print(f"The finaly weather data: {new_weather} ")  