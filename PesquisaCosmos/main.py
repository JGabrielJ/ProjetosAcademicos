# Importação de Bibliotecas
import pygame
from math import sqrt
from time import sleep
import PySimpleGUI as sg
from emoji import emojize


# Criação de Funções
def linha(nl):
    print('-'*nl)


# Tocando o som dos Padrinhos Mágicos
def tocar_som():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('song.mp3')
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.event.wait(1)


# Janela da Pesquisa
def janela_pesquisa():
    # Definindo o tema de cor da interface
    sg.theme('DarkPurple6')

    # Criando o layout da interface
    design = [
        [sg.Text(emojize(':sparkles:'*20), pad=(92.5,0), text_color='#12b520')],
        [sg.Text('Seja bem-vindo(a) à pesquisa da Equipe Cosmo!', pad=(132.5,0), text_color='#12b520')],
        [sg.Text(emojize(':sparkles:'*20), pad=(92.5,0), text_color='#12b520')],
        [sg.HorizontalSeparator(color='#12b520')],
        [sg.Text('Qual é o seu nome?'), sg.Input(text_color='#fff', size=(50,0), key='username')],
        [sg.Text('Você possui plano de saúde?'), sg.Radio('Sim', 'planosaude', text_color='#fff'), sg.Radio('Não', 'planosaude', text_color='#fff')],
        [sg.Text('Já utilizou o sistema de saúde pública?'), sg.Radio('Sim', 'planosaudeuso', text_color='#fff'), sg.Radio('Não', 'planosaudeuso', text_color='#fff')],
        [sg.Text('Por quanto tempo você usou esse sistema?'), sg.Combo(['Pouquíssimo Tempo', 'Pouco Tempo', 'Tempo Intermediário', 'Muito Tempo', 'Tempo Indefinido'], text_color='#fff', size=(25,0))],
        [sg.HorizontalSeparator(color='#12b520')],
        [sg.Text('Já tentou adquirir algum medicamento pelo sistema de saúde pública?'), sg.Radio('Sim', 'adqrmedic', text_color='#fff'), sg.Radio('Não', 'adqrmedic', text_color='#fff')],
        [sg.Text('Se sim, qual foi a facilidade de obtê-lo?'), sg.Combo(['Muito Fácil', 'Fácil', 'Médio', 'Difícil', 'Muito Difícil'], size=(25,0), text_color='#fff')],
        [sg.Text('Qual foi a velocidade da obtenção deste medicamento?'), sg.Combo(['Muito Rápido', 'Rápido', 'Mediano', 'Demorado', 'Bastante Demorado'], size=(20,0), text_color='#fff')],
        [sg.HorizontalSeparator(color='#12b520')],
        [sg.Text('Como você avalia a qualidade das consultas, sendo 0 (horrível) e 10 (perfeito)?'), sg.OptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,0), text_color='#fff')],
        [sg.Text('Qual nota você dá à velocidade de atendimento do sistema de saúde pública?'), sg.OptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,0), text_color='#fff')],
        [sg.Text('De modo geral, qual nota você daria ao sistema de saúde pública?'), sg.OptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff')],
        [sg.Button('Enviar Dados', pad=(95,0)), sg.Output(size=(37,0), background_color='#070739', text_color='#12b520')]
    ]

    # Fazendo a janela aparecer
    return sg.Window('Pesquisa sobre Saúde Pública', icon='icon.ico', layout=design, finalize=True)


