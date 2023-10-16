#Q1
phone_book = {
    '0568323222':'Amal',
    '0522222232':'Mohammed',
    '0532335983':'Khadijah',
    '0545341144':'Abdullah',
    '0545534556':'Rawan',
    '0560664566':'Faisal',
    '0567917077':'Layla'
}

phone_number=input('provide the number:')

if phone_number.isnumeric():
    if phone_number in phone_book:
        print(f"The owner is {phone_book.get(phone_number)}")
    else:print("Sorry, the number is not found")
else:print("This is invalid number")


print("--"*20)
#Q2
def update_list(list_:list)->list:
    new_list=[]
    final_list=[]
    
 
    for i in range(0,len(list_)):
        if list_[i] == 0:
            new_list.append(list_[i])
        if list_[i] !=0:
            final_list.append(list_[i])
  
        
    final_list.extend(new_list)
    return final_list




print(update_list([5, 0, 34, 9, 0, 13, 8]))
