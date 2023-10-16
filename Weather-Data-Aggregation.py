print("A program of Weather Data Aggregation.")
#An example: dictionary = {"Jeddah":{"Date":10/16/2023,"Temperature":34,"humidity":14,"weather condition":"Sunny"}}

def check_char(key1:str)-> str:
    if not key1.isalpha():
            print("Invaild , please enter a vaild name.")

def check_number(value2:int)->int:
    if not value2.isnumeric():
        print("Invaild , please enter a vaild number.")

def check_date(value3:int)->int:
    slash = "/"
    if not(value3.isnumeric and slash in value3):
        print("Invaild, for example: 10/16/2023.")

dictionary={}          
key1 = input("City name: ")
check_char(key1)
value2 = input("Date:")
check_date(value2)
value3 = input("Temperature:")
check_number(value3)
value4 = input("Humidity:")
check_number(value4)
value5 = input("Weather condition:")
check_char(value5)

dictionary[key1]={"Date":value2}
dictionary[key1]["Temperature:"]=value3
dictionary[key1]["Humidity:"]=value4
dictionary[key1]["Weather condition:"]=value5
print(dictionary)

print("-"*20)
print("------Query by City------")

def check_input(value):
    if not city_name.isalpha():
        print("Invaild , please enter a vaild name.")


def query_by_city(city_name):
    if city_name in dictionary:
        print(f"The weather data of {city_name} city: {dictionary[city_name]}")

city_name = input("Enter city name:")
check_input(city_name)
query_by_city(city_name)


print("-"*20)
print("---Allow the user to update or delete weather data---")

option = input("Do you want to:\n 1-Update an item \n 2-Delete an item \n choose an option:")
print(option)
 
if option =="1":
    new_key = input("Enter a new data:")
    new_value = input(f"Enter a new value in {new_key} :")

    dictionary[key1].update({new_key:new_value})
    print(f"Now is updated : {dictionary}")
elif option =="2":
    remove_key = input("Enter the name of key to remove: ")
    dictionary[key1].pop(remove_key)
    print(f"Now is Removed : {dictionary}")
else:
    print("Invaild input please choose 1 or 2.")