# Janela dos Administradores
def janela_admin():
    # Definindo o tema de cor da interface
    sg.theme('DarkPurple6')

    # Criando o layout da interface
    design = [
        [sg.Text(emojize(':sparkles:'*20), pad=(142.5,0), text_color='#12b520')],
        [sg.Text('Insira os dados fornecidos pelos usuários aqui!', pad=(182.5,0), text_color='#12b520')],
        [sg.Text(emojize(':sparkles:'*20), pad=(142.5,0), text_color='#12b520')],
        [sg.HorizontalSeparator(color='#12b520')],
        [sg.Text('Nota 1:    '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota1'), sg.Text('Nota 2:    '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota2'), sg.Text('Nota 3:    '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota3'), sg.Text('Nota 4:   '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota4')],
        [sg.Text('Nota 5:    '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota5'), sg.Text('Nota 6:    '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota6'), sg.Text('Nota 7:    '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota7'), sg.Text('Nota 8:   '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota8')],
        [sg.Text('Nota 9:    '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota9'), sg.Text('Nota 10:  '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota10'), sg.Text('Nota 11:  '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota11'), sg.Text('Nota 12:  '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota12')],
        [sg.Text('Nota 13:  '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota13'), sg.Text('Nota 14:  '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota14'), sg.Text('Nota 15:  '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota15'), sg.Text('Nota 16:  '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota16')],
        [sg.Text('Nota 17:  '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota17'), sg.Text('Nota 18:  '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota18'), sg.Text('Nota 19:  '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota19'), sg.Text('Nota 20:  '), sg.InputOptionMenu([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(5,1), text_color='#fff', key='nota20')],
        [sg.Button('Analisar Dados', pad=(62.5,0)), sg.Output(size=(56,10), background_color='#4d4d4d', text_color='#00bed4')]
    ]

    # Fazendo a janela aparecer
    return sg.Window('Pesquisa sobre Saúde Pública', icon='icon.ico', layout=design, finalize=True)


# Janelas Iniciais
janela0, janela1 = janela_pesquisa(), None

# Leitura de Eventos
while True:
    # Definindo variáveis para as janelas, os eventos e os valores
    janela, evento, valor = sg.read_all_windows()

    # Quando a janela for fechada
    if (janela == janela0 or janela == janela1) and evento == sg.WIN_CLOSED:
        break

    # Para enviar os dados inseridos na pesquisa
    if janela == janela0 and evento == 'Enviar Dados':
        # Para ir à próxima janela
        if valor['username'] == 'equipecosmo12345': # type: ignore
            janela1 = janela_admin()
            janela0.hide()
        # Para finalizar o programa
        else:
            tocar_som()
            print('Agradecemos a sua atenção e colaboração!\nFechando o programa...')
            sleep(1.5)
            break

    # Para exibir os resultados
    if janela == janela1 and evento == 'Analisar Dados':
        # Inserindo as notas em uma lista e convertendo todos os valores para inteiro
        notas = [int(valor['nota1']), int(valor['nota2']), int(valor['nota3']), int(valor['nota4']), # type: ignore
        int(valor['nota5']), int(valor['nota6']), int(valor['nota7']), int(valor['nota8']), # type: ignore
        int(valor['nota9']), int(valor['nota10']), int(valor['nota11']), int(valor['nota12']), # type: ignore
        int(valor['nota13']), int(valor['nota14']), int(valor['nota15']), int(valor['nota16']), # type: ignore
        int(valor['nota17']), int(valor['nota18']), int(valor['nota19']), int(valor['nota20'])] # type: ignore
        # notas = [3, 8, 6, 2, 7, 10, 8, 5, 7, 4, 2, 6, 5, 5, 6, 7, 6, 5, 5, 7]

        # Exibindo os resultados
        print(f'As notas dadas à velocidade de atendimento do Sistema de Saúde Pública Brasileiro foram:\n{notas}')
        linha(98)

        # Calculando o mínimo, o máximo, a média aritmética e a ordem crescente da lista das notas
        minimo = min(notas)
        maximo = max(notas)
        media = sum(notas) / len(notas)
        notas.sort()

        sleep(1)
        print(f'A menor nota dada foi {minimo}\nA maior nota dada foi {maximo}\nA média aritmética das notas é {media:.2f}')
        print(f'A lista com as notas em ordem crescente é:\n{notas}')
        linha(98)

        # Analisando a distribuição de frequência das notas
        sleep(1)
        for n in range(0, 11):
            if notas.count(n) > 0:
                print(f'A nota {n} aparece {notas.count(n)} vez(es)')
        print('As demais notas apareceram 0 vezes')
        linha(98)

        # Calculando a amplitude, a variância e o desvio-padrão da lista das notas
        amplitude = notas[len(notas) - 1] - notas[0]
        sqroot = 0
        for v in range(0, len(notas)):
            sqroot = sqroot + (notas[v] - media) ** 2
        variancia = sqroot / (len(notas) - 1)
        desvio_padrao = sqrt(variancia)

        sleep(1)
        print(f'A amplitude da lista é {amplitude:.2f}\nA variância da lista é {variancia:.2f}\nO desvio-padrão da lista é {desvio_padrao:.2f}')
        linha(98)
