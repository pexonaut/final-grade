from genericpath import exists
import heapq
import sqlite3
import time
from typing import final
import biblioteca_funções

# Database
conexao = sqlite3.connect('banco_de_dados_anchieta.db')
cursor = conexao.cursor()

# Menu
print('''\033[34mCalcular notas [1]
Editar/Excluir notas [2]
Ver notas e médias [3]\033[m''')
inserir_menu = int(input("Selecione a ação desejada: "))
calcular_notas = 1
editar_notas = 2
ver_notas = 3

if inserir_menu == calcular_notas:
    while True:
        print("-" * 28)  # Pra deixar bonitinho
        print('''\033[33mMatematica [1]
Geografia [2]
Historia [3]
Português [4]
Quimica [5]
Fisica [6]\033[m''')

        materia_mat = 1
        materia_geo = 2
        materia_hist = 3
        materia_port = 4
        materia_qui = 5
        materia_fis = 6

        materia_escolhida = int(input("Escolha a materia calculada (Precisa ser um numero): "))

        if ((materia_escolhida > 0) and (materia_escolhida <= 6)):

            g1 = int(input("Nota da g1: "))
            g2 = int(input("Nota da g2: "))
            g3 = int(input("Nota da g3: "))
            pe = int(input("Pontos extras e diversificadas: "))

            lista1 = [g1, g2, g3]
            nt1 = max(lista1)
            nt2 = (heapq.nlargest(2, lista1)[-1])
            mdp = round((nt1 + nt2)/2) + pe

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

            print("-" * 28)  # Pra deixar bonitinho

            if ptf <= 0:
                ptf = "passou"
                print('''\033[32mMedia do 1° trimestre: {}\nMedia do 2° trimestre: {}\nVocê já passou de ano, parabéns!'''.format(mdp, media))
            else:
                print('''\033[31mMedia do 1° trimestre: {}\nMedia do 2° trimestre: {}\nFaltam {} pontos para passar de ano!'''.format(mdp, media, ptf))
                ptf = "Não passou"
        else:
            print("Opção Invalida")

        # Inserir no banco de dados
        while ((materia_escolhida > 0) and (materia_escolhida <= 6)):

            if materia_escolhida == materia_mat:
                cursor.execute(
                    f"INSERT INTO Matematica VALUES ('{nt1}', '{nt2}', '{mdp}', '{nota1}', '{nota2}', '{media}', '{ptf}')")
                conexao.commit()
            elif materia_escolhida == materia_geo:
                cursor.execute(
                    f"INSERT INTO Geografia VALUES ('{nt1}', '{nt2}', '{mdp}', '{nota1}', '{nota2}', '{media}', '{ptf}')")
                conexao.commit()
            elif materia_escolhida == materia_hist:
                cursor.execute(
                    f"INSERT INTO Historia VALUES ('{nt1}', '{nt2}', '{mdp}', '{nota1}', '{nota2}', '{media}', '{ptf}')")
                conexao.commit()
            elif materia_escolhida == materia_port:
                cursor.execute(
                    f"INSERT INTO Português VALUES ('{nt1}', '{nt2}', '{mdp}', '{nota1}', '{nota2}', '{media}', '{ptf}')")
                conexao.commit()
            elif materia_escolhida == materia_qui:
                cursor.execute(
                    f"INSERT INTO Quimica VALUES ('{nt1}', '{nt2}', '{mdp}', '{nota1}', '{nota2}', '{media}', '{ptf}')")
                conexao.commit()
            else:
                cursor.execute(
                    f"INSERT INTO Fisica VALUES ('{nt1}', '{nt2}', '{mdp}', '{nota1}', '{nota2}', '{media}', '{ptf}')")
                conexao.commit()    

            print(
                '\033[35m!!!!Aguarde o programa encerrar se você preza pelo seus dados!!!!\033[m')
            break
        break

# Visualizar Notas
elif inserir_menu == ver_notas:
    while True:
        print('''\033[33mMatematica [1]
Geografia [2]
Historia [3]
Português [4]
Quimica [5]
Fisica [6]''')
        
        materia_mat = 1
        materia_geo = 2
        materia_hist = 3
        materia_port = 4
        materia_qui = 5
        materia_fis = 6
        materia_escolhida = int(input("Escolha a materia que vai ser visualizada (Precisa ser um numero): "))

        if ((materia_escolhida > 0) and (materia_escolhida <= 6)):
            while True:

                print("-" * 28)  # Pra deixar bonitinho

                print("\033[35mCarregando 'banco_de_dados_anchieta'\033[m")
                time.sleep(2)
                

                print("Modelo para visualização de dados:\n('nota1, nota 2, media 1° trimestre', 'nota1, 2 e media do 2° trimestre e situação final')")
                print(" ")
                if materia_escolhida == materia_mat:
                  for row in cursor.execute("SELECT * FROM Matematica"):
                         print("-" * 28)
                         print(row)
                
                elif materia_escolhida == materia_geo:
                    for row in cursor.execute("SELECT * FROM Geografia"):
                        print("-" * 28)
                        print(row)

                elif materia_escolhida == materia_hist:
                    for row in cursor.execute("SELECT * FROM Historia"):
                        print("-" * 28)
                        print(row)

                elif materia_escolhida == materia_port:
                    for row in cursor.execute("SELECT * FROM Português"):
                        print("-" * 28)
                        print(row)

                elif materia_escolhida == materia_qui:
                    for row in cursor.execute("SELECT * FROM Quimica"):
                        print("-" * 28)
                        print(row)

                else:
                    for row in cursor.execute("SELECT * FROM Fisica"):
                        print("-" * 28)
                        print(row)

                break
        
        else:
            print("Opção invalida ):")
        
        break
