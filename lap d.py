


'''Q1'''

number_book = {
    "0568323222" : "abdoullah",
    "0522222232" : "ahmed",
    "0532335983" : "turki" ,
    "0545341144" : "amal" ,
    "0557407242" : "naif"
    }


user_input = input("Enter num: ")
if  user_input in number_book:
    print(f"this name {number_book[user_input]}")
elif len(user_input) !=10:
    print("This is invalid number")
elif user_input.isnumeric() != True:
    print("This is invalid number")
else:
    print("Sorry, the number is not found")
    

'''Q2'''

Number =  [5, 0, 34, 9, 0, 13, 8, -5]

def my_list(lst1 )-> list:
    lst1.sort()
    lst1_without_zeros = []
    for n in lst1:
        if n != 0:
            lst1_without_zeros.append(n)
    lst1_without_zeros.append(0)
    lst1 = lst1_without_zeros
    return lst1

new_lis = my_list(Number)
print(new_lis)