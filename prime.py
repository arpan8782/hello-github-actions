i=int(input("enter number"))
j=2
for j in range(2,i,1):
    if i%j==0:
        print("not prime")
        break

else:
    print("prime")


