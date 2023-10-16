#Q1
phoneBook = {
      "0568323222" : "Amal", 
      "0522222232" : "mohammed",
      "0532335983" : "Khadijah",
      "0545341144" : "abdullah" ,
      "0545534556" : "Rawan",
      "0560664566" : "Faisal",
      "0567917077" : "Layla"   
      }
    
phoneNumber = input("please enter phonenumber:")
if phoneNumber in phoneBook:
    print(F"the owner of this number {phoneNumber} is : {phoneBook[phoneNumber]}")
elif len(phoneNumber) > 10 or len(phoneNumber) < 10:
    print("This is invalid number")
elif phoneNumber.isnumeric() != True:
    print("This is invalid number")
else:
    print("Sorry, the number is not found")

print("-"*20)

#Q2
def rearrangesList(list1 )-> list:
    list1.sort()
    for n in list1:
        if n in list1:
            if n == 0:
             list1.remove(n)
             list1.append(n)
    
    return list1
    
       
listNumber =  [5, 0, 34, 9, 0, 13, 8, -5]
print(f"List befor arrange: {listNumber}")
arrangeList = rearrangesList(listNumber)
print(f"List after arrange: {arrangeList}")


    