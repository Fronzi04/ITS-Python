''''
Write a Python function called countdown that takes a positive integer n as input and prints a countdown from n to zero. 
If the input number is negative, display an error message.
 To implement the function, you must exclusively use a while loop and the parameter n passed as input to the function.
 Declaring any additional variables inside the function is not allowed.
 Then, call the function with n = -5 and n = 5.
'''
def countdown(n:int):
    x=True
    while x==True:
        
        if n > 0:
            x=False
        else:
            n=int(input("errore, reinserisci: "))
    for i in range(n,-1,-1):
        print(n)
        n=n-1
countdown(n=int(input("inserisci: ")))

