my_d={"0568323222":"maram",
      "0522222232":"taif",
      "0532335983":"mayar",
      "0545341144":"faisal",
      "0545534556":"bader",
      "0560664566":"osama",
      "0567917077":"lamira"
      }

input_user=input("enter number:" )
if input_user in my_d :
    if input_user.isnumeric()!= True:
      print("This is invalid number")

    print (f"This is invalid number:{input_user} is {my_d[input_user]}")
else:
    print("Sorry, the number is not found")


print("--"*40)



def l_r(list1 )-> list:
    list1.sort()
    for n in list1:
        if n in list1:
            if n == 0:
             list1.remove(n)
             list1.append(n)

    return list1


list =  [5, 0, 34, 9, 0, 13, 8, -5]
print(f" befor : {list}")
m = l_r(list)
print(f" after : {m}")


