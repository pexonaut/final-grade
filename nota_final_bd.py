import heapq
import sqlite3
import time


def main():
    conexao = sqlite3.connect('banco_de_dados_anchieta.db')
    cursor = conexao.cursor()

    print("-" * 28)
    print('\033[34mCalcular notas [1]\nVer notas e médias [2]\033[m')
    inserir_menu = input("Selecione a ação desejada: ")

    if inserir_menu == "1" and inserir_menu.isdigit():
        inserir_menu = int(inserir_menu)

        while True:
            print("-" * 28)
            print(
                '\033[33mMatematica [1]\nGeografia [2]\nHistoria [3]\nPortuguês [4]\nQuimica [5]\nFisica [6]\nBiologia [7]')

            materia_escolhida = input(
                "Escolha a materia calculada (Precisa ser um numero): \033[m")

            if ((materia_escolhida == "1", "2", "3", "4", "5", "6", "7") and (materia_escolhida.isdigit())):

                materia_escolhida = int(materia_escolhida)

                materia_mat = 1
                materia_geo = 2
                materia_hist = 3
                materia_port = 4
                materia_qui = 5
                materia_fis = 6
                materia_bio = 7

                def calcular_notas():
                    print('-------1° trimestre--------')

                    g1 = input("Nota da g1: ")

                    if g1.isdigit():
                        g1 = int(g1)
                    else:
                        print("\033[31mOpção Invalida\033[m")
                        repe = input(
                            "\033[35mDeseja voltar para o 1° trimestre? [S/N]\033[m").upper()

                        if repe == "S":
                            calcular_notas()

                        else:
                            repe = input(
                                "\033[35mDeseja voltar para o menu principal? [S/N]\033[m").upper()
                            if repe == "S":
                                main()
                            else:
                                print("Programa encerrado :(")
                                exit()

                    g2 = input("Nota da g2: ")

                    if g2.isdigit():
                        g2 = int(g2)
                    else:
                        print("\033[31mOpção Invalida\033[m")
                        repe = input(
                            "\033[35mDeseja voltar para o 1° trimestre? [S/N]\033[m").upper()

                        if repe == "S":
                            calcular_notas()

                        else:
                            repe = input(
                                "\033[35mDeseja voltar para o menu principal? [S/N]\033[m").upper()
                            if repe == "S":
                                main()
                            else:
                                print("Programa encerrado :(")
                                exit()

                    g3 = input("Nota da g3: ")

                    if g3.isdigit():
                        g3 = int(g3)
                    else:
                        print("\033[31mOpção Invalida\033[m")
                        repe = input(
                            "\033[35mDeseja voltar para o 1° trimestre? [S/N]\033[m").upper()

                        if repe == "S":
                            calcular_notas()

                        else:
                            repe = input(
                                "\033[35mDeseja voltar para o menu principal? [S/N]\033[m").upper()
                            if repe == "S":
                                main()
                            else:
                                print("Programa encerrado :(")
                                exit()

                    p1 = input("Diversificada: ")

                    if p1.isdigit():
                        p1 = int(p1)
                    else:
                        print("\033[31mOpção Invalida\033[m")
                        repe = input(
                            "\033[35mDeseja voltar para o 1° trimestre? [S/N]\033[m").upper()

                        if repe == "S":
                            calcular_notas()

                        else:
                            repe = input(
                                "\033[35mDeseja voltar para o menu principal? [S/N]\033[m").upper()
                            if repe == "S":
                                main()
                            else:
                                print("Programa encerrado :(")
                                exit()

                    p2 = input("Pontos extras: ")

                    if p2.isdigit():
                        p2 = int(p2)
                    else:

                        print("\033[31mOpção Invalida\033[m")
                        repe = input(
                            "\033[35mDeseja voltar para o 1° trimestre? [S/N]\033[m").upper()

                        if repe == "S":
                            calcular_notas()

                        else:
                            repe = input(
                                "\033[35mDeseja voltar para o menu principal? [S/N]\033[m").upper()
                            if repe == "S":
                                main()
                            else:
                                print("Programa encerrado :(")
                                exit()

                    lista1 = [g1, g2, g3]
                    pe = p1 + p2
                    nt1 = max(lista1)
                    nt2 = (heapq.nlargest(2, lista1)[-1])
                    mdp = round((nt1 + nt2)/2) + pe

                    print('-------2° trimestre--------')

                    globo1 = input("Nota da g1: ")

                    if globo1.isdigit():
                        globo1 = int(globo1)
                    else:
                        print("\033[31mOpção Invalida\033[m")
                        repe = input(
                            "\033[35mDeseja voltar para o 1° trimestre? [S/N]\033[m").upper()

                        if repe == "S":
                            calcular_notas()

                        else:
                            repe = input(
                                "\033[35mDeseja voltar para o menu principal? [S/N]\033[m").upper()
                            if repe == "S":
                                main()
                            else:
                                print("Programa encerrado :(")
                                exit()

                    globo2 = input("Nota da g2: ")

                    if globo2.isdigit():
                        globo2 = int(globo2)
                    else:
                        print("\033[31mOpção Invalida\033[m")
                        repe = input(
                            "\033[35mDeseja voltar para o 1° trimestre? [S/N]\033[m").upper()

                        if repe == "S":
                            calcular_notas()

                        else:
                            repe = input(
                                "\033[35mDeseja voltar para o menu principal? [S/N]\033[m").upper()
                            if repe == "S":
                                main()
                            else:
                                print("Programa encerrado :(")
                                exit()

                    globo3 = input("Nota da g3: ")

                    if globo3.isdigit():
                        globo3 = int(globo3)
                    else:
                        print("\033[31mOpção Invalida\033[m")
                        repe = input(
                            "\033[35mDeseja voltar para o 1° trimestre? [S/N]\033[m").upper()

                        if repe == "S":
                            calcular_notas()

                        else:
                            repe = input(
                                "\033[35mDeseja voltar para o menu principal? [S/N]\033[m").upper()
                            if repe == "S":
                                main()
                            else:
                                print("Programa encerrado :(")
                                exit()

                    px1 = input("Diversificadas: ")

                    if px1.isdigit():
                        px1 = int(px1)
                    else:
                        print("\033[31mOpção Invalida\033[m")
                        repe = input(
                            "\033[35mDeseja voltar para o 1° trimestre? [S/N]\033[m").upper()

                        if repe == "S":
                            calcular_notas()

                        else:
                            repe = input(
                                "\033[35mDeseja voltar para o menu principal? [S/N]\033[m").upper()
                            if repe == "S":
                                main()
                            else:
                                print("Programa encerrado :(")
                                exit()

                    px2 = input("Pontos extras: ")

                    if px2.isdigit():
                        px2 = int(px2)
                    else:
                        print("\033[31mOpção Invalida\033[m")
                        repe = input(
                            "\033[35mDeseja voltar para o 1° trimestre? [S/N]\033[m").upper()

                        if repe == "S":
                            main()

                        else:
                            repe = input(
                                "\033[35mDeseja voltar para o menu principal? [S/N]\033[m").upper()
                            if repe == "S":
                                main()
                            else:
                                print("Programa encerrado :(")
                                exit()

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

                    repe = input(
                        "\033[35mDeseja confirmar essas notas? [S/N]\033[m").upper()

                    if repe == "S":
                        print("\033[32mNotas salvas com sucesso!!\033[m")

                    elif repe == "N":
                        repe = input(
                            "\033[35mDeseja refazer as notas? [S/N]\033[m").upper()
                        if repe == "S":
                            calcular_notas()
                        else:
                            repe = input(
                                "\033[35mDeseja voltar ao menu principal? [S/N]\033[m").upper()
                            if repe == "S":
                                main()
                            else:
                                print("Programa encerrado :(")
                                exit()

                    else:
                        print("\033[31mOpção Invalida\033[m")
                        repe = input(
                            "\033[35mDeseja voltar para o 1° trimestre? [S/N]\033[m").upper()

                        if repe == "S":
                            main()

                        else:
                            repe = input(
                                "\033[35mDeseja voltar para o menu principal? [S/N]\033[m").upper()
                            if repe == "S":
                                main()
                            else:
                                print("Programa encerrado :(")
                                exit()

                    cursor.execute(
                        'CREATE TABLE IF NOT EXISTS "Matematica" ("m_nt1" NUMERIC, "m_nt2" NUMERIC, "m_mdp" NUMERIC, "m_nota1" NUMERIC, "m_nota2" NUMERIC, "m_media" NUMERIC, "rapariga" INTEGER, "m_pf" NUMERIC)')
                    cursor.execute(
                        'CREATE TABLE IF NOT EXISTS "Geografia" ("g_nt1" NUMERIC, "g_nt2" NUMERIC, "g_mdp" NUMERIC, "g_nota1" NUMERIC, "g_nota2" NUMERIC, "g_media" NUMERIC, "rapariga" INTEGER, "g_pf" NUMERIC)')
                    cursor.execute(
                        'CREATE TABLE IF NOT EXISTS "Historia" ("h_nt1" NUMERIC, "h_nt2" NUMERIC, "h_mdp" NUMERIC, "h_nota1" NUMERIC, "h_nota2" NUMERIC, "h_media" NUMERIC,"rapariga" INTEGER, "h_pf" NUMERIC)')
                    cursor.execute(
                        'CREATE TABLE IF NOT EXISTS "Português" ("p_nt1" NUMERIC, "p_nt2" NUMERIC, "p_mdp" NUMERIC, "p_nota1" NUMERIC, "p_nota2" NUMERIC, "p_media" NUMERIC,"rapariga" INTEGER, "p_pf" NUMERIC)')
                    cursor.execute(
                        'CREATE TABLE IF NOT EXISTS "Quimica" ("q_nt1" NUMERIC, "q_nt2" NUMERIC, "q_mdp" NUMERIC, "q_nota1" NUMERIC, "q_nota2" NUMERIC, "q_media" NUMERIC,"rapariga" INTEGER, "q_pf" NUMERIC)')
                    cursor.execute(
                        'CREATE TABLE IF NOT EXISTS "Fisica" ("f_nt1" NUMERIC, "f_nt2" NUMERIC, "f_mdp" NUMERIC, "f_nota1" NUMERIC, "f_nota2" NUMERIC, "f_media" NUMERIC,"rapariga" INTEGER, "f_pf" NUMERIC)')
                    cursor.execute(
                        'CREATE TABLE IF NOT EXISTS "Biologia" ("b_nt1" NUMERIC, "b_nt2" NUMERIC, "b_mdp" NUMERIC, "b_nota1" NUMERIC, "b_nota2" NUMERIC, "b_media" NUMERIC,"rapariga" INTEGER, "b_pf" NUMERIC)')

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
                    elif materia_escolhida == materia_bio:
                        cursor.execute(
                            f"INSERT INTO Biologia VALUES ('{nt1}', '{nt2}', '{mdp}', '{nota1}', '{nota2}', '{media}', '{rapariga}', '{ptf}')")
                        conexao.commit()
                    else:
                        print(materia_escolhida)
                        print(type(materia_escolhida))

                    repe = input(
                        "\033[35mDeseja reiniciar o programa? [S/N]\033[m").upper()

                    if repe == "S":
                        main()

                    else:
                        print("Programa encerrado :(")
                        exit()

                calcular_notas()

            else:
                repe = input(
                    "\033[35mDeseja votar para o menu principal? [S/N]\033[m").upper()

                if repe == "S":
                    main()
                else:
                    print("Programa encerrado :(")
                    exit()

            break

    elif inserir_menu == "2" and inserir_menu.isdigit():
        inserir_menu = int(inserir_menu)
        while True:
            print("-" * 28)
            print(
                '\033[33mMatematica [1]\nGeografia [2]\nHistoria [3]\nPortuguês [4]\nQuimica [5]\nFisica [6]\nBiologia [7]\033[m')

            materia_escolhida = input(
                "Escolha a materia que vai ser visualizada (Precisa ser um numero): ")

            if ((materia_escolhida == "1", "2", "3", "4", "5", "6", "7") and (materia_escolhida.isdigit())):

                materia_escolhida = int(materia_escolhida)

                materia_mat = 1
                materia_geo = 2
                materia_hist = 3
                materia_port = 4
                materia_qui = 5
                materia_fis = 6
                materia_bio = 7

                print("-" * 28)

                print(
                    "\033[35mCarregando 'banco_de_dados_anchieta'\033[m")
                print(' ')

                # criar as tabelas
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS "Matematica" ("m_nt1" NUMERIC, "m_nt2" NUMERIC, "m_mdp" NUMERIC, "m_nota1" NUMERIC, "m_nota2" NUMERIC, "m_media" NUMERIC, "rapariga" INTEGER, "m_pf" NUMERIC)')
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS "Geografia" ("g_nt1" NUMERIC, "g_nt2" NUMERIC, "g_mdp" NUMERIC, "g_nota1" NUMERIC, "g_nota2" NUMERIC, "g_media" NUMERIC, "rapariga" INTEGER, "g_pf" NUMERIC)')
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS "Historia" ("h_nt1" NUMERIC, "h_nt2" NUMERIC, "h_mdp" NUMERIC, "h_nota1" NUMERIC, "h_nota2" NUMERIC, "h_media" NUMERIC,"rapariga" INTEGER, "h_pf" NUMERIC)')
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS "Português" ("p_nt1" NUMERIC, "p_nt2" NUMERIC, "p_mdp" NUMERIC, "p_nota1" NUMERIC, "p_nota2" NUMERIC, "p_media" NUMERIC,"rapariga" INTEGER, "p_pf" NUMERIC)')
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS "Quimica" ("q_nt1" NUMERIC, "q_nt2" NUMERIC, "q_mdp" NUMERIC, "q_nota1" NUMERIC, "q_nota2" NUMERIC, "q_media" NUMERIC,"rapariga" INTEGER, "q_pf" NUMERIC)')
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS "Fisica" ("f_nt1" NUMERIC, "f_nt2" NUMERIC, "f_mdp" NUMERIC, "f_nota1" NUMERIC, "f_nota2" NUMERIC, "f_media" NUMERIC,"rapariga" INTEGER, "f_pf" NUMERIC)')
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS "Biologia" ("b_nt1" NUMERIC, "b_nt2" NUMERIC, "b_mdp" NUMERIC, "b_nota1" NUMERIC, "b_nota2" NUMERIC, "b_media" NUMERIC,"rapariga" INTEGER, "b_pf" NUMERIC)')

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
