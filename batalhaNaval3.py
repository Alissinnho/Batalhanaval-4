# Funções

def criarTabuleiro():
    matriz = []
    for i in range(5):
        linhas = []
        for j in range(10):
            linhas.append('0')
        matriz.append(linhas)
    return matriz

def imprimirTabuleiro(tabuleiro):
    contador = 1
    print("    1.   2.   3.   4.   5.   6.   7.   8.   9.   10. ")
    for linha in tabuleiro:
        print(f"{contador}.{linha}")
        contador += 1


def posicionarJogador(tabuleiro):
    print("Escolha as posições dos barcos")
    contador = 0
    while contador < 5:
        escolhaLinha = int(input("Escolha a linha (1 - 5): ")) - 1
        escolhaColuna = int(input("Escolha a coluna (1 - 10): ")) - 1
        if escolhaLinha < 0 or escolhaLinha > 4 or escolhaColuna < 0 or escolhaColuna > 9:
            print("Digite uma posição válida!")
            print()
        elif tabuleiro[escolhaLinha][escolhaColuna] == '0':
            print("posição escolhida com sucesso!")
            print()
            tabuleiro[escolhaLinha][escolhaColuna] = 'x'
            contador += 1
        else:
            print("posição já escolhida")
            print()
    print(f"Tabuleiro final: ")
    imprimirTabuleiro(tabuleiroJogador)

def jogadaJogador(tabuleiroatacado,vidaOponente,tabuleiroFalso):
    while True:
        print("Faça sua jogada!")
        jogadaLinha = int(input("Escolha a linha (1 - 5): ")) - 1
        jogadaColuna = int(input("Escolha a Coluna (1 - 10): ")) - 1
        if jogadaLinha < 0 or jogadaLinha > 4 or jogadaColuna < 0 or jogadaColuna > 9:
            print("Digite uma posição válida!")
            print("------------------------------------------")
            imprimirTabuleiro(tabuleiroFalso)
            print("------------------------------------------")
        elif tabuleiroFalso[jogadaLinha][jogadaColuna] == 'x' or tabuleiroFalso[jogadaLinha][jogadaColuna] == 'O':
            print("Você já atacou essa posição, escolha outra.")
            print("------------------------------------------")
            imprimirTabuleiro(tabuleiroFalso)
            print("------------------------------------------")
        elif tabuleiroatacado[jogadaLinha][jogadaColuna] == 'x':
            vidaOponente -= 5
            tabuleiroFalso[jogadaLinha][jogadaColuna] = 'x'
            print("------------------------------------------")
            imprimirTabuleiro(tabuleiroFalso)
            print("------------------------------------------")
            print("O jogador afundou uma embarcação!")
            break
        else:
            tabuleiroFalso[jogadaLinha][jogadaColuna] = 'O'
            print("não tem nenhum barco nessa posição :(")
            print("------------------------------------------")
            imprimirTabuleiro(tabuleiroFalso)
            print("------------------------------------------")
            break
    return vidaOponente



# Vidas
vidaJogador = 5
vidaComputador = 5

#Tabuleiros
tabuleiroJogador = criarTabuleiro()
tabuleiroComputador = criarTabuleiro()
tabuleiroFalso = criarTabuleiro() # Tabuleiro só com zeros utilizado para mostrar ao jogador

for i in range(5):
    tabuleiroComputador[i][i] = 'x'

# Jogo

# print("Bem vindo ao jogo 'Batalha Naval'!")
# print()
# posicionarJogador(tabuleiroJogador)
# print()
# print("------------------------------------------")
# print("Agora o Computador escolhe posição!")
# # Computador escolhe a posição
# print("------------------------------------------")
while vidaComputador != 0 or vidaJogador != 0:
    print("Vez do jogador atacar:")
    print("------------------------------------------")
    jogadaJogador(tabuleiroComputador,vidaComputador,tabuleiroFalso)


