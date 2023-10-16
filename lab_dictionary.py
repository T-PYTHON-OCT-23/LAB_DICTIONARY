


phone_book = {
 "0568323222": "Amal" ,
 "0522222232" : "Mohammed" ,
 "0532335983" : "Khadijah" ,
 "0545341144" :"Abdullah" ,
 "0545534556" :"Rawan" ,
 "0560664566" : "Faisal" ,
 "0567917077" : "Layla" ,
}

entry_item = input("enter the number: ")

if not entry_item in phone_book:
    print("Sorry, the number is not found")
if len(entry_item) < 10 or len(entry_item) >10:
    print("This is invalid number")
if entry_item.isnumeric() == False :
    print("This is invalid number")



list=[5,0,34,9,0,13,8]
zeros = []


def rearange (list):
  list=[5,0,34,9,0,13,8]
  list.sort(reverse=True)
  print(list)



rearange(list)

