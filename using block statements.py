#largest of three num
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
if a>b and a>c:
    print("the value a is larger")
elif b>c:
    print("the value b is larger")
else:
    print(" the value c is larger")






#largest using def
def larg(a,b,c):
    if a>b and a>c:
        largest=a
    elif b>c:
         largest=b
    else:
       largest=c
    return largest
a= 10
b= 14
c= 12
print(larg(a,b,c))

