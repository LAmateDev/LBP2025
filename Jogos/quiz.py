# Crie um jogo de perguntas e respostas a partir de uma lista de questões com múltiplas alternativas
# (ou verdadeiro/falso). O sistema deve apresentar uma pergunta de cada vez, permitir que o usuário
# selecione uma resposta e, em seguida, informar se a resposta está correta, atualizando uma pontuação.


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