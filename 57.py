def genOTP(size,qty):
    import random as rd
    list1=[]
    for i in range (0,qty,1):
        rd2=rd.randint(10**(size-1),(10**size)-1)
        list1.append(rd2)
    return(list1)
print(genOTP(2,20))
print(genOTP(4,10))
print(genOTP(6,3))
print(genOTP(8,2))
