One_list = []
Odd_list = []
Even_list = []
R_list = []


n = int(input("Enter Number of elements:"))
print("Enter Elements:")
for x in range(0,n):
    One_list.append(int(input()))
for i in One_list:
    if i not in R_list:
     R_list.append(i)
for num in R_list:
    if num % 2 == 0 :
        if num >=0:
            Even_list.append(num)
    elif num >=0:
     Odd_list.append(num)
    

    
     

print("List:",R_list)
print("Odd_list",Odd_list)
print("Even_list",Even_list)
