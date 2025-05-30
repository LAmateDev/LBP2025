from time import sleep
from random import randint, choice

def adivinha_numero():
    cont = 1
    print("JOGO DA ADIVINHAÇÃO\nO computador vai pensar em um número de 1 a 100\n"
          "Tente acertar com o menor número de tentativas")
    print("=-" * 30)
    sleep(2)
    print("Computador escolhendo número...")
    sleep(1)
    computador = randint(1, 100)
    print("Número escolhido!")

    while True:

        usuario = int(input("Seu palpite: "))

        if usuario == computador:
            print(f"O computador pensou no número {computador} e você {usuario}\nVocê venceu com {cont} tentativas!")
            break

        elif usuario > computador:
            print("Palpite muito alto")

        else:
            print("Palpite muito baixo")

        cont += 1


def batalha_naval():
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


def forca():
    vidas = 6
    palavras = ["python", "java", "codigo", "programar", "operador", "binario"]
    palavra = choice(palavras)
    letras = [[], []]  # Indice 0: lista de letras corretas / Indice 1: lista de letras incorretas
    palavra_escondida = ["_" for l in
                         palavra]  # Variavel que utilizaremos para exibir a palavra parcialmente descoberta

    while True:

        if "".join(palavra_escondida) == palavra:
            print(f"Você venceu com {vidas} vidas restantes! A palavra era {palavra}")
            break

        if vidas == 0:
            print(f"Suas vidas acabaram, você perdeu! A palavra era {palavra}")
            break

        print(f"Letras escolhidas:\n"
              f"Corretas: {letras[0]}\n"
              f"Incorretas: {letras[1]}")
        print(f"Vidas restantes: {vidas}")

        for e in palavra_escondida:
            print(e, end="")
        print()
        letra = input("Seu palpite de letra: ")
        if letra in palavra:
            letras[0].append(letra)
            print(f"Você acertou! a letra {letra} está na palavra")
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_escondida[i] = letra
        else:
            print(f"Você errou! a letra {letra} não está na palavra")
            vidas -= 1
            letras[1].append(letra)

        # Exibição da palavra parcialmente descoberta

        for e in palavra_escondida:
            print(e, end="")
        print()


def hanoi_tower():
    torres = [[5, 4, 3, 2, 1], [], []]

    while True:

        for i, l in enumerate(torres):
            print(f"T{i + 1}", end=" - ")
            for e in l:
                print(e, end=" ")
            print()

        if torres[1] == [5, 4, 3, 2, 1] or torres[2] == [5, 4, 3, 2, 1]:
            print("Você venceu!")
            break

        torre = int(input("Digite a torre que deseja mexer (1, 2, 3): "))
        if len(torres[torre - 1]) > 0:
            disco = torres[torre - 1][-1]
            destino = int(input(f"Para qual torre deseja mover o disco {disco}: "))

            if len(torres[destino - 1]) == 0 or torres[torre - 1][-1] < torres[destino - 1][-1]:
                torres[destino - 1].append(disco)
                torres[torre - 1].remove(disco)
            else:
                print("Movimento Inválido\nNão é possível empilhar um disco maior sobre um menor")
        else:
            print("Movimento inválido. Não há discos nesta torre")


def joquempo():
    escolhas = {'pedra': 'papel', 'papel': 'tesoura', 'tesoura': 'pedra'}

    placar = [0, 0]  # Indice 0: Usuario, Indice 1: Computador

    print("PEDRA, PAPEL, TESOURA\nVocê contra o computador!\nO primeiro a fazer 3 pontos ganha")
    sleep(2)

    while True:

        computador = choice(['pedra', 'papel', 'tesoura'])

        if placar[0] == 3:
            print(f"Você venceu!\nPlacar final: {placar[0]}x{placar[1]}")
            break

        if placar[1] == 3:
            print(f"Você perdeu!\nPlacar final: {placar[0]}x{placar[1]}")
            break

        usuario = input("Sua escolha: ").strip().lower()

        if usuario == escolhas[computador]:
            placar[0] += 1
            print(f"Você escolheu {usuario} e o computador {computador}\nVocê venceu!\n"
                  f"Placar: {placar[0]}x{placar[1]}  --> Usuario x computador")

        elif usuario == computador:
            print(f"Você escolheu {usuario} e o computador {computador}\nEMPATE")

        else:
            placar[1] += 1
            print(f"Você escolheu {usuario} e o computador {computador}\nVocê perdeu!\n"
                  f"Placar: {placar[0]}x{placar[1]}  --> Usuario x Computador")


def quiz():
    gabarito = ["a", "c", "b", "a", "d"]
    pontos = 0
    print("Quiz de Programação")
    print("Para cada questão selecione apenas uma alternativa: ")

    questao1 = ("1 - Qual o principal objetivo do paradigma orientado a objetos em programação?\n"
                "a) Modelar o software a partir de entidades do mundo real usando conceitos como classes e objetos\n"
                "b) Garantir que o programa execute apenas uma vez\n"
                "c) Armazenar dados em estruturas de chave-valor\n"
                "d) Permitir que o código seja executado de forma assíncrona")

    questao2 = ("2 - Qual das alternativas abaixo é um exemplo de estrutura de dados em programação?\n"
                "a) if\n"
                "b) return\n"
                "c) fila (queue)\n"
                "d) while")

    questao3 = (" 3 - O que significa o termo imutabilidade em linguagens de programação como Python?\n"
                "a) Um dado que não pode ser acessado\n"
                "b) Um dado que não pode ser alterado depois de criado\n"
                "c) Um dado que pode ser alterado dentro de uma função\n"
                "d) Um dado que só pode ser usado dentro de uma classe")

    questao4 = (" 4 - Em programação, qual o principal uso de uma expressão lambda?\n"
                "a) Definir uma função anônima, geralmente de forma simples e concisa\n"
                "b) Definir uma constante para ser usada globalmente\n"
                "c) Criar um laço de repetição de forma mais eficiente\n"
                "d) Armazenar dados em memória de forma permanente")

    questao5 = (" 5 - Em programação, o que significa o conceito de recursão?\n"
                "a) Executar várias funções de forma assíncrona\n"
                "b) Armazenar uma função como argumento de outra função\n"
                "c) Criar uma estrutura de dados que se referencia\n"
                "d) Uma função que chama a si mesma durante a execução")

    questoes = [questao1, questao2, questao3, questao4, questao5]
    for i in range(len(gabarito)):
        print(questoes[i])
        print()
        resposta = input("Digite a alternativa correta: ").strip().lower()
        if resposta == gabarito[i]:
            print("Você selecionou a alternativa correta!")
            pontos += 1
        else:
            print(f"Você selecionou a alternativa incorreta! Alternativa correta: {gabarito[i]}")

    print(f"Fim do Quiz, você fez {pontos} pontos")
