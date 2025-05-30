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


