




def add_to_dict(**dict):
    return dict

#to add
weather={}

answer=''

while answer!='n':
        
    city = input("Enter City name:")
    date = input("Enter the date:")
    temperature = input("Enter temperature in celsius:")
    humidity = input("Enter humidity:")
    weather_condition = input("Enter weather condition:")
    value = add_to_dict(date=date,temperature=temperature,humidity=humidity,weather_condition=weather_condition)
    weather[city]=value
    answer=input("do you need to add new city: y or n: ")
    

#to search on city info
find_data=input("Enter the city name for info: ")

if find_data in weather.keys():
    print(weather[find_data])
else:print("info not found!!")



#to update on city info
update=input("to update on date Enter city name enter space for otherwise:")

if not update.isspace():
    update_date = input("Enter the new date:")
    update_temperature = input("Enter new temperature in celsius:")
    update_humidity = input("Enter new humidity:")
    update_weather_condition = input("Enter new weather condition:")
    update_value = add_to_dict(date=update_date,temperature=update_temperature,humidity=update_humidity,weather_condition=update_weather_condition)

    weather[update]=update_value





print(weather)




