my_d={"0568323222":"maram",
      "0522222232":"taif",
      "0532335983":"mayar",
      "0545341144":"faisal",
      "0545534556":"bader",
      "0560664566":"osama",
      "0567917077":"lamira"
      }

input_user= input("enter number:")
if input_user in my_d:
    print (f"This is invalid number:{input_user} is {my_d[input_user]}")
else:
    print("Sorry, the number is not found")


l:[5, 0, 34, 9, 0, 13, 8]
def lis(l):
    for n in l:
        if n ==0:
          l.sort(l)
       
          return l
print(lis())




