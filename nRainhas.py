def criar_tabuleiro(n):
    return [["_" for _ in range(n)] for _ in range(n)]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("  ".join(linha))
    print()

def verifica_rainha(tabuleiro, linha, coluna, n):
    for i in range(linha):
        if tabuleiro[i][coluna] == "Q":
            return False

    for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == "Q":
            return False

    for i, j in zip(range(linha, -1, -1), range(coluna, n)):
        if tabuleiro[i][j] == "Q":
            return False

    return True

def resolver_n_rainhas(tabuleiro, linha, n):
    if linha >= n:
        return True  # fim

    for coluna in range(n):
        if verifica_rainha(tabuleiro, linha, coluna, n):
            tabuleiro[linha][coluna] = "Q" 
            if resolver_n_rainhas(tabuleiro, linha + 1, n):
                return True
            tabuleiro[linha][coluna] = "_" #se a proxima linha não existe posição verificavel -> faz backtrack

    return False

def n_rainhas(n):
    tabuleiro = criar_tabuleiro(n)
    if resolver_n_rainhas(tabuleiro, 0, n):
        imprimir_tabuleiro(tabuleiro)
    else:
        print("Não há solução para", n, "rainhas.")

# Exemplo de uso
n = 8
n_rainhas(n)