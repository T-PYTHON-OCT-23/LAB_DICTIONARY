#Q1

def getName(phoneNum):
    phoneBook = {
        "0568323222": "Amal", "0522222232": "Mohammed",
        "0532335983":"Khadijah","0545341144":"Abdullah",
        "0545534556":"Rawan","0560664566":"Faisal","0567917077":"Layla"
    }## dictionary
    
    if not phoneNum.isdigit() or len(phoneNum) != 10:
        return "This is an invalid Number !"
    
    owner = phoneBook.get(phoneNum)
    
    if owner is not None:
        return owner
    else:
        return "Sorry, the number is not found"

phoneNum = input("Please enter the phone number: ")

result = getName(phoneNum)
print(result)

#Q2

def zeros():
    list = [5, 0, 34, 9, 0, 13, 8]

    result1 = [n for n in list if n != 0]
    result1.extend([0] * list.count(0))
    return result1
print(zeros())