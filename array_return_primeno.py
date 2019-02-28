#return the no of primeno in an array
import math
def IsPrime(n):
    flag=True
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
                flag=False
                break
                
    return flag

# def array_contain_prime(arr):        
#         flag=False        
#         for x in arr:
#                 if(IsPrime(x)):
#                         flag=True
#                         print(x)
#         return flag
n=[3,4,5,6,7,8,9,10,11]
print(IsPrime(n))


