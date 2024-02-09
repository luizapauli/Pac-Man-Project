######################################################
# Introdução a Programação (2023/2)
# EP2 - PacMan
# Integrante 1: Luiza Paulid e Castro
# Integrante 2: Paulo José Campos Barbosa
# Integrante 3: 
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

def limitaParede(tecla, yPacman, xPacman):
    """
    Função responsável por limitar os movimentos do Pacman de acordo com as paredes do mapa

    Parâmetros:
        yPacman: Posição Y do Pacman
        xPacman: Posição X do Pacman 
    Retorno:
        yPacman: Posição Y do Pacman
        xPacman: Posição X do Pacman
    """
    c = xPacman//32
    l = yPacman//32
    if tecla == "up":
        if MAPA[l][c] == 1:
            yPacman = 32*(l+1)
            #direcao = "STILL"
    if tecla == "left":
        if MAPA[l][c] == 1:
            xPacman = 32*(c+1)
            #direcao = "STILL"
    if tecla == "down":
        if MAPA[l+1][c] == 1:
            yPacman = 32*l
            #direcao = "STILL"
    if tecla == "right":
        if MAPA[l][c+1] == 1:
            xPacman = 32*(c)
            #direcao = "STILL"

    return yPacman, xPacman

def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Pac-Man", CORFUNDOJANELA, ICONE)

    # jogador_baixo = [carregaImagem("Recursos/Imagens/jogador_baixo1.png", (32, 32)),
    #                  carregaImagem("Recursos/Imagens/jogador_baixo2.png", (32, 32)),
    #                  carregaImagem("Recursos/Imagens/jogador_baixo3.png", (32, 32))]
    # jogador_cima = [carregaImagem("Recursos/Imagens/jogador_cima1.png", (32, 32)),
    #                 carregaImagem("Recursos/Imagens/jogador_cima2.png", (32, 32)),
    #                 carregaImagem("Recursos/Imagens/jogador_cima3.png", (32, 32))]
    # jogador_esquerda = [carregaImagem("Recursos/Imagens/jogador_esquerda1.png", (32, 32)),
    #                     carregaImagem("Recursos/Imagens/jogador_esquerda2.png", (32, 32)),
    #                     carregaImagem("Recursos/Imagens/jogador_esquerda3.png", (32, 32))]
    # jogador_direita = [carregaImagem("Recursos/Imagens/jogador_direita1.png", (32, 32)),
    #                    carregaImagem("Recursos/Imagens/jogador_direita2.png", (32, 32)),
    #                    carregaImagem("Recursos/Imagens/jogador_direita3.png", (32, 32))]
    # imagemJogador = jogador_baixo
    # frameJogador = 0

    # velocidadeAnimacaoJogador = 0.2
    #direcao = PARADO

    parede = carregaImagem("Recursos/Imagens/parede.png", (32, 32))
    pilula = carregaImagem("Recursos/Imagens/pilula.png", (32, 32))
    xIcone = 32
    yIcone = 32
    pacman = carregaImagem("Recursos/Imagens/pacman.png", (xIcone, yIcone))
    xPacman = 400
    yPacman = 320
    while True:      
        
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Verifica se uma das teclas foi precionada
        #Se sim, atualiza a posição do Pacman
        if teclaPressionada(K_UP):
            #direcao = CIMA
            #imagemJogador = jogador_cima
            yPacman -= 2
            yPacman = 0 if yPacman < 0 else yPacman
            yPacman, xPacman = limitaParede("up", yPacman, xPacman)
        elif teclaPressionada(K_DOWN):
            #direcao = BAIXO
           # imagemJogador = jogador_baixo
            yPacman += 2
            yPacman = (ALTURAJANELA - yIcone) if yPacman > (ALTURAJANELA - yIcone) else yPacman
            yPacman, xPacman = limitaParede("down", yPacman, xPacman)
        elif teclaPressionada(K_LEFT):
            #direcao = ESQUERDA
            #imagemJogador = jogador_esquerda
            xPacman -= 2
            xPacman = 0 if xPacman < 0 else xPacman
            if yPacman == 9*32 and xPacman == 0:
                xPacman = LARGURAJANELA - xIcone
            else:
                yPacman, xPacman = limitaParede("left", yPacman, xPacman)
        elif teclaPressionada(K_RIGHT):
            #direcao = DIREITA
            #imagemJogador = jogador_direita
            xPacman += 2
            xPacman = (LARGURAJANELA - xIcone) if xPacman > (LARGURAJANELA - xIcone) else xPacman
            if yPacman == 9*32 and xPacman == (LARGURAJANELA - xIcone):
                xPacman = 0
            else:
                yPacman, xPacman = limitaParede("right", yPacman, xPacman) 

        #Desenha o mapa
        desenhaMapa(parede, pilula)

        #Desenha o Pacman
        desenhaImagem(pacman, xPacman, yPacman)

       # movimentacao()


        #Atualiza os objetos na janela
        atualizaTelaJogo()

        
    finalizaJogo()

main()
