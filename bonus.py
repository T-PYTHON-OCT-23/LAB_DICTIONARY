inputdata_=""
dict_ = {}
while inputdata_ != "exit":
    inputdata_ = input("Enter name of a city: exit to quit: ")
    inputdate_ = input("Enter date: ")
    inputtemp_ = input("Enter temp: ")
    inputhumidity_ = input("Enter humidity: ")
    inputweather_ = input("Enter weather: ")
    dict_[inputdata_] = [inputdate_, inputtemp_, inputhumidity_, inputweather_]
    
    
query_ = input("Enter city name to query: ")
if query_ in dict_:
    print(dict_[query_])
    

update_ = input("Enter city name to update: ")

if update_ in dict_:
    dict_[update_][0] = input("Enter date: ")
    dict_[update_][1] = input("Enter temp: ")
    dict_[update_][2] = input("Enter humidity: ")
    dict_[update_][3] = input("Enter weather: ")
    
print(dict_)


del_ = input("Enter city name to delete: ")

del dict_[del_]



