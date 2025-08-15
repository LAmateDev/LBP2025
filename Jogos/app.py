from flask import Flask, render_template, request,  session, redirect, url_for
from random import choice,randint
import secrets, json

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# função para carregar os usuarios existentes, usando json
# Desserializa JSON, tarsnforma o JSON em objeto em Python
def carregar_usuarios():
    with open("usuarios.json", "r") as arquivo:
        usuarios = json.load(arquivo)
        return usuarios
    
# Função para salvar o usuario cadastrado no json
# Serializa, transforma o objeto Python para JSON
def cadastrar_usuario(lista_usuarios):
    with open("usuarios.json", "w") as arquivo:
        json.dump(lista_usuarios, arquivo, indent=4)



# executa antes de qualquer rota ser executada
@app.before_request

def verifica_login():
    rotas_livres = ['login', 'home', 'static', 'games', 'criar_conta', 'criar']
    if request.endpoint not in rotas_livres:
        if not session.get("logado"):
            return redirect('/login')

@app.route("/login", methods=["GET", "POST"])

def login():
    mensagem = None
    nome = request.form.get("usuario")
    senha = request.form.get("senha")
    usuarios = carregar_usuarios()

    if request.method == "POST":
        for usuario in usuarios:
            if nome == usuario["nome"] and senha == usuario["senha"]:
                session["logado"] =  True
                return redirect(url_for("home"))
            
        mensagem = "Usuário ou senha inválidos!"
        return render_template("login.html", mensagem = mensagem)

    return render_template("login.html")

@app.route("/criar_conta")

def criar_conta():
    return render_template("CriarConta.html")


@app.route("/criar", methods=["POST"])
def criar():
    erro = None
    nome = request.form.get("usuario")
    senha = request.form.get("senha")
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if nome == usuario["nome"]:
            erro = "Já existe um usuario com esse nome"
            return render_template("CriarConta.html", mensagem = erro)
    
    novo_usuario = {"nome": nome, "senha": senha}
    usuarios.append(novo_usuario)

    cadastrar_usuario(usuarios)
    return redirect(url_for("login"))


@app.route("/sair")

def sair():
    session.clear()
    return render_template("index.html")

@app.route("/games")

def games():
    return render_template("games.html")

@app.route("/")

def home():
    if "logado" in session:
        return render_template("index.html")
    
    return render_template("index.html")


#Adivinhacao

def inicializar_adivinhar_numero():
    session["numero_adivinhar"] = 5
    session["numero_tentativa"] = 0
    session["jogo_terminado"] = False
    
@app.route("/adivinhacao")

def adivinhacao():
    return render_template("jogo_adivinha.html")




#Quiz
gabarito = ["a", "c", "b", "a", "d"]

questoes = [
    {
        "pergunta": "1 - Qual o principal objetivo do paradigma orientado a objetos em programação?",
        "alternativas": {
            "a": "Modelar o software a partir de entidades do mundo real usando conceitos como classes e objetos",
            "b": "Garantir que o programa execute apenas uma vez",
            "c": "Armazenar dados em estruturas de chave-valor",
            "d": "Permitir que o código seja executado de forma assíncrona"
        }
    },
    {
        "pergunta": "2 - Qual das alternativas abaixo é um exemplo de estrutura de dados em programação?",
        "alternativas": {
            "a": "if",
            "b": "return",
            "c": "fila (queue)",
            "d": "while"
        }
    },
    {
        "pergunta": "3 - O que significa o termo imutabilidade em linguagens de programação como Python?",
        "alternativas": {
            "a": "Um dado que não pode ser acessado",
            "b": "Um dado que não pode ser alterado depois de criado",
            "c": "Um dado que pode ser alterado dentro de uma função",
            "d": "Um dado que só pode ser usado dentro de uma classe"
        }
    },
    {
        "pergunta": "4 - Em programação, qual o principal uso de uma expressão lambda?",
        "alternativas": {
            "a": "Definir uma função anônima, geralmente de forma simples e concisa",
            "b": "Definir uma constante para ser usada globalmente",
            "c": "Criar um laço de repetição de forma mais eficiente",
            "d": "Armazenar dados em memória de forma permanente"
        }
    },
    {
        "pergunta": "5 - Em programação, o que significa o conceito de recursão?",
        "alternativas": {
            "a": "Executar várias funções de forma assíncrona",
            "b": "Armazenar uma função como argumento de outra função",
            "c": "Criar uma estrutura de dados que se referencia",
            "d": "Uma função que chama a si mesma durante a execução"
        }
    },
]

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        respostas = [request.form.get(f"q{i+1}") for i in range(len(gabarito))]
        pontos = sum([1 for i in range(len(gabarito)) if respostas[i] == gabarito[i]])
        return render_template("quiz.html", questoes=questoes, resultado=True, pontos=pontos)

    return render_template("quiz.html", questoes=questoes, resultado=False)




