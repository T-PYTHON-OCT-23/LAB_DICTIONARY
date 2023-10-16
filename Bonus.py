#BONUS
weatherData={}
def dataInput(dictitionary_:dict)->dict:
    city = input("please enter the city name: ")
    date = input("please enter the date (DD-MM-YYYY): ")
    temperature = input("please enter the temperature: ")
    humidity = input("please enter the humidity percentage: ")
    condition = input("please enter the condition (e.g., sunny, rainy): ")
    input_={
        "city":city,
        "date":date,
        "temperature":temperature,
        "humidity":humidity,
        "condition":condition
        }
    dictitionary_[city]=(input_)
    return dictitionary_

def queryData(dictitionary_:dict)->dict:
    
    return

def deleteData(dictitionary_:dict)->dict:
    return

def updateData(dictitionary_:dict)->dict:
    return

while True:
    print("if you want to add weather data type '1' :")
   # print("if you want to query data type 2")
   # print("if you want to update data type 3")
   # print("if you want to delete data type 4")
    print("if you want to print and termenate type 5")

    choice=input("please enter your choice : ")
    if choice=="1":
        dataInput(weatherData)
    #elif choice=="2":
        
    #elif choice=="3":
        
    #elif choice=="4":
        
    elif choice=="5":
        print(weatherData)
        break
    else:
        print("Invalid choice. Please enter a valid option.\n")