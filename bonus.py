inputdata_=""
dict_ = {}
while inputdata_ != "exit":
    inputdata_ = input("Enter name of a city: exit to quit: ")
    inputdate_ = input("Enter date: ")
    inputtemp_ = input("Enter temp: ")
    inputhumidity_ = input("Enter humidity: ")
    inputweather_ = input("Enter weather: ")
    temp_={inputdata_, inputdate_, inputtemp_, inputhumidity_, inputweather_}
    dict_.update({inputdata_:temp_})
        
query_ = input("Enter city name to query: ")
if query_ in dict_:
    print(dict_[query_])
    

update_ = input("Enter city name to update: ")

if update_ in dict_:
    data = input("Enter date: ")
    temp = input("Enter temp: ")
    hum = input("Enter humidity: ")
    weather = input("Enter weather: ")
    dict_.update({update_:[data, temp, hum, weather]})
    
print(dict_)


del_ = input("Enter city name to delete: ")

del dict_[del_]



