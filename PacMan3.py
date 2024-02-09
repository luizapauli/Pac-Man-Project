######################################################
# Introdução a Programação (2023/2)
# EP2 - PacMan
# Integrante 1: Luiza Pauli de Castro
# Integrante 2: 
# Integrante 3: 
######################################################


#ATENÇÃO: você não pode importar o módulo PyGame neste arquivo. 
#Consequentemente, você não pode usar o métodos do módulo.
#Você pode, se precisar, importar o módulo math e/ou random.
from BaseParaJogo import *
import math as m

CORFUNDOJANELA = (222, 212, 161)
LARGURAJANELA = 800
ALTURAJANELA = 640
ICONE = "Recursos/Imagens/icone.png"

MAPA = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],   
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,1,1,1,2,1,1,2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,2,1],
[1,2,2,2,2,2,1,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,1,2,1],
[1,2,1,1,1,2,1,2,1,2,2,2,1,1,1,2,1,1,1,1,1,2,1,2,1],
[1,2,2,2,2,2,2,2,1,2,1,1,1,2,2,2,1,2,2,2,1,2,2,2,1],
[1,2,1,1,1,1,1,2,1,2,2,2,2,2,1,2,2,2,1,2,1,2,1,2,1],
[1,2,2,2,1,2,2,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,2,2,1],
[1,2,1,2,1,2,1,2,2,2,2,2,2,2,1,2,2,2,2,2,1,2,1,1,1],
[2,2,2,2,1,2,1,1,1,1,2,1,1,1,1,2,1,2,1,1,1,2,2,2,2],
[1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,1,2,1],
[1,2,2,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,1,2,1,2,1],
[1,1,1,2,1,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,1,2,1],
[1,2,2,2,1,1,2,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,2,2,1],
[1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1],
[1,2,2,2,1,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,2,1],
[1,2,1,2,1,2,2,2,2,2,1,2,2,2,1,2,2,2,2,1,2,2,2,2,1],
[1,2,1,2,1,2,1,1,1,2,1,2,1,1,1,1,1,1,2,1,2,1,1,2,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

def desenhaMapa(parede, pilula):
    for l in range(len(MAPA)):
        for c in range(len(MAPA[l])):
            if MAPA[l][c] == 1:
                desenhaImagem(parede, c*32, l*32)
            elif MAPA[l][c] == 2:
                desenhaImagem(pilula, c*32, l*32)

def movimentoJogador(direcaoAtual, yJogador, xJogador):
    """
    Função responsável por controlar a movimentação do Jogador.

    Parâmetros:
        direcao: Direção correspondente a tecla pressionada
        yJogador: Posição Y do Jogador
        xJogador: Posição X do Jogador
    """
    if direcaoAtual == "UP":
        yJogador -= 2
    elif direcaoAtual == "DOWN":
        yJogador += 2
    elif direcaoAtual == "LEFT":
        xJogador -= 2
    elif direcaoAtual == "RIGHT":
        xJogador += 2
    else:
        direcaoAtual = "STILL"

    return yJogador, xJogador

def limitaParede(direcaoAtual, direcaoIntencao, yJogador, xJogador, lista_imagem_jogador):
    """
    Função responsável por limitar os movimentos do Pacman de acordo com as paredes do mapa

    Parâmetros:
        direcao: Direção correspondente a tecla pressionada
        yPacman: Posição Y do Pacman
        xPacman: Posição X do Pacman 
    Retorno:
        direcao: Direção correspondente à limitação do mapa
        yPacman: Posição Y do Pacman
        xPacman: Posição X do Pacman
    """
    # Representação das extremidades da imagem do personagem
    # A---B
    # |   |
    # C---D

    c = xJogador//32
    l = yJogador//32
    # Checa estremidades A e B respectivamente
    if direcaoIntencao == "UP":
        if MAPA[l][c] != 1 and MAPA[l][c+1] != 1:
            direcaoAtual = direcaoIntencao
        else:
            if direcaoAtual == direcaoIntencao:
                yJogador = 32*(l+1)
                direcaoAtual = "STILL"  
    # Checa estremidades C e D respectivamente
    elif direcaoIntencao== "DOWN":
        if MAPA[l+1][c] != 1 and MAPA[l+1][c+1] != 1:
            direcaoAtual = direcaoIntencao
        else:
            if direcaoAtual == direcaoIntencao:
                yJogador = 32*l
                direcaoAtual = "STILL"
    # Checa estremidades B e C respectivamente         
    elif direcaoIntencao == "LEFT":
        if MAPA[l][c+1] != 1 and MAPA[l+1][c] != 1:
            direcaoAtual = direcaoIntencao
        else:
            if direcaoAtual == direcaoIntencao:
                xJogador = 32*(c+1)
                direcaoAtual = "STILL"
    # Checa estremidades A e C respectivamente
    elif direcaoIntencao == "RIGHT":
        if MAPA[l][c] != 1 and MAPA[l+1][c] != 1:
            direcaoAtual = direcaoIntencao
        else:
            if direcaoAtual == direcaoIntencao:
                xJogador = 32*(c)
                direcaoAtual = "STILL"

    return direcaoAtual, yJogador, xJogador

def portal (direcao, tamIcone, yJogador, xJogador):
    if direcao == "LEFT":
        if yJogador == 9*32 and xJogador == 0:
            xJogador = LARGURAJANELA - tamIcone
    else:
        if yJogador == 9*32 and xJogador == (LARGURAJANELA - tamIcone):
            xJogador = 0
    return xJogador

def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Pac-Man", CORFUNDOJANELA, ICONE)

    tamIcone = 32
    jogador_baixo = [carregaImagem("Recursos/Imagens/jogador_baixo1.png", (tamIcone, tamIcone)),
                     carregaImagem("Recursos/Imagens/jogador_baixo2.png", (tamIcone, tamIcone)),
                     carregaImagem("Recursos/Imagens/jogador_baixo3.png", (tamIcone, tamIcone))]
    jogador_cima = [carregaImagem("Recursos/Imagens/jogador_cima1.png", (tamIcone, tamIcone)),
                    carregaImagem("Recursos/Imagens/jogador_cima2.png", (tamIcone, tamIcone)),
                    carregaImagem("Recursos/Imagens/jogador_cima3.png", (tamIcone, tamIcone))]
    jogador_esquerda = [carregaImagem("Recursos/Imagens/jogador_esquerda1.png", (tamIcone, tamIcone)),
                        carregaImagem("Recursos/Imagens/jogador_esquerda2.png", (tamIcone, tamIcone)),
                        carregaImagem("Recursos/Imagens/jogador_esquerda3.png", (tamIcone, tamIcone))]
    jogador_direita = [carregaImagem("Recursos/Imagens/jogador_direita1.png", (tamIcone, tamIcone)),
                       carregaImagem("Recursos/Imagens/jogador_direita2.png", (tamIcone, tamIcone)),
                       carregaImagem("Recursos/Imagens/jogador_direita3.png", (tamIcone, tamIcone))]
    lista_imagem_jogador = [jogador_cima, jogador_baixo, jogador_esquerda, jogador_direita]
    imagemJogador = jogador_esquerda
    frameJogador = 0
    velocidadeAnimacaoJogador = 0.12
    direcaoAtual = direcaoIntencao= "STILL"

    xJogador = 400
    yJogador = 320
    parede = carregaImagem("Recursos/Imagens/parede.png", (tamIcone, tamIcone))
    pilula = carregaImagem("Recursos/Imagens/pilula.png", (tamIcone, tamIcone))
    

    while True:      
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Verifica se uma das teclas foi precionada
        #Se sim, atualiza a inteção de movimento do Pacman
        if teclaPressionada(K_UP):
            direcaoIntencao = "UP"
        elif teclaPressionada(K_DOWN):
            direcaoIntencao = "DOWN"
        elif teclaPressionada(K_LEFT):
            direcaoIntencao = "LEFT"
        elif teclaPressionada(K_RIGHT):
            direcaoIntencao = "RIGHT"

        #Se a direção atual do jogador for igual a intenção, a função limitaParede fará 
        # direcaoAtual = "STILL", para parar o personagem quando bater em uma parede 
        direcaoAtual, yJogador, xJogador = limitaParede(direcaoAtual, direcaoIntencao, yJogador, xJogador)
        yJogador, xJogador = movimentoJogador(direcaoAtual, yJogador, xJogador)
        #Desenha o mapa
        desenhaMapa(parede, pilula)

        # Desenha o jogador
        if direcaoAtual != "STILL":
            frameJogador += velocidadeAnimacaoJogador
            if frameJogador >= 3:
                frameJogador = 0
            desenhaImagem(imagemJogador[int(frameJogador)], xJogador, yJogador)
        else:
            desenhaImagem(imagemJogador[0], xJogador, yJogador)

        #Atualiza os objetos na janela
        atualizaTelaJogo()

        
    finalizaJogo()

main()