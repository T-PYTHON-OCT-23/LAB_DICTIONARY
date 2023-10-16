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
    list_ = sorted(list_, reverse=True) 
    # Check if there are any zeros in the list
    if 0 in list_:
        # While the last element is not 0, move it to the end
        while list_[-1] != 0:
            list_.insert(0,list_.pop(-1))
    
    return list_
    
test = [5, 0, 34, 9, 0, 13, 8,-1]

print(zerolist_(test))

