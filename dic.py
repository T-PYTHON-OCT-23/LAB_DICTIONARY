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
