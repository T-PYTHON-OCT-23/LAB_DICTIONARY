my_contacts = {"Amal",
               "Mohammed",
               "Khadijah",
               "Abdullah",
               "Rawan",
               "Faisal",
               "Layla"}

for key in my_contacts:
    print(my_contacts)

contacts = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}

phone_input = input("Enter Name: ")
if phone_input in contacts:
    print(f"The number for {phone_input} is {contacts[phone_input]}")
else:
    print(f"Sorry we don't have the info for {phone_input}")
  #2
def rearrange(input_numbers):
    numbers = [x for x in input_numbers if x != 0]
    zero = [x for x in input_numbers if x == 0]
    arranged_list = numbers + zero
    return arranged_list

input_numbers = [5, 0, 34, 9, 0, 13, 8]
result = rearrange(input_numbers)
print(result)

