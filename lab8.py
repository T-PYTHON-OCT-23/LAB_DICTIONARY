#Q1)

phone_book = {
   "0568323222"  : "Amal" , 
   "0522222232 " : "Mohammed" ,
   "0532335983 " : "Khadijah" ,
   "0545341144" : "Abdullah" ,
   "0545534556" : "Rawan" ,
   "0560664566" : "Faisal" ,  
   "0567917077" : "Layla" 
}
user_input:int= input("Enter phone number : ")


if user_input in phone_book :
    print(f"The owner of number {user_input} is {phone_book[user_input]}")
    
elif len(user_input) < 10 or  len(user_input) > 10  :
         print("This is invalid number")        

elif user_input.isnumeric() == False :
        print("This is invalid number")  
else :
    print("Sorry, the number is not found") 



#Q2)
#my_list = [5, 0, 34, 9, 0, 13, 8]
def rearranges_the_list(my_list):
    zeros=[]
    non_zeros=[]

    for num in my_list:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)
    return non_zeros + zeros
new_list = [5, 0, 34, 9, 0, 13, 8]
result = rearranges_the_list(new_list)
print("New iist : ",result)            