
user_number = input("Enter your number: ")
if user_number in phone_book:
    print(f"the owner for this number is {user_number} is {phone_book[user_number]} ")
else:
    print(f"Sorry, the number is not found {user_number}")  
#for n in phone_book:
if len(user_number) < 10 or len(user_number) > 10:
   print("This is invalid number")
if  not user_number.isdigit() :
    print("This is invalid number")
def receives_numbers (numbers:list)->int:
    for index,n in enumerate(numbers):
        if n==0 in numbers:
            numbers.pop(index)
            numbers.append(0)
      
       
    return numbers
print (receives_numbers(numbers=[5, 0, 34, 9, 0, 13, 8]))            

        
    
    

    