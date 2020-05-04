# Cálculo da Média de notas - IFRN

print("Calcule sua média na Disciplina.")
print('-' * 32)
p1 = float(input('Digite a nota da P1 [0 a 100]: '))
p2 = float(input('Digite a nota da P2 [0 a 100]: '))
media_parcial = (2 * p1 + 3 * p2) / 5
print(f'\n Sua Média Parcial é {round(media_parcial)}. \n')
if 20 <= media_parcial < 59.60:
    print('Você ainda não passou e poderá fazer a Prova Final.')
    pf = float(input('Qual sua nota na PF? '))
    media_parcial1 = (pf + media_parcial) / 2
    media_parcial2 = (2 * p1 + 3 * pf) / 5
    media_parcial3 = (2 * pf + 3 * p2) / 5
    media_final = max(media_parcial1, media_parcial2, media_parcial3)
    print('\n Sua média final é %.f \n' % media_final)
    if media_final < 60:
        print('Infelizmente você foi reprovado :(')
    else:
        print('Parabéns, você foi aprovado!')
else:
    if media_parcial < 20:
        print('Infelizmente você foi reprovado :(')
    else:
        print('Você foi aprovado por média. Parabéns!')
