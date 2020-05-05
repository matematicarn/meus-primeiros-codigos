# Em um grupo de n pessoas, calcule a probabilidade de haver pelo menos duas pessoas que façam aniversário no mesmo dia.
import math
n = int(input("Há quantas pessoas no grupo? "))
prob = (1 - math.perm(365,n)/365**n)
print(f"\n Num grupo de {n} pessoas, a probabilidade de haver pelo menos duas pessoas que tenham o mesmo dia de aniversário é de %.2f." % round(prob,2))
