# Batalha naval simples, usuario x computador, com navios de proporção 1x1

from random import randint

tabuleiro = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

def exibe_tabuleiro(tabuleiro):
    print("   0 1 2 3 4 5")
    for i in range(len(tabuleiro)):
        print(f"{i}| ", end="")
        for l in range(len(tabuleiro[i])):
            print(f"{tabuleiro[i][l]}", end=" ")
        print()


navio1 = [randint(0, 5), randint(0, 5)]
navio2 = [randint(0, 5), randint(0, 5)]
navio3 = [randint(0, 5), randint(0, 5)]

navios = [navio1, navio2, navio3]
cont = 0

while True:

    exibe_tabuleiro(tabuleiro)
    if len(navios) == 0:
        print(f"Você destruiu todos os navios inimigos com {cont} tentativas")
        break

    print("Digite a coordenada que deseja atacar Ex[1, 4]")
    ponto = [int(input("Digite a linha: ")), int(input("Digite a coluna: "))]

    if ponto in navios:
        tabuleiro[ponto[0]][ponto[1]] = "X"
        print("Você acertou e destruiu um navio!")
        navios.remove(ponto)
    
    else:
        tabuleiro[ponto[0]][ponto[1]] = "."
        print("Você acertou a água")
    
    cont += 1