#Pedra Papel Tesoura
@app.route("/pedra_papel_tesoura", methods=["GET", "POST"])
def pedra_papel_tesoura():
    # Inicializar placar e estado do jogo
    if "placar" not in session:
        session["placar"] = [0, 0]  # [usuario, computador]
        session["resultado"] = ""
        session["fim_de_jogo"] = False

    if request.method == "POST":
        if session.get("fim_de_jogo"):
            # Reinicia o jogo
            session.pop("placar", None)
            session.pop("resultado", None)
            session.pop("fim_de_jogo", None)
            return redirect(url_for("pedra_papel_tesoura"))

        usuario = request.form.get("escolha")
        computador = choice(['pedra', 'papel', 'tesoura'])
        escolhas = {'pedra': 'papel', 'papel': 'tesoura', 'tesoura': 'pedra'}

        if usuario == computador:
            session["resultado"] = f"Empate! Ambos escolheram {usuario}."
        elif escolhas[computador] == usuario:
            session["placar"][0] += 1
            session["resultado"] = f"Você escolheu {usuario} e o computador {computador}. Você venceu!"
        else:
            session["placar"][1] += 1
            session["resultado"] = f"Você escolheu {usuario} e o computador {computador}. Você perdeu!"

        # Verificar fim de jogo
        if session["placar"][0] == 3:
            session["resultado"] += f" Você ganhou o jogo! Placar final: {session['placar'][0]} x {session['placar'][1]}"
            session["fim_de_jogo"] = True
        elif session["placar"][1] == 3:
            session["resultado"] += f" Você perdeu o jogo! Placar final: {session['placar'][0]} x {session['placar'][1]}"
            session["fim_de_jogo"] = True

    return render_template("pedra_papel_tesoura.html",
                           placar=session.get("placar", [0, 0]),
                           resultado=session.get("resultado", ""),
                           fim_de_jogo=session.get("fim_de_jogo", False))


#HANOI
@app.route("/torre_de_hanoi", methods=["GET", "POST"])
def torre_de_hanoi():
    # Inicializa o jogo
    if "torres" not in session:
        session["torres"] = [[5, 4, 3, 2, 1], [], []]
        session["mensagem"] = ""
        session["vitoria"] = False

    if request.method == "POST":
        # Reiniciar o jogo
        if request.form.get("acao") == "novo_jogo":
            session.pop("torres", None)
            session.pop("mensagem", None)
            session.pop("vitoria", None)
            return redirect(url_for("torre_de_hanoi"))

        origem = int(request.form.get("origem")) - 1
        destino = int(request.form.get("destino")) - 1
        torres = session["torres"]

        if origem not in [0, 1, 2] or destino not in [0, 1, 2]:
            session["mensagem"] = "Torres inválidas. Escolha de 1 a 3."
        elif not torres[origem]:
            session["mensagem"] = "Movimento inválido. A torre de origem está vazia."
        else:
            disco = torres[origem][-1]
            if not torres[destino] or disco < torres[destino][-1]:
                torres[destino].append(torres[origem].pop())
                session["mensagem"] = f"Disco {disco} movido da torre {origem+1} para {destino+1}"
            else:
                session["mensagem"] = "Movimento inválido. Não é possível colocar um disco maior sobre um menor."

        # Verifica vitória
        if torres[1] == [5, 4, 3, 2, 1] or torres[2] == [5, 4, 3, 2, 1]:
            session["vitoria"] = True
            session["mensagem"] = "Parabéns! Você venceu!"

        session["torres"] = torres

    return render_template("torre_de_hanoi.html",
                           torres=session.get("torres"),
                           mensagem=session.get("mensagem", ""),
                           vitoria=session.get("vitoria", False))



