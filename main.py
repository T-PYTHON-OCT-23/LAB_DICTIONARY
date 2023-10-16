dictnumber = {
 "Amal":"0568323222",
 "Mohammed":"0522222232",
 "Khadijah":"0532335983",
 "Abdullah":"0545341144" ,
 "Rawan":"0545534556" ,
 "Faisal":"0560664566" ,
 "Layla":"0567917077" 
}

input_number = input("Enter number: ")

if not input_number.isdigit():
    print("This is invalid number")

if len(input_number) != 10:
    print("This is invalid number")

if not input_number in dictnumber.values():
    print("Sorry, the number is not found")
    
else:
    value = {i for i in dictnumber if dictnumber[i]==input_number}
    print(value)    
        
    
def zerolist_(list_):
    list_=sorted(list_)
    list_=list_[::-1]
    return list_
    
test = [5, 0, 34, 9, 0, 13, 8]

print(zerolist_(test))

