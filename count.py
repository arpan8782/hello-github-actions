j=int(input("enter a no."))
i=1
while i<=j:
    if i%3==0 or i%5==0:
        print("",end="")
    else:
        print("",i,end="")
    i=i+1