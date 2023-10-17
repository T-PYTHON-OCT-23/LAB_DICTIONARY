# Q1
phone_book = {
     "0568323222" :"Amal" ,
     "0522222232":"Mohammed",
     "0532335983" : "Khadijah" ,
     "0545341144":"Abdullah "  , 
      "0545534556" :"Rawan " ,
      "0560664566" : "Faisal",
      "0567917077": "Layla "
 }

user_input = input("Please enter the number: ")
''' 
# another soluation
if len(user_input)==10 and user_input.isdigit() and user_input in phone_book:
      owner= print(f"the {user_input} is {phone_book[user_input]}")
else:
    print("Sorry, the number is not found")

    الفرق بين 
    isdigit :
تدعم الارقام فقط سواء الصحيحة ام الكسور
    isnumeric :
    شاملة اكثر
'''    
if user_input in phone_book:
    owner= print(phone_book[user_input])
elif len(user_input) < 10 or len(user_input) > 10 or user_input.isnumeric():
             print("This is invalid number")
else:
    print("Sorry, the number is not found")
print()
print(" ---------Q2-------------")
print()

#Q2

def arrange (list_num:list):  
    zerros_list = []

    for i in list_num:
        if i==0 :
            zerros_list.append(i)
        else:
            zerros_list.insert(0,i)

    return zerros_list


list= [5, 0, 34, 9, 0, 13, 8]
result =arrange(list)
print (result)




