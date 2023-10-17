
weather_data = {}

while True:
  
    print("1. Input Weather Data")
    print("2. Query by City")
    print("3. Update Weather Data")
    print("4. Delete Weather Data")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == "1":
        city = input("Enter the city name: ")
        date = input("Enter the date (YYYY-MM-DD): ")
        temperature = float(input("Enter temperature (in Celsius): "))
        humidity = float(input("Enter humidity (%): "))
        condition = input("Enter weather condition: ")

        if city in weather_data:
            if date in weather_data[city]:
                print("Weather data for this date already exists.")
            else:
                weather_data[city][date] = {
                    "temperature": temperature,
                    "humidity": humidity,
                    "condition": condition
                }
       

    elif choice == "2":
        city = input("Enter city name to query: ")
        if city in weather_data:
            print(f"Weather data for {city}:")
            for date, details in weather_data[city].items():
                print(f"Date: {date}, Temperature: {details['temperature']}°C, Humidity: {details['humidity']}%, Condition: {details['condition']}")
        else:
            print(f"No weather data found for {city}")

    elif choice == "3":
        city = input("Enter the city name to update weather data: ")
        date = input("Enter the date to update (YYYY-MM-DD): ")
        if city in weather_data and date in weather_data[city]:
            print(f"Current data for {city} on {date}: {weather_data[city][date]}")
            temperature = float(input("Enter new temperature (in Celsius): " ))
            humidity = float(input("Enter new humidity (%): "))
            condition = input("Enter new weather condition: ")
            
            weather_data[city][date] = {
                "temperature": temperature,
                "humidity": humidity,
                "condition": condition
            }
        else:
            print(f"No data found for {city} on {date}")

    elif choice == "4":
        city = input("Enter the city name to delete weather data: ")
        date = input("Enter the date to delete (YYYY-MM-DD): ")
        if city in weather_data and date in weather_data[city]:
            del weather_data[city][date]
            if not weather_data[city]:
                del weather_data[city]
            print(f"Weather data for {city} on {date} deleted")
        else:
            print(f"No data found for {city} on {date}")

    elif choice == "5":
        break
    else:
        print("Invalid choice. Please select a valid option.")