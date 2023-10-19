number_book = {
    "0568323222" : "Amal" ,
    "0522222232" : "Mohammed" ,
    "0532335983" : "Khadijah" ,
    "0545341144" : "Abdullah" ,
    "0545534556" : "Rawan" ,
    "0560664566" : "Faisal" ,
    "0567917077" : "Layla"
}

search = input("Enter the number:  ")

if len(search)<10 and not search.isnumeric() :
    print("This is invalid number")
    
    if not search in number_book:
        print("Sorry, the number is not found")

print("_"*20)

def receives_list (my_list:list) -> list :
    new_list = sorted(my_list, reverse=True) 
    return new_list


                
numbers=[5, 0, 34, 9, 0, 13, 8]        

print(receives_list(numbers))

              
            

    