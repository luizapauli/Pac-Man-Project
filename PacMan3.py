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
ALTURAJANELA = 680
ICONE = "Recursos/Imagens/icone.png"
MAPA = [
[3,4,4,4,4,4,4,4,4,4,4,4,19,7,7,7,7,7,7,7,7,7,7,7,8],   
[5,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,14],
[6,2,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,2,1,2,1,1,1,2,14],
[6,2,2,2,2,2,1,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,1,2,14],
[6,1,1,1,2,1,1,2,1,2,2,2,1,1,1,2,1,1,1,1,1,2,1,2,14],
[6,2,2,2,2,2,2,2,1,2,1,1,1,2,2,2,1,2,2,2,1,2,2,2,14],
[6,2,1,1,1,1,1,2,1,2,2,2,2,2,1,2,2,2,1,2,1,2,1,2,14],
[6,2,2,2,1,2,2,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,2,2,14],
[6,2,1,2,1,2,1,2,2,2,2,2,2,2,1,2,2,2,2,2,1,2,1,1,14],
[17,2,2,2,1,2,1,1,1,1,2,1,1,1,1,2,1,2,1,1,1,2,2,2,16],
[11,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,1,2,15],
[11,2,2,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,1,2,1,2,15],
[11,1,1,2,1,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,1,2,15],
[11,2,2,2,1,1,2,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,2,2,15],
[11,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,15],
[11,2,2,2,1,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,2,15],
[11,2,1,2,1,2,2,2,2,2,2,1,2,2,1,2,2,2,2,1,2,2,2,2,15],
[11,2,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,2,15],
[11,2,2,2,2,2,2,2,2,2,2,1,2,1,2,2,2,2,2,2,2,2,2,2,15],
[9,12,12,12,12,12,12,12,12,12,12,12,18,13,13,13,13,13,13,13,13,13,13,13,10]
]

MAPA_AUX = [
[3,4,4,4,4,4,4,4,4,4,4,4,19,7,7,7,7,7,7,7,7,7,7,7,8],   
[5,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,1,2,2,2,2,2,14],
[6,2,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,2,1,2,1,1,1,2,14],
[6,2,2,2,2,2,1,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,1,2,14],
[6,1,1,1,2,1,1,2,1,2,2,2,1,1,1,2,1,1,1,1,1,2,1,2,14],
[6,2,2,2,2,2,2,2,1,2,1,1,1,2,2,2,1,2,2,2,1,2,2,2,14],
[6,2,1,1,1,1,1,2,1,2,2,2,2,2,1,2,2,2,1,2,1,2,1,2,14],
[6,2,2,2,1,2,2,2,1,1,2,1,1,2,1,2,1,1,1,2,1,2,2,2,14],
[6,2,1,2,1,2,1,2,2,2,2,2,2,2,1,2,2,2,2,2,1,2,1,1,14],
[17,2,2,2,1,2,1,1,1,1,2,1,1,1,1,2,1,2,1,1,1,2,2,2,16],
[11,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,1,2,15],
[11,2,2,2,1,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1,1,2,1,2,15],
[11,1,1,2,1,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,1,2,15],
[11,2,2,2,1,1,2,1,1,2,1,2,1,1,1,2,1,1,1,1,1,2,2,2,15],
[11,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,15],
[11,2,2,2,1,1,2,1,1,1,1,1,1,2,1,2,1,1,1,1,1,1,1,2,15],
[11,2,1,2,1,2,2,2,2,2,2,1,2,2,1,2,2,2,2,1,2,2,2,2,15],
[11,2,1,2,1,2,1,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,2,15],
[11,2,2,2,2,2,2,2,2,2,2,1,2,1,2,2,2,2,2,2,2,2,2,2,15],
[9,12,12,12,12,12,12,12,12,12,12,12,18,13,13,13,13,13,13,13,13,13,13,13,10]
]

