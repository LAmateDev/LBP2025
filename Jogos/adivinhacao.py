# O sistema gera um número aleatório dentro de um intervalo definido (ex: 1 a 100).
# O usuário tenta adivinhar qual é o número. Após cada tentativa, o sistema informa se o palpite do usuário
# foi muito alto, muito baixo ou se acertou. Opcionalmente, pode contar o número de tentativas.

from time import sleep
from random import randint

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