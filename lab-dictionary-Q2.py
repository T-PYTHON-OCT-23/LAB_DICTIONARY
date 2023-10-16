#Q2
my_list=[5, 0, 34, 9, 0, 13, 8]
def Reverse(my_list):
   new_list = my_list[::-1]
   return new_list

print("Unorder list:",my_list)
my_list.sort()
print("Ordered list:",my_list)
print("Reversed:",Reverse(my_list))