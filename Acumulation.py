#Escreva um programa que leia um inteiro n e escreva a soma dos números
#inteiros entre 0 e n. Utilize um ciclo for para o efeito.
n=int(input("Write a number"))
acum=0
for i in range(n):
    acum+=i
    print(acum)
