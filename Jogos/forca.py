# Implemente o jogo da forca utilizando uma lista predefinida de palavras.
# A cada rodada, uma palavra é escolhida aleatoriamente.
# O usuário tenta adivinhar as letras.
# A interface deve mostrar a palavra parcialmente descoberta, as letras já tentadas
# (corretas e incorretas) e o número de tentativas restantes. O usuário perde se cometer 6 erros.

from random import choice

vidas = 6
palavras = ["python", "java", "codigo", "programar", "operador", "binario"]
palavra = choice(palavras)
letras = [[], []]  # Indice 0: lista de letras corretas / Indice 1: lista de letras incorretas
palavra_escondida = ["_" for l in palavra] # Variavel que utilizaremos para exibir a palavra parcialmente descoberta


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




