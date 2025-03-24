def power(n,m):
    if m==0:
        return 1
    else:
        n=n*power(n,m-1)
        return n
print(power(3,4))