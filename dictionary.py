# Create a phone book dictionary with names and numbers
phone_book = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}

def owner_number(num):
    if not num.isdigit():
        return "This is an invalid number (contains letters or symbols)"
    if len(num) != 10:
        return "This is an invalid number (less or more than 10 numbers)."



my_list = [5, 0, 34, 9, 0, 13, 8,]

def rearange (lst:list)->int:
    non_zeros =[n for n in lst if n != 0]
    zeros = [n for n in lst if n == 0]
    return non_zeros + zeros

m =rearange(my_list)
print(m)


