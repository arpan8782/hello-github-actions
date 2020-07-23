def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
i=int(input("enter no."))
result=fact(i)
print(result)