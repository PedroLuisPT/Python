The idea is to write a number and a word in order to relate the number 0 to first letter, 1 to second and so on.
i=0
k=int(input("Write a number"))
w=input("write a word")

while i<k:
    print(i,w[:i])
    i=i+1
    
