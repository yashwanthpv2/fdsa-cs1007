def rec(n) : 
    if n==0:
         return 0
    else:
          r=n%10  
    return(r + rec(n//10))  
n = int(input("enter a number")) 
print(rec(n))