def desenhaMapa(lista_objetos):
    
    for l in range(len(MAPA)):
        for c in range(len(MAPA[l])):
            if MAPA[l][c] == 1:
                desenhaImagem(lista_objetos[0], c*32, l*32)
            elif MAPA[l][c] == 2:
                desenhaImagem(lista_objetos[1], c*32, l*32)
            elif MAPA[l][c] == 3:
                desenhaImagem(lista_objetos[2], c*32, l*32)
            elif MAPA[l][c] == 4:
                desenhaImagem(lista_objetos[3], c*32, l*32)
            elif MAPA[l][c] == 5:
                desenhaImagem(lista_objetos[4], c*32, l*32)
            elif MAPA[l][c] == 6:
                desenhaImagem(lista_objetos[5], c*32, l*32)
            elif MAPA[l][c] == 7:
                desenhaImagem(lista_objetos[6], c*32, l*32)
            elif MAPA[l][c] == 8:
                desenhaImagem(lista_objetos[7], c*32, l*32)
            elif MAPA[l][c] == 9:
                desenhaImagem(lista_objetos[8], c*32, l*32)
            elif MAPA[l][c] == 10:
                desenhaImagem(lista_objetos[9], c*32, l*32)
            elif MAPA[l][c] == 11:
                desenhaImagem(lista_objetos[10], c*32, l*32)
            elif MAPA[l][c] == 12:
                desenhaImagem(lista_objetos[11], c*32, l*32)
            elif MAPA[l][c] == 13:
                desenhaImagem(lista_objetos[12], c*32, l*32)
            elif MAPA[l][c] == 14:
                desenhaImagem(lista_objetos[13], c*32, l*32)
            elif MAPA[l][c] == 15:
                desenhaImagem(lista_objetos[14], c*32, l*32)
            elif MAPA[l][c] == 16:
                desenhaImagem(lista_objetos[15], c*32, l*32)
            elif MAPA[l][c] == 17:
                desenhaImagem(lista_objetos[16], c*32, l*32)
            elif MAPA[l][c] == 18:
                desenhaImagem(lista_objetos[17], c*32, l*32)
            elif MAPA[l][c] == 19:
                desenhaImagem(lista_objetos[18], c*32, l*32)
            elif MAPA[l][c] == 0:
                desenhaImagem(lista_objetos[19], c*32, l*32)
            # n = 1
            # while True:
            #     if MAPA[l][c] == n:
            #         desenhaImagem(lista_objetos[n-1], c*32, l*32)
            #         break
            #     else:
            #         n += 1

    # nº no mapa: objeto -> índice em 'lista_objetos' = (nº no mapa) - 1
    # 0: ----
    # 1: parede
    # 2: pilula
    # 3: quina noroeste
    # 4; parede norte
    # 5: parede oeste 1
    # 6: parede oeste 2
    # 7: parede norte 2
    # 8: quina nordeste
    # 9: quinda sudoeste
    # 10: quina sudeste
    # 11: parede oeste 3
    # 12: parede sul 1
    # 13: parede sul 2
    # 14: parede leste 1
    # 15: parede leste 2
    # 16: portal leste

