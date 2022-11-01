import heapq
import sqlite3
import time
import biblioteca_funções


def main():
    conexao = sqlite3.connect('banco_de_dados_anchieta.db')
    cursor = conexao.cursor()

    print("-" * 28)
    print('\033[34mCalcular notas [1]\nVer notas e médias [2]\033[m')
    inserir_menu = int(input("Selecione a ação desejada: "))
    calcular_notas = 1
    ver_notas = 2

    if inserir_menu == calcular_notas:
        while True:
            print("-" * 28)
            print(
                '\033[33mMatematica [1]\nGeografia [2]\nHistoria [3]\nPortuguês [4]\nQuimica [5]\nFisica [6]\nBiologia [7]')

            materia_mat = 1
            materia_geo = 2
            materia_hist = 3
            materia_port = 4
            materia_qui = 5
            materia_fis = 6
            materia_bio = 7

            materia_escolhida = int(
                input("Escolha a materia calculada (Precisa ser um numero): \033[m"))

            if ((materia_escolhida > 0) and (materia_escolhida <= 7)):

                print('-------1° trimestre--------')
                g1 = int(input("Nota da g1: "))
                g2 = int(input("Nota da g2: "))
                g3 = int(input("Nota da g3: "))
                
                p1 = int(input("Diversificada: "))
                p2 = int(input("Pontos extras: "))

                lista1 = [g1, g2, g3]
                pe = p1 + p2
                nt1 = max(lista1)
                nt2 = (heapq.nlargest(2, lista1)[-1])
                mdp = round((nt1 + nt2)/2) + pe

                print('-------2° trimestre--------')
                globo1 = int(input("Nota da g1: "))
                globo2 = int(input("Nota da g2: "))
                globo3 = int(input("Nota da g3: "))
                
                px1 = int(input("Diversificadas: "))
                px2 = int(input("Pontos extras: "))

                lista2 = [globo1, globo2, globo3]
                
                pxe = px1 + px2
                nota1 = max(lista2)
                nota2 = (heapq.nlargest(2, lista2)[-1])
                media = round((nota1 + nota2)/2) + pxe
                ptf = 180 - (media + mdp)

                print("-" * 28)

                if ptf <= 0:
                    print('''\033[32mMedia do 1° trimestre: {}\nMedia do 2° trimestre: {}\nVocê já passou de ano, parabéns!'''.format(
                        mdp, media))
                    ptf = 0
                    rapariga = "passou"

                else:
                    print('''\033[31mMedia do 1° trimestre: {}\nMedia do 2° trimestre: {}\nFaltam {} pontos para passar de ano!'''.format(
                        mdp, media, ptf))
                    rapariga = "não passou"

            else:
                print("\033[31mOpção Invalida\033[m")

                repe = input(
                    "\033[35mDeseja reiniciar o programa? [S/N]\033[m").upper()

                if repe == "S":
                    main()

                else:
                    print("Programa encerrado :(")
                    exit()

            while ((materia_escolhida > 0) and (materia_escolhida <= 7)):

                if materia_escolhida == materia_mat:
                    cursor.execute(
                        f"INSERT INTO Matematica VALUES ('{nt1}', '{nt2}', '{mdp}', '{nota1}', '{nota2}', '{media}', '{rapariga}', '{ptf}')")
                    conexao.commit()
                elif materia_escolhida == materia_geo:
                    cursor.execute(
                        f"INSERT INTO Geografia VALUES ('{nt1}', '{nt2}', '{mdp}', '{nota1}', '{nota2}', '{media}', '{rapariga}', '{ptf}')")
                    conexao.commit()
                elif materia_escolhida == materia_hist:
                    cursor.execute(
                        f"INSERT INTO Historia VALUES ('{nt1}', '{nt2}', '{mdp}', '{nota1}', '{nota2}', '{media}', '{rapariga}', '{ptf}')")
                    conexao.commit()
                elif materia_escolhida == materia_port:
                    cursor.execute(
                        f"INSERT INTO Português VALUES ('{nt1}', '{nt2}', '{mdp}', '{nota1}', '{nota2}', '{media}', '{rapariga}', '{ptf}')")
                    conexao.commit()
                elif materia_escolhida == materia_qui:
                    cursor.execute(
                        f"INSERT INTO Quimica VALUES ('{nt1}', '{nt2}', '{mdp}', '{nota1}', '{nota2}', '{media}', '{rapariga}', '{ptf}')")
                    conexao.commit()
                elif materia_escolhida == materia_fis:
                    cursor.execute(
                        f"INSERT INTO Fisica VALUES ('{nt1}', '{nt2}', '{mdp}', '{nota1}', '{nota2}', '{media}', '{rapariga}', '{ptf}')")
                    conexao.commit()
                else:
                    cursor.execute(
                        f"INSERT INTO Biologia VALUES ('{nt1}', '{nt2}', '{mdp}', '{nota1}', '{nota2}', '{media}', '{rapariga}', '{ptf}')")
                    conexao.commit()

                repe = input(
                    "\033[35mDeseja reiniciar o programa? [S/N]\033[m").upper()

                if repe == "S":
                    main()

                else:
                    print("Programa encerrado :(")
                    exit()

                break
            break
    elif inserir_menu == ver_notas:
        while True:
            print("-" * 28)
            print(
                '\033[33mMatematica [1]\nGeografia [2]\nHistoria [3]\nPortuguês [4]\nQuimica [5]\nFisica [6]\nBiologia [7]\033[m')

            materia_mat = 1
            materia_geo = 2
            materia_hist = 3
            materia_port = 4
            materia_qui = 5
            materia_fis = 6
            materia_bio = 7

            materia_escolhida = int(
                input("Escolha a materia que vai ser visualizada (Precisa ser um numero): "))

            if ((materia_escolhida > 0) and (materia_escolhida <= 7)):
                while True:

                    print("-" * 28)

                    print("\033[35mCarregando 'banco_de_dados_anchieta'\033[m")
                    print(' ')
                    time.sleep(2)

                    print(
                        "\033[33mModelo para visualização de dados:\n('Média do 1° tri', 'Média do 2° tri', 'Situação final', 'Pontos para passar')")
                    print(' ')
                    print('---Notas---\033[m')

                    if materia_escolhida == materia_mat:
                        for row in cursor.execute("SELECT m_mdp, m_media, rapariga, m_pf FROM Matematica"):
                            print(row)
                    elif materia_escolhida == materia_geo:
                        for row in cursor.execute("SELECT g_mdp, g_media, rapariga, g_pf FROM Geografia"):
                            print(row)
                    elif materia_escolhida == materia_hist:
                        for row in cursor.execute("SELECT h_mdp, h_media, rapariga, h_pf FROM Historia"):
                            print(row)
                    elif materia_escolhida == materia_port:
                        for row in cursor.execute("SELECT p_mdp, p_media, rapariga, p_pf FROM Português"):
                            print(row)
                    elif materia_escolhida == materia_qui:
                        for row in cursor.execute("SELECT q_mdp, q_media, rapariga, q_pf FROM Quimica"):
                            print(row)
                    elif materia_escolhida == materia_fis:
                        for row in cursor.execute("SELECT f_mdp, f_media, rapariga, f_pf FROM Fisica"):
                            print(row)
                    else:
                        for row in cursor.execute("SELECT b_mdp, b_media, rapariga, b_pf FROM Biologia"):
                            print(row)

                    repe = input(
                        "\033[35mDeseja reiniciar o programa? [S/N]\033[m").upper()

                    if repe == "S":
                        main()

                    else:
                        print("Programa encerrado :(")
                        exit()

                    break

            else:
                print("\033[31mOpção Invalida\033[m")

                repe = input(
                    "\033[35mDeseja reiniciar o programa? [S/N]\033[m").upper()

                if repe == "S":
                    main()

                else:
                    print("Programa encerrado :(")
                    exit()

            break

    else:
        print("\033[31mOpção Invalida\033[m")

        repe = input(
            "\033[35mDeseja reiniciar o programa? [S/N]\033[m").upper()

        if repe == "S":
            main()

        else:
            print("Programa encerrado :(")
            exit()


main()
