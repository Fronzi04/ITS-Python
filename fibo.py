def fibo(n:int):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return int(fibo(n-1)+fibo(n-2))
print(fibo(10))