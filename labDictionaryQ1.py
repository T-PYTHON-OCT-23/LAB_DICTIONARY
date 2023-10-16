#Q1
phoneBook={
    "0568323222":"Amal",
    "0522222232":"Mohammed",
    "0532335983":"Khadijah",
    "0545341144":"Abdullah",
    "0545534556":"Rawan",
    "0560664566":"Faisal",
    "0567917077":"Layla"
    }

def checkPhoneBook(n:str)->str:
    if len(n)!=10 or not n.isnumeric():
        print("This is invalid number")
    else:
        for key in phoneBook:
            if n==key:
                print(f"This number belong to {phoneBook[key]}")
        else:
            print("Sorry, the number is not found")

number=input("Enter a ten digit phone number: ")
checkPhoneBook(number)            