def carregaSprites(tamIcone: int):
    """
    Carrega os sprites do mapa e dos personagens

    Parâmetro:
        tamIcone: Tamanho padrão dos ícones
    """
    # JOGADOR
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

    # SOMBRAS
    sombra_baixo = [carregaImagem("Recursos/Imagens/sombra_baixo1.png", (tamIcone, tamIcone)),
                     carregaImagem("Recursos/Imagens/sombra_baixo2.png", (tamIcone, tamIcone)),
                     carregaImagem("Recursos/Imagens/sombra_baixo3.png", (tamIcone, tamIcone))]
    sombra_cima = [carregaImagem("Recursos/Imagens/sombra_cima1.png", (tamIcone, tamIcone)),
                    carregaImagem("Recursos/Imagens/sombra_cima2.png", (tamIcone, tamIcone)),
                    carregaImagem("Recursos/Imagens/sombra_cima3.png", (tamIcone, tamIcone))]
    sombra_esquerda = [carregaImagem("Recursos/Imagens/sombra_esquerda1.png", (tamIcone, tamIcone)),
                        carregaImagem("Recursos/Imagens/sombra_esquerda2.png", (tamIcone, tamIcone)),
                        carregaImagem("Recursos/Imagens/sombra_esquerda3.png", (tamIcone, tamIcone))]
    sombra_direita = [carregaImagem("Recursos/Imagens/sombra_direita1.png", (tamIcone, tamIcone)),
                       carregaImagem("Recursos/Imagens/sombra_direita2.png", (tamIcone, tamIcone)),
                       carregaImagem("Recursos/Imagens/sombra_direita3.png", (tamIcone, tamIcone))]
    lista_imagem_sombras = [sombra_cima, sombra_baixo, sombra_esquerda, sombra_direita]

    parede = carregaImagem("Recursos/Imagens/parede.png", (tamIcone, tamIcone))
    pilula = carregaImagem("Recursos/Imagens/pilula2.png", (tamIcone, tamIcone))
    quina_noroeste = carregaImagem("Recursos/Imagens/quina_noroeste2.png", (tamIcone, tamIcone))
    parede_norte1 = carregaImagem("Recursos/Imagens/parede_norte1.png", (tamIcone, tamIcone))
    parede_oeste1 = carregaImagem("Recursos/Imagens/parede_oeste1.png", (tamIcone, tamIcone))
    parede_oeste2 = carregaImagem("Recursos/Imagens/parede_oeste2.png", (tamIcone, tamIcone))
    parede_norte2 = carregaImagem("Recursos/Imagens/parede_norte2.png", (tamIcone, tamIcone))
    quina_nordeste = carregaImagem("Recursos/Imagens/quina_nordeste2.png", (tamIcone, tamIcone))
    quina_sudoeste = carregaImagem("Recursos/Imagens/quina_sudoeste1.png", (tamIcone, tamIcone))
    quina_sudeste = carregaImagem("Recursos/Imagens/quina_sudeste1.png", (tamIcone, tamIcone))
    parede_oeste3 = carregaImagem("Recursos/Imagens/parede_oeste3.png", (tamIcone, tamIcone))
    parede_sul1 = carregaImagem("Recursos/Imagens/parede_sul1.png", (tamIcone, tamIcone))
    parede_sul2 = carregaImagem("Recursos/Imagens/parede_sul2.png", (tamIcone, tamIcone))
    parede_leste1 = carregaImagem("Recursos/Imagens/parede_leste1.png", (tamIcone, tamIcone))
    parede_leste2 = carregaImagem("Recursos/Imagens/parede_leste2.png", (tamIcone, tamIcone))
    portal_leste = carregaImagem("Recursos/Imagens/portal_leste2.png", (tamIcone, tamIcone))
    portal_oeste = carregaImagem("Recursos/Imagens/portal_oeste1.png", (tamIcone, tamIcone))
    portal_sul = carregaImagem("Recursos/Imagens/portal_sul1.png", (tamIcone, tamIcone))
    portal_norte = carregaImagem("Recursos/Imagens/portal_norte1.png", (tamIcone, tamIcone))
    piso = carregaImagem("Recursos/Imagens/piso2.png", (tamIcone, tamIcone))
    lista_objetos = [parede, pilula, quina_noroeste, parede_norte1, parede_oeste1, parede_oeste2, parede_norte2, quina_nordeste, quina_sudoeste, quina_sudeste, parede_oeste3, parede_sul1, parede_sul2, parede_leste1, parede_leste2, portal_leste, portal_oeste, portal_sul, portal_norte, piso]
    return lista_imagem_jogador, lista_objetos, lista_imagem_sombras

def verificaTeclaPressionada(direcaoIntencao):
    """
    Verifica qual tecla foi pressionada pelo jogador.
    
    Parâmetro:
        direcaoIntencao: 
    """
    if teclaPressionada(K_UP):
        direcaoIntencao = "UP"
    elif teclaPressionada(K_DOWN):
        direcaoIntencao = "DOWN"
    elif teclaPressionada(K_LEFT):
        direcaoIntencao = "LEFT"
    elif teclaPressionada(K_RIGHT):
        direcaoIntencao = "RIGHT"
    
    return direcaoIntencao

def telaPontuacao(pilulasColetadas: int):
    """
    Função responsável por desenhar e atualizar a tela de pontuação.

    Parâmetro:
        pilulasColetadas: Quantidade de pílulas coletadas
    """
    pontuacao = carregaImagem("Recursos/Imagens/pontuacao3.png")
    desenhaImagem(pontuacao, 0, 640)
    desenhaTexto(str(pilulasColetadas), 180, 658, 35, "firebrick4") #coral4

def defineImagemJogador(direcaoAtual: str, imagemJogador: int, lista_imagem_jogador: list):
    """
    Define o conjunto de imagens do jogador a ser utilizado de acordo com a direção atual.
    
    Parâmetros:
        direcaoAtual: Direção atual do jogador;
        imagemJogador: Índice correspondente à imagem atual do jogador;
        lista_imagem_jogador: Lista de imagens do jogador.
    Retorno:
        imagemJogador: Índice correspondente à imagem atual do jogador.
    """
    if direcaoAtual == "UP":
        imagemJogador = lista_imagem_jogador[0]
    elif direcaoAtual == "DOWN":
        imagemJogador = lista_imagem_jogador[1]
    elif direcaoAtual == "LEFT":
        imagemJogador = lista_imagem_jogador[2]
    elif direcaoAtual == "RIGHT":
        imagemJogador = lista_imagem_jogador[3]
    else:
        imagemJogador = imagemJogador
    return imagemJogador

def movimentoJogador(direcaoAtual: str, yJogador: int, xJogador: int):
    """
    Função responsável por controlar a movimentação do Jogador.

    Parâmetros:
        direcaoAtual: Direção atual do jogador;
        yJogador: Posição Y do Jogador;
        xJogador: Posição X do Jogador.
    Retorno:
        yJogador: Posição Y do Jogador atualizada;
        xJogador: Posição X do Jogador atualizada.
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

def verificaIntencao(direcaoAtual: str, direcaoIntencao: str, yJogador: int, xJogador: int):
    """
    Controla a mudança entre a intenção de direção e a direção atual.
    Se o caminho estiver livre, a mudança ocorre. (Não é cumulativa)

    Parâmetros:
        direcaoAtual: Direção atual do jogador;
        direcaoIntencao: Intenção de mudança de direção;
        yJogador: Posição Y do Jogador;
        xJogador: Posição X do Jogador;
    Retorno:
        direcaoAtual: Direção atualizada do jogador;
        yJogador: Posição Y do Jogador atualizada;
        xJogador: Posição X do Jogador atualizada.
    """
    # Representação das extremidades da imagem do personagem:
    # A---B
    # |   |
    # C---D
    # As extremidades são utilizadas para definir se a imagem completa do personagem poderá 
    # passar pelo caminho, assim evitando bugs de movimetação

    # Representante no mapa da coordenada X de cada extremidade:
    xA = xC = xJogador//32
    xB = xD = (xJogador + 31)//32
    # Representante no mapa da coordenada Y de cada extremidade:
    yA = yB = yJogador//32
    yC = yD = (yJogador + 31)//32

    # Checa extremidades A e B (o que muda é o Y)
    if direcaoIntencao == "UP":
        if (MAPA[yA-1][xA] == 0 or MAPA[yA-1][xA] == 2) and (MAPA[yB-1][xB] == 0 or MAPA[yB-1][xB] == 2):
            direcaoAtual = direcaoIntencao    
    # Checa extremidades C e D (o que muda é o Y)
    elif direcaoIntencao== "DOWN":
        if (MAPA[yC+1][xC] == 0 or MAPA[yC+1][xC] == 2) and (MAPA[yD+1][xD] == 0 or MAPA[yD+1][xD] == 2):
            direcaoAtual = direcaoIntencao       
    # Checa extremidades A e C (o que muda é o X)      
    elif direcaoIntencao == "LEFT":
        if (MAPA[yA][xA-1] == 0 or MAPA[yA][xA-1] == 2) and (MAPA[yC][xC-1] == 0 or MAPA[yC][xC-1] == 2):
            direcaoAtual = direcaoIntencao
    # Checa extremidades B e D (o que muda é o X) 
    elif direcaoIntencao == "RIGHT":
        if (MAPA[yB][xB+1] == 0 or MAPA[yB][xB+1] == 2) and (MAPA[yD][xD+1] == 0 or MAPA[yD][xD+1] == 2):
            direcaoAtual = direcaoIntencao
        

    return direcaoAtual, yJogador, xJogador

def limitaParede(direcaoAtual: str, yJogador: int, xJogador: int):
    """
    Função responsável por limitar os movimentos do Jogador de acordo com as paredes do mapa.

    Parâmetros:
        direcaoAtual: Direção atual do jogador;
        yJogador: Posição Y do Jogador;
        xJogador: Posição X do Jogador.
    Retorno:
        direcaoAtual: Estado de movimento correspondente à limitação do mapa;
        yJogador: Posição Y do Jogador atualizada;
        xJogador: Posição X do Jogador atualizada.
    """
    c = xJogador//32
    l = yJogador//32
    if direcaoAtual == "UP" and (MAPA[l][c] != 0 and MAPA[l][c] != 2):
        yJogador = 32*(l+1)
        direcaoAtual = "STILL"
    if direcaoAtual == "LEFT" and (MAPA[l][c] != 0 and MAPA[l][c] != 2):
        xJogador = 32*(c+1)
        direcaoAtual = "STILL"
    if direcaoAtual == "DOWN" and (MAPA[l+1][c] != 0 and MAPA[l+1][c] != 2):
        yJogador = 32*l
        direcaoAtual = "STILL"
    if direcaoAtual == "RIGHT" and (MAPA[l][c+1] != 0 and MAPA[l][c+1] != 2):
        xJogador = 32*(c)
        direcaoAtual = "STILL"
        
    return direcaoAtual, yJogador, xJogador

# FUNÇÃO SEM USO -> a ser atualizada
def portal (direcao, tamIcone, yJogador, xJogador):
    if direcao == "LEFT":
        if yJogador == 9*32 and xJogador == 0:
            xJogador = LARGURAJANELA - tamIcone
    else:
        if yJogador == 9*32 and xJogador == (LARGURAJANELA - tamIcone):
            xJogador = 0
    return xJogador

def coletaPilula (direcaoAtual, xJogador, yJogador):
    """
    Função responsável por coletar as pílulas do mapa (atualiza os valores do mapa).

    Parâmetros:
        direcaoAtual: Direção atual do jogador;
        yJogador: Posição Y do Jogador;
        xJogador: Posição X do Jogador.
    """

    xLeft = (xJogador + 16)//32
    xRight = (xJogador - 16)//32
    y = yJogador//32 #Left and Right
    x = xJogador//32 #Up and Down
    yUp = (yJogador + 16)//32
    yDown = (yJogador - 16)//32

    MAPA[yUp][x] = 0 if direcaoAtual == "UP" and MAPA[yUp][x] == 2 else MAPA[yUp][x]
    MAPA[y][xLeft] = 0 if direcaoAtual == "LEFT" and MAPA[y][xLeft] == 2 else MAPA[y][xLeft]
    MAPA[yDown+1][x] = 0 if direcaoAtual == "DOWN" and MAPA[yDown+1][x] == 2 else MAPA[yDown+1][x]
    MAPA[y][xRight+1] = 0 if direcaoAtual == "RIGHT" and MAPA[y][xRight+1] == 2 else MAPA[y][xRight+1]

def contaPilula():
    """
    Função responsável por contar as pílulas coletadas

    Retorno:
        pilulasColetadas: Quantidade de pílulas coletadas até o momento
    """
    pilulasRestantes = 0
    pilulasTotais = 0

    for l in range(len(MAPA)):
        for c in range(len(MAPA[l])):
            if MAPA[l][c] == 2:
                pilulasRestantes += 1

    for l in range(len(MAPA_AUX)):
        for c in range(len(MAPA_AUX[l])):
            if MAPA_AUX[l][c] == 2:
                pilulasTotais += 1
    
    pilulasColetadas = pilulasTotais - pilulasRestantes
                
    return pilulasColetadas

def main():
    """
    Função responsável por unir as outras funções.
    """
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Pac-Man", CORFUNDOJANELA, ICONE)

    lista_imagem_jogador, lista_objetos, lista_imagem_sombras = carregaSprites(32)
    imagemJogador = lista_imagem_jogador[2]
    frameJogador = 0
    velocidadeAnimacaoJogador = 0.12
    direcaoAtual = direcaoIntencao= "STILL"

    xJogador = 400
    yJogador = 320


    while True:      
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

    # >>>> JOGADOR <<<<
        
        direcaoIntencao = verificaTeclaPressionada(direcaoIntencao)
            
        # Verifica a intenção de movimento
        direcaoAtual, yJogador, xJogador = verificaIntencao(direcaoAtual, direcaoIntencao, yJogador, xJogador)
        
        # Atualiza a imagem do jogador
        imagemJogador = defineImagemJogador(direcaoAtual, imagemJogador, lista_imagem_jogador)

        # Atualiza a posição do jogador
        yJogador, xJogador = movimentoJogador(direcaoAtual, yJogador, xJogador)

        # Atualiza o mapa ao coletar as pílulas
        coletaPilula (direcaoAtual, xJogador, yJogador)
        pilulasColetadas = contaPilula()
        # print(pilulasColetadas)
        
        direcaoAtual, yJogador, xJogador = limitaParede(direcaoAtual, yJogador, xJogador)


        #Desenha o mapa
        desenhaMapa(lista_objetos)

        telaPontuacao(pilulasColetadas)

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