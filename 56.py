import random as rd
list1=[]
size=4
for i in range (0,10,1):
    rd2=rd.randint(10**(size-1),(10**size)-1)
    list1.append(rd2)
print(list1)
