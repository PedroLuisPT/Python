def sumCicles()
"""
Write a code which reads a int number "n" and writes the sum of the int numbers between 0 e n. Using the cicle "for".
Requires: a int number >0
Ensures: the sum of all the int numbers between 0 and the given nunber
"""
n=int(input("Write a number"))
acum=0
for i in range(n):
    acum+=i
    print(acum)
return acum    
