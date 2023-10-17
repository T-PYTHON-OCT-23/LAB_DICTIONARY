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

if user_input in phone_book:
    owner= print(phone_book[user_input])
elif len(user_input) < 10 or len(user_input) > 10 or user_input.isnumeric():
             print("This is invalid number")
else:
    print("Sorry, the number is not found")
print()

#Q2
new_list = ()
def arrange (list_num:list):  
    for i in list_num:
        if i==0  in list_num:
            list_num.insert(-1,i)
            return list_num


list= [5, 0, 34, 9, 0, 13, 8]
result =arrange(list)
print (result)




