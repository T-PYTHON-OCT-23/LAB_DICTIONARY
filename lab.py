phone_book={
"0568323222" :"Amal" ,
"0522222232":"Mohammed", 
"0532335983":"Khadijah", 
"0545341144":"Abdullah" , 
"0545534556":"Rawan", 
"0560664566":"Faisal", 
"0567917077 ":"Layla"}

print('Welcome in the phone book program')
number=input("Please provide the number: ")
if number in phone_book:
    print('The owner of the number',phone_book[number])
elif (len(number) < 10 or len(number) >10):
    print("This is invalid number")
elif number.isalnum()==True :
    print("This is invalid number")
else :
    print("Sorry, the number is not found")

numbers=[5, 0, 34, 9, 0, 13, 8]
def list_rearranges(numbers):
    numbers.sort(reverse=True)
    print(numbers)
list_rearranges(numbers)
    
