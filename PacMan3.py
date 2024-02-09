######################################################
# Introdução a Programação (2023/2)
# EP2 - PacMan
# Integrante 1: Luiza Pauli de Castro
# Integrante 2: Paulo José Campos Barbosa
# Integrante 3: Poliana
# Integrante 4: 
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
[1,1,1,2,1,1,1,2,1,2,2,2,2,2,1,2,2,2,1,2,1,2,1,1,1],
[0,0,1,2,1,2,2,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,1,0,0],
[1,1,1,2,1,2,1,2,2,2,2,2,2,2,1,2,2,2,2,2,1,2,1,1,1],
[2,2,2,2,1,2,1,1,1,1,2,1,1,1,1,2,1,2,1,1,1,2,2,2,2],
[1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,1,1,1],
[0,0,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,1,2,1,0,0],
[1,1,1,2,1,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,1,1,1],
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

def movimento(direcao, tamIcone, yJogador, xJogador):
    """
    Função responsável por controlar a movimentação do Jogador.

    Parâmetros:
        direcao: Direção correspondente a tecla pressionada
        tamIcone: Tamanho do ícone do jogador
        yJogador: Posição Y do Jogador
        xJogador: Posição X do Jogador
    """
    if direcao == "UP":
        yJogador -= 2
        # direcao, yJogador, xJogador = limitaParede("UP", yJogador, xJogador)
    elif direcao == "DOWN":
        yJogador += 2
        # direcao, yJogador, xJogador = limitaParede("DOWN", yJogador, xJogador)
    elif direcao == "LEFT":
        xJogador -= 2
    #     if yJogador == 9*32 and xJogador == 0:
    #         xJogador = LARGURAJANELA - tamIcone
    #     else:
    #         direcao, yJogador, xJogador = limitaParede("LEFT", yJogador, xJogador)
    elif direcao == "RIGHT":
        xJogador += 2
        # if yJogador == 9*32 and xJogador == (LARGURAJANELA - tamIcone):
        #     xJogador = 0
        # else:
        #     direcao, yJogador, xJogador = limitaParede("RIGHT", yJogador, xJogador) 
    else:
        direcao = "STILL"

    return yJogador, xJogador

def limitaParede(direcao, yJogador, xJogador):
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
    c = xJogador//32
    l = yJogador//32
    # c = int(m.ceil(c)) if yJogador%32 != 0 else int(m.floor(c))
    # l = int(m.ceil(l)) if xJogador%32 != 0 else int(m.floor(l))
    if direcao == "UP":
        if MAPA[l][c] == 1:
            yJogador = 32*(l+1)
            direcao = "STILL"
    if direcao == "LEFT":
        if MAPA[l][c] == 1:
            xJogador = 32*(c+1)
            direcao = "STILL"
    if direcao == "DOWN":
        if MAPA[l+1][c] == 1:
            yJogador = 32*l
            direcao = "STILL"
    if direcao == "RIGHT":
        if MAPA[l][c+1] == 1:
            xJogador = 32*(c)
            direcao = "STILL"

    return direcao, yJogador, xJogador

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

    jogador_baixo = [carregaImagem("Recursos/Imagens/jogador_baixo1.png", (32, 32)),
                     carregaImagem("Recursos/Imagens/jogador_baixo2.png", (32, 32)),
                     carregaImagem("Recursos/Imagens/jogador_baixo3.png", (32, 32))]
    jogador_cima = [carregaImagem("Recursos/Imagens/jogador_cima1.png", (32, 32)),
                    carregaImagem("Recursos/Imagens/jogador_cima2.png", (32, 32)),
                    carregaImagem("Recursos/Imagens/jogador_cima3.png", (32, 32))]
    jogador_esquerda = [carregaImagem("Recursos/Imagens/jogador_esquerda1.png", (32, 32)),
                        carregaImagem("Recursos/Imagens/jogador_esquerda2.png", (32, 32)),
                        carregaImagem("Recursos/Imagens/jogador_esquerda3.png", (32, 32))]
    jogador_direita = [carregaImagem("Recursos/Imagens/jogador_direita1.png", (32, 32)),
                       carregaImagem("Recursos/Imagens/jogador_direita2.png", (32, 32)),
                       carregaImagem("Recursos/Imagens/jogador_direita3.png", (32, 32))]
    imagemJogador = jogador_esquerda
    frameJogador = 0

    velocidadeAnimacaoJogador = 0.12
    direcao = "STILL"

    parede = carregaImagem("Recursos/Imagens/parede.png", (32, 32))
    pilula = carregaImagem("Recursos/Imagens/pilula.png", (32, 32))
    tamIcone = 32
    # pacman = carregaImagem("Recursos/Imagens/pacman.png", (tamIcone, tamIcone))
    xJogador = 400
    yJogador = 320

    while True:      
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Verifica se uma das teclas foi precionada
        #Se sim, atualiza a posição do Pacman
        if teclaPressionada(K_UP):
            direcao = "UP"
            imagemJogador = jogador_cima
        elif teclaPressionada(K_DOWN):
            direcao = "DOWN"
            imagemJogador = jogador_baixo
        elif teclaPressionada(K_LEFT):
            direcao = "LEFT"
            imagemJogador = jogador_esquerda
        elif teclaPressionada(K_RIGHT):
            direcao = "RIGHT"
            imagemJogador = jogador_direita

        yJogador, xJogador = movimento(direcao, tamIcone, yJogador, xJogador)
        if direcao == "UP" or direcao == "DOWN":
            direcao, yJogador, xJogador = limitaParede(direcao, yJogador, xJogador)
        else:
            xJogador = portal(direcao, tamIcone, yJogador, xJogador)
            direcao, yJogador, xJogador = limitaParede(direcao, yJogador, xJogador)

        #Desenha o mapa
        desenhaMapa(parede, pilula)

        #Desenha o Pacman
        # desenhaImagem(pacman, xJogador, yJogador)

        # Desenha o jogador
        if direcao != "STILL":
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