#batalha naval
def iniciar_jogo():
    global tabuleiro, navios, cont
    tabuleiro = [[0 for _ in range(6)] for _ in range(6)]
    navios = []
    while len(navios) < 3:
        navio = [randint(0, 5), randint(0, 5)]
        if navio not in navios:
            navios.append(navio)
    cont = 0



@app.route("/batalha", methods=["GET", "POST"])
def batalha():
    # Inicializa jogo se não existir
    if "tabuleiro" not in session or "navios" not in session:
        session["tabuleiro"] = [[0 for _ in range(6)] for _ in range(6)]
        navios = []
        while len(navios) < 3:
            ponto = [randint(0, 5), randint(0, 5)]
            if ponto not in navios:
                navios.append(ponto)
        session["navios"] = navios
        session["cont"] = 0
        session["fim"] = False

    mensagem = ""
    fim = session.get("fim", False)
    tabuleiro = session["tabuleiro"]
    navios = session["navios"]
    cont = session["cont"]

    if request.method == "POST":
        linha = int(request.form["linha"])
        coluna = int(request.form["coluna"])
        ponto = [linha, coluna]

        if tabuleiro[linha][coluna] != 0:
            mensagem = "Você já atacou este ponto."
        else:
            cont += 1
            if ponto in navios:
                tabuleiro[linha][coluna] = "X"
                navios.remove(ponto)
                mensagem = "Você acertou e destruiu um navio!"
            else:
                tabuleiro[linha][coluna] = "."
                mensagem = "Você acertou a água."

            if not navios:
                mensagem = f"Você destruiu todos os navios com {cont} tentativas!"
                fim = True

        # Atualiza sessão
        session["tabuleiro"] = tabuleiro
        session["navios"] = navios
        session["cont"] = cont
        session["fim"] = fim

    return render_template("batalha.html", tabuleiro=tabuleiro, mensagem=mensagem, fim=fim)

@app.route("/novo-jogo")
def novo_jogo():
    session.pop("tabuleiro", None)
    session.pop("navios", None)
    session.pop("cont", None)
    session.pop("fim", None)
    return redirect(url_for("batalha"))


#Forca
PALAVRAS = ["python", "java", "codigo", "programar", "operador", "binario"]

@app.route('/forca', methods=['GET', 'POST'])
def forca():
    if 'palavra' not in session:
        palavra = choice(PALAVRAS)
        session['palavra'] = palavra
        session['vidas'] = 6
        session['letras_corretas'] = []
        session['letras_erradas'] = []
        session['palavra_escondida'] = ["_" for _ in palavra]

    palavra = session['palavra']
    vidas = session['vidas']
    letras_corretas = session['letras_corretas']
    letras_erradas = session['letras_erradas']
    palavra_escondida = session['palavra_escondida']
    mensagem = ""

    if request.method == 'POST':
        letra = request.form['letra'].lower()

        if letra in palavra:
            if letra not in letras_corretas:
                letras_corretas.append(letra)
                for i, l in enumerate(palavra):
                    if l == letra:
                        palavra_escondida[i] = letra
                mensagem = f"Você acertou! A letra '{letra}' está na palavra."
            else:
                mensagem = f"A letra '{letra}' já foi usada."
        else:
            if letra not in letras_erradas:
                letras_erradas.append(letra)
                vidas -= 1
                mensagem = f"Você errou! A letra '{letra}' não está na palavra."
            else:
                mensagem = f"A letra '{letra}' já foi usada."

    session['vidas'] = vidas
    session['letras_corretas'] = letras_corretas
    session['letras_erradas'] = letras_erradas
    session['palavra_escondida'] = palavra_escondida

    venceu = "".join(palavra_escondida) == palavra
    perdeu = vidas == 0

    if venceu:
        mensagem = f"Parabéns! Você venceu com {vidas} vidas restantes. A palavra era '{palavra}'"
    elif perdeu:
        mensagem = f"Você perdeu! A palavra era '{palavra}'"

    return render_template('forca.html',
                           palavra_escondida=palavra_escondida,
                           letras_corretas=letras_corretas,
                           letras_erradas=letras_erradas,
                           vidas=vidas,
                           mensagem=mensagem,
                           fim=venceu or perdeu)

@app.route('/novo_jogo')
def novo_jogo_forca():
    session.clear()
    return redirect(url_for('forca'))




if __name__ == "__main__":
    app.run(debug=True)