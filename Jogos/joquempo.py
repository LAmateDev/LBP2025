# Desenvolva o clássico jogo onde o usuário escolhe entre Pedra, Papel ou Tesoura.
# O computador fará a sua escolha aleatoriamente. O sistema então determina e exibe o vencedor da rodada
# (usuário, computador ou empate) e, opcionalmente, mantém um placar.

from random import choice
from time import sleep

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



