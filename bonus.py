inputdata_=""
dict_ = {}
while inputdata_ != "exit":
    inputdata_ = input("Enter name of a city: exit to quit: ")
    inputdate_ = input("Enter date: ")
    inputtemp_ = input("Enter temp: ")
    inputhumidity_ = input("Enter humidity: ")
    inputweather_ = input("Enter weather: ")
    temp_={"City":inputdata_,
           "Date":inputdate_, 
           "Temp":inputtemp_,
           "Humidity":inputhumidity_, 
           "Weather":inputweather_}
    dict_.update({inputdata_:temp_})
        
query_ = input("Enter city name to query: ")
if query_ in dict_:
    print(dict_[query_])
    

update_ = input("Enter city name to update: ")

if update_ in dict_:
    date = input("Enter date: ")
    temp = input("Enter temp: ")
    hum = input("Enter humidity: ")
    weather = input("Enter weather: ")
    temp_={"City":update_,
        "Date":date, 
        "Temp":temp,
        "Humidity":hum, 
        "Weather":weather}
    dict_.update({update_:temp})
    print(dict_)


del_ = input("Enter city name to delete: ")

del dict_[del_]



