import random
# Funções

# Função para criar as matrizes do tabuleiro
def criarTabuleiro():
    matriz = []
    for i in range(5):
        linhas = []
        for j in range(10):
            linhas.append('0')
        matriz.append(linhas)
    return matriz

# Função que imprime o tabuleiro bonitinho
def imprimirTabuleiro(tabuleiro):
    contador = 1
    print("    1.   2.   3.   4.   5.   6.   7.   8.   9.   10. ")
    for linha in tabuleiro:
        print(f"{contador}.{linha}")
        contador += 1


# Função criada para o jogador posicionar seus barcos
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

# Função que realiza a jogada de um jogador
def jogadaJogador(tabuleiroatacado,vidaOponente,tabuleiroFalso):
    while True:
        print("Faça sua jogada!")
        jogadaLinha = int(input("Escolha a linha (1 - 5): ")) - 1
        jogadaColuna = int(input("Escolha a Coluna (1 - 10): ")) - 1
        if jogadaLinha < 0 or jogadaLinha > 4 or jogadaColuna < 0 or jogadaColuna > 9:
            print("Digite uma posição válida!")
            print("------------------------------------------")
            print("tabuleiro inimigo:")
            imprimirTabuleiro(tabuleiroFalso)
            print("------------------------------------------")
        elif tabuleiroFalso[jogadaLinha][jogadaColuna] == 'x' or tabuleiroFalso[jogadaLinha][jogadaColuna] == 'O':
            print("Você já atacou essa posição, escolha outra.")
            print("------------------------------------------")
            print("tabuleiro inimigo:")
            imprimirTabuleiro(tabuleiroFalso)
            print("------------------------------------------")
        elif tabuleiroatacado[jogadaLinha][jogadaColuna] == 'x':
            vidaOponente -= 1
            tabuleiroFalso[jogadaLinha][jogadaColuna] = 'x'
            print("------------------------------------------")
            print("tabuleiro inimigo:")
            imprimirTabuleiro(tabuleiroFalso)
            print("------------------------------------------")
            print("O jogador afundou uma embarcação!")
            break
        else:
            tabuleiroFalso[jogadaLinha][jogadaColuna] = 'O'
            print("não tem nenhum barco nessa posição :(")
            print("------------------------------------------")
            print("tabuleiro inimigo:")
            imprimirTabuleiro(tabuleiroFalso)
            print("------------------------------------------")
            break
    return vidaOponente

# Função que realiza a jogada do Computador
def jogadaComputador(tabuleiroJogador, vidaJogador, tabuleiroFalso):
    while True:
        linhaComputador = random.randint(0, 4)
        colunaComputador = random.randint(0,9)
        if tabuleiroJogador[linhaComputador][colunaComputador] == 'x':
            tabuleiroFalso[linhaComputador][colunaComputador] = 'x'
            vidaJogador -= 1
            print(f"computador escolheu a linha {linhaComputador + 1}")
            print(f"computador escolheu a coluna {colunaComputador + 1}")
            print("computador acertou!")
            print("------------------------------------------")
            print("tabuleiro do Jogador:")
            imprimirTabuleiro(tabuleiroFalso)
            break
        elif tabuleiroJogador[linhaComputador][colunaComputador] == '0':
            tabuleiroFalso[linhaComputador][colunaComputador] = 'O'
            print(f"computador escolheu a linha {linhaComputador + 1}")
            print(f"computador escolheu a coluna {colunaComputador + 1}")
            print("computador errou!")
            print("------------------------------------------")
            print("tabuleiro do Jogador:")
            imprimirTabuleiro(tabuleiroFalso)
            break
        else:
            vidaJogador += 0
    return vidaJogador

# Função para o computador posicionar os barcos aleatoriamente
def colocarbarcoaleatorio(tabuleiro, numbarcos):
    barcoscolocados = 0
    while barcoscolocados < numbarcos:
        linha = random.randint(0, 5 - 1)
        coluna = random.randint(0, 10 - 1)
        if tabuleiro[linha][coluna] == '0':
            tabuleiro[linha][coluna] = 'x'
            barcoscolocados += 1

# Vidas
vidaJogador = 5
vidaComputador = 5

#Tabuleiros
tabuleiroJogador = criarTabuleiro()
tabuleiroComputador = criarTabuleiro()
computadorFalso = criarTabuleiro() # Tabuleiro só com zeros utilizado para mostrar ao jogador
jogadorFalso = criarTabuleiro()

# Jogo
print("Bem vindo ao jogo 'Batalha Naval'!")
print()
imprimirTabuleiro(jogadorFalso)
print()
posicionarJogador(tabuleiroJogador)
print()
print("------------------------------------------")
print("Agora o Computador escolhe posição!")
colocarbarcoaleatorio(tabuleiroComputador,5)
print("Computador escolheu as posições!")
print("------------------------------------------")
while True:
    print("Vez do jogador atacar:")
    print("------------------------------------------")
    vidaComputador = jogadaJogador(tabuleiroComputador,vidaComputador,computadorFalso)
    if vidaComputador == 0: # Verifica se o jogador venceu
        print("Você venceu! afundou todos os barcos do computador")
        print("tabuleiro final do Computador: ")
        imprimirTabuleiro(computadorFalso)
        print("------------------------------------------")
        print(f"barcos restantes: {vidaComputador}")
        print()
        print()
        print("Seu tabuleiro: ")
        imprimirTabuleiro(jogadorFalso)
        print("------------------------------------------")
        print(f"barcos restantes: {vidaJogador}")
        print("------------------------------------------")
        print("Obrigado por Jogar! O Alisson e o Enzo agradecem :)")
        break
    print("Vez do Computador atacar:")
    print("------------------------------------------")
    vidaJogador = jogadaComputador(tabuleiroJogador,vidaJogador,jogadorFalso)
    if vidaJogador == 0: # Verifica se o computador venceu.
        print("Você perdeu :(, o computador afundou todos os seus barcos.")
        print("------------------------------------------")
        print("tabuleiro final do Computador: ")
        imprimirTabuleiro(computadorFalso)
        print("------------------------------------------")
        print(f"barcos restantes: {vidaComputador}")
        print()
        print()
        print("Seu tabuleiro: ")
        imprimirTabuleiro(jogadorFalso)
        print("------------------------------------------")
        print(f"barcos restantes: {vidaJogador}")
        print("------------------------------------------")
        print("Obrigado por Jogar! O Alisson e o Enzo agradecem :)")
        break