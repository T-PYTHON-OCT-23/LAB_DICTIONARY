phone={
    "0568323222":"Amal",
    "0522222232":"Mohammed",
    "0532335983":"Khadijah",
    "0545341144":"Abdullah",
    "0545534556":"Rawan",
    "0560664566":"Faisal",
    "0567917077":"Layla"
    }

user_number=input("enter number:")
if user_number in phone:
    print(f"The phone number{user_number} belonge to : {phone[user_number]}")
elif len(user_number)< 10 and len(user_number)>10:
    print( "This is invalid number")
elif user_number.isnumeric()!=True :
     print("This is invalid number")
else:
    print("Sorry, the number is not found")


def fuctioList(items):
    for n in items:
        if n==0:
            items.remove(n)
            items.append(n)
    return items
    
print("This list: ")
print(fuctioList([5, 0, 34, 9, 0, 13, 8]))
    