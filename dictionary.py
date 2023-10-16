phone_book ={
    " 0568323222" : "Amal",
       "0522222232" : " Mohammed"	,
       " 0532335983" :"Khadijah",
       "0545341144":"Abdullah" ,
       "0545534556" : "Rawan" ,
    	"0560664566":"  Faisal",
        "0567917077": "Layla"
       


}
user_input = input("Enter phone number: ")
if user_input in phone_book:
  print(f"the owner {user_input} is {phone_book[user_input]} ")
elif len(user_input)< 10 and len(user_input)>10:
     
       print ("This is invalid number" )
      
elif user_input.isnumeric()!=True:
            print("this is invalid number")
else:
    print(f"Sorry we don't have the info for {user_input}")





def resorte_list (list)-> list:
      list.sort() 
      for num in list:
       if num in list:
            if num == 0 :
             list.remove(num)
            list.append(num)
      return 

mylist=[5, 0, 34, 9, 0, 13, 8, ]

mylist=[x for x in mylist if x !=0]
zeros=[0,0]
mylist.extend(zeros)
#print(f"list beforn resort: {mylist}") محاولة للحل لم تضبط
#resortlist=resorte_list(mylist)
print(f"list affter resort: {mylist}")


#deleted_item = list.pop(1)ايضا هنا حاولت احل باستخدام pop
#deleted_item = list.pop(4)

#print(list)
#resorte_list (list)


'''alya programmer'''
    