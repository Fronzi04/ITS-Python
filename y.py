def summ(n:int):
    s=0
    if n<0:
        print("error")
    else:
        while n:
            s+=n
            n-=1
        print(s)
summ(-5)         

def rsum(n:int):
    if n<0:
        return "errore"
    elif n ==0:
        return 0
    else:
        return n+rsum(n-1)
print(rsum(-5))
    
    
