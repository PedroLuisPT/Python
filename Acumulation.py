#Write a code which reads a int number "n" and writes the sum of the int numbers between 0 e n. Using the cicle "for".
n=int(input("Write a number"))
acum=0
for i in range(n):
    acum+=i
    print(acum)
