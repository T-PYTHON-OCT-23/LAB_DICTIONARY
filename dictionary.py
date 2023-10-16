print("dictionary start")
number_book = {
    "0568323222" : "Amal",
    "0522222232" : "Mohammed",
    "0532335983" : "Khadijah",
    "0545341144" : "Abdullah",
    "0545534556" : "Rawan",
    "0560664566" : "Faisal",
    "0567917077" : "Layla"
}

user_input = input("Enter number you want to search for: ")
if not isinstance(user_input, str):
    print("This is invalid number")

if len(user_input) == 10:
    if user_input in number_book:
        print(number_book.get(user_input))
    else:
        print("Sorry, the number is not found")
else:
    print("This is invalid number")


print("ditionary end")
print("-"*50)
print("list satrt")
list_new = [5,0,34,9,0,13,8]

def list_number(list:list) -> list:
    new_list = []
    for n in list:
        if n == 0:
            new_list.append(n)
        else:
            new_list.insert(0,n)      
    return new_list

final_list = list_number(list_new)
print(final_list)
print("list end")
print("-"*50)

