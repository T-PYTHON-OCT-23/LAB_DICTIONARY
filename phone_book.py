#Q1
phone_book={
"0568323222":"Amal",
"0522222232":"Mohammed",
"0532335983":"Khadijah",
"0545341144":"Abdullah",
"0545534556":"Rawan",
"0560664566":"Faisal",
"0567917077":"Layla"
}

def is_numeric(value:int)->int:
    if len(number)<=10 :
        print("This is invalid number")
    elif number.isnumeric() != True:
        print("This is invalid number!")
    else:
        print("error")

number = (input("Please enter the number:"))
is_numeric(number)
if number in phone_book:
        print(f"name:",phone_book[number])

