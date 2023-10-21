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
    "0568323222" : "Amal",
    "0522222232" : "Mohammed",
    "0532335983" : "Khadijah",
    "0545341144" : "Abdullah",
    "0545534556" : "Rawan",
    "0560664566" : "Faisal",
    "0567917077" : "Layla"
}

phone_input = input("Enter phonr number: ")
if phone_input in contacts:
    print(f"The phone number {phone_input} is for {contacts[phone_input]}")
else:
    print(f"Sorry we don't have the info for {phone_input}")
