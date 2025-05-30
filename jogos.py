from Jogos import jogos
from time import sleep

class Minigames():
    def __init__(self):
        self.jogos = ["Adivinhe o Número", "Batalha Naval", "Jogo da Forca", "Torre de Hanoi", "Joquempô", "Quiz"]

    def iniciar(self):
        while True:
            sleep(1)
            print("\nPlataforma de Minijogos")
            print("-" * 30)

            print("1 - Jogar\n"
                  "2 - Sair")

            escolha = int(input("Digite sua escolha: "))
            print("-" * 30)

            if escolha == 1:
                for i, j in enumerate(self.jogos):
                    print(f"{j} -> {i + 1}")
                print("-" * 30)
                opcao = int(input("Digite o número do jogo que deseja jogar: "))
                print("-" * 30)
                if opcao == 1:
                    print(f"Iniciando {self.jogos[0]}")
                    print("-" * 30)
                    jogos.adivinha_numero()
                elif opcao == 2:
                    print(f"Iniciando {self.jogos[1]}")
                    print("-" * 30)
                    jogos.batalha_naval()
                elif opcao == 3:
                    print(f"Iniciando {self.jogos[2]}")
                    print("-" * 30)
                    jogos.forca()
                elif opcao == 4:
                    print(f"Iniciando {self.jogos[3]}")
                    print("-" * 30)
                    jogos.hanoi_tower()
                elif opcao == 5:
                    print(f"Iniciando {self.jogos[4]}")
                    print("-" * 30)
                    jogos.joquempo()
                elif opcao == 6:
                    print(f"Iniciando {self.jogos[5]}")
                    print("-" * 30)
                    jogos.quiz()
                else:
                    print("Digite uma opção válida")

            elif escolha == 2:
                print("Fechando Plataforma...")
                break

            else:
                print("Digite um número válido")

plataforma = Minigames()
plataforma.iniciar()
