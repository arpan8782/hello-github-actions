x=int(input("enter first no."))
y=int(input("enter second no."))
def add(x,y):
    c=x+y
    d=x*y
    return c,d
z,t=add(x,y)
p=z+10
q=t+10
print(p,q)