weather = {
    "Riyadh":{
        "date":"2023/12/1",
        "temperature":"45",
        "humidity":True,
        "weather condition":"sunny"
        },
    "Arar":{
        "date":"2023/12/1",
        "temperature":"23",
        "humidity":False,
        "weather condition":"sunny"
        },
    "Rafha":{
        "date":"2023/12/1",
        "temperature":"22",
        "humidity":True,
        "weather condition":"rainy"
        },
    "Haiel":{
        "date":"2023/12/1",
        "temperature":"15",
        "humidity":True,
        "weather condition":"rainy"
        },
    "Damam":{
        "date":"2023/12/1",
        "temperature":"55",
        "humidity":True,
        "weather condition":"sunny"
        },
    "Abha":{
        "date":"2023/12/1",
        "temperature":"5",
        "humidity":True,
        "weather condition":"rainy"
        }
}

user_input = input("Enter city name to see the weather: ")
if not user_input in weather:
    print(f"{user_input} is not found")
    choisen = int(input("If you want to insert city enter 1, If you don't enter 2: "))
    if choisen == 1:
        city_name = input("If you want to add a new city enter the name: ")
        date = input("If you want to add date to a new city enter the data: ")
        humidity = input("If you want to add humidity a new city enter the humidity: ")
        huweather_conditionmidity = input("If you want to add weather condition to a new city enter the condition. Hint: sunny,rainy: ")
    else:
        print("Thank for your time")


