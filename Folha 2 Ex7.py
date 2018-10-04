##Finding the smallest number as they are input in the code.

a=int(input("Write the first number"))
print("The smallest number is",a)
b=int(input("Write another number"))
if a<b:
    print("The smallest number is",a)
else:
    print("The smallest number is",b)
c=int(input("Write another number"))
if a<b and a<c:
    print("The smallest number is",a)
elif b<c and b<a:
    print("The smallest number is",b)
else:
    print("The smallest number is",c)
d=int(input("Write another number"))
if d<a and d<b and d<c:
    print("The smallest number is",d)
elif a<b and a<d and a<c:
    print("The smallest number is",a)
elif b<c and b<a and b<d:
    print("The smallest number is",b)
elif c<a and c<b and c<d:
    print("The smallest number is",c)
