import heapq
# Calculadora de pontos 1° trimestre    

g1 = int(input("Nota da g1: "))
g2 = int(input("Nota da g2: "))
g3 = int(input("Nota da g3: "))
pe = int(input("Pontos extras e diversificadas: "))

# Pegar as duas notas maiores-

# Maior nota:
lista1 = [g1, g2, g3]
nt1 = max(lista1)

# Segunda maior nota:
nt2 = (heapq.nlargest(2, lista1)[-1])

# Média entre elas/soma de pontos-
mdp = round((nt1 + nt2)/2) + pe

# Calcular outro trimestre-
escolha = str(input('''Deseja adicionar outro trimestre? 
[S/N]: '''))

if escolha == "S":
    while True:
        print('-------2° trimestre--------')
        globo1 = int(input("Nota da g1: "))
        globo2 = int(input("Nota da g2: "))
        globo3 = int(input("Nota da g3: "))
        pxe = int(input("Pontos extras e diversificadas: "))

        # Maior nota:
        lista2 = [globo1, globo2, globo3]
        nota1 = max(lista2)

        # Segunda maior nota:
        nota2 = (heapq.nlargest(2, lista2)[-1])

        # Média entre elas/soma de pontos-
        media = round((nota1 + nota2)/2) + pxe

        # Calcular quantos pontos faltam para passar de ano
        ptf = 180 - (media + mdp)
        if ptf <= 0:
            print('''Media do 1° trimestre: {}
Media do 2° trimestre: {}
Você já passou de ano, parabéns!'''.format(mdp, media))
        else:
            print('''Media do 1° trimestre: {}
Media do 2° trimestre: {}
Faltam {} pontos para passar de ano!'''.format(mdp, media, ptf))

        break
else:
    print(
        'A média final do aluno(a) foi de [{}] pontos no trimestre'.format(mdp))
