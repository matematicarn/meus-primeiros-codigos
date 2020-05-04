# Teoria dos Números: calcule o número de primos positivos menores ou iguais a um dado real positivo.
from mpmath import *
import math

x = float(input('Digite um número real positivo: '))
y = math.floor(x) #retorna o maior inteiro menor ou igual a x 
def p(y):
  return primepi(y) #retorna o # de primos positivos menores ou iguais a y
print(f'Existem {p(y)} primos positivos menores ou iguais a {x}.')