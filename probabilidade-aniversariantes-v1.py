# Em um grupo de n pessoas, calcule a probabilidade de haver pelo menos duas pessoas que façam aniversário no mesmo dia.
import math
n = int(input("Há quantas pessoas no grupo? "))
lista = []
r = 1
while r <= n:
    lista.append(366-r)
    r += 1
else:
    prob = (1 - math.prod(lista)/(365**n))*100
print(f'\n Num grupo de {n} pessoas, a probabilidade de haver pelo menos duas pessoas que tenham o mesmo dia de aniversário é de {round(prob)}%.')