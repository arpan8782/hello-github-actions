t=int(input("enter number of terms"))
u=0
k=1
print("",u,end="")
print("",k,end="")
for i in range (0,t,1):
    j=u+k
    u=k
    k=j
    print("",j,end="")


