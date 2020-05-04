# Teoria dos Números: calcule a soma dos quadrados dos dígitos de um dado inteiro positivo

x = input('Digite um inteiro positivo: ')
def q(x):
  return sum(int(n)**2 for n in str(x))
print(f'A soma dos quadrados de seus dígitos é igual a {q(x)}.')