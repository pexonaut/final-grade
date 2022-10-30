import heapq

def calcular_notas(g1, g2, g3, pe, globo1, globo2, globo3, pxe):
    
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

    lista2 = [globo1, globo2, globo3]
    nota1 = max(lista2)
    nota2 = (heapq.nlargest(2, lista2)[-1])
    media = round((nota1 + nota2)/2) + pxe
    ptf = 180 - (media + mdp)

    return nt1, nt2, mdp, nota1, nota2, media, ptf
