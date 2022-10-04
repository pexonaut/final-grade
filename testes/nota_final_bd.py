import heapq
import sqlite3

#Menu
print('''-Selecione a ação desejada-
Calcular notas [1]
Editar/Excluir notas [2]
Ver notas e médias [3]''')
inserir_menu = int(input(": "))
calcular_notas = 1
editar_notas = 2
ver_notas = 3

if inserir_menu == calcular_notas:
    while True:
        print('''
-Escolha a materia calculada-
Matematica [1]
Geografia [2]
Historia [3]
Português [4]
Quimica [5]
Fisica [6]''')
        
        materia_escolhida = int(input(": "))
        
        if ((materia_escolhida > 0) and (materia_escolhida <= 6)):
            
            g1 = int(input("Nota da g1: "))
            g2 = int(input("Nota da g2: "))
            g3 = int(input("Nota da g3: "))
            pe = int(input("Pontos extras e diversificadas: "))
            
            lista1 = [g1, g2, g3]
            nt1 = max(lista1)
            nt2 = (heapq.nlargest(2, lista1)[-1])
            mdp = round((nt1 + nt2)/2) + pe
            
            
            escolha = str(input('''Deseja adicionar outro trimestre? 
[S/N]: '''))
        
            if escolha == "S":
                while True:
                    print('-------2° trimestre--------')
                    globo1 = int(input("Nota da g1: "))
                    globo2 = int(input("Nota da g2: "))
                    globo3 = int(input("Nota da g3: "))
                    pxe = int(input("Pontos extras e diversificadas: "))
                    
                    lista2 = [globo1, globo2, globo3]
                    nota1 = max(lista2)
                    nota2 = (heapq.nlargest(2, lista2)[-1])
                    media = round((nota1 + nota2)/2) + pxe

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
                 print('A média final do aluno(a) foi de [{}] pontos no trimestre!'.format(mdp))


