
fact=int(input("enter the number"))
def factorial(fact):
    if fact==1 or fact==0:
        return 1
    else:
        return(fact*(factorial(fact-1)))#recursion
        
        
k=factorial(fact)
print("factorial of ",fact,"is:",k)       
