### Calculadora de pontos 1° trimestre

g1 = int(input("Nota da g1: "))
g2 = int(input("Nota da g2: "))
g3 = int(input("Nota da g3: "))
pe = int(input("Pontos extras e diversificadas: "))

#Pegar as duas notas maiores-
    
#Maior nota:
nt1 = g1
if g2 > nt1:
  nt1 = g2
if g3 > nt1:
  nt1 = g3

#Segunda maior nota:
nt2 = g1
if (nt2 > g2) <= nt1:
  nt2 = g2
elif (nt2 > g3) <= nt1:
  nt2 = g3

#Média entre elas/soma de pontos-
mdp = (nt1 + nt2)/2 + pe

#Calcular outro trimestre-
escolha = str(input('''Deseja adicionar outro trimestre? 
[S/N]: '''))

if escolha == "S":
    while True:
        print('-------2° trimestre--------')
        globo1 = int(input("Nota da g1: "))
        globo2 = int(input("Nota da g2: "))
        globo3 = int(input("Nota da g3: "))
        pxe = int(input("Pontos extras e diversificadas: "))
        
        #Maior e segundo maior
        nota1 = globo1
        if globo2 > nota1:
            nota1 = globo2
        if globo3 > nota1:
            nota1 = globo3
            
        nota2 = globo1
        if (nota2 > globo2) <= nota1:
            nota2 = globo2
        elif (nota2 > globo3) <= nota1:
            nota2 = globo3
        
        #Média entre elas/soma de pontos-
        media = ((nota1 + nota2)/2) + pxe
        
        #Calcular quantos pontos faltam para passar de ano
        ptf = 180 - (media + mdp)
        if ptf <= 0:
            print('''Media do 1° trimestre: {}
Media do 2° trimestre: {}
Você já passou de ano, parabéns!'''.format(mdp, media))
        else:
            print('''Media do 1° trimestre: {}
Media do 2° trimestre: {}
Faltam {} pontos para passar de ano!'''.format(mdp, media, ptf))
        
        break;
else:
    print('A média final do aluno(a) foi de [{}] pontos no trimestre'.format(mdp))

        