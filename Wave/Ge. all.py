import pyautogui
import time
import PySimpleGUI as sg
import datetime as dt

# Trava de Dt limite (DIA ATUAL)

data = dt.date.today()

dia = data.day
mes = data.month
ano = data.year


def acessar_wms():
    pyautogui.PAUSE = 1

    pyautogui.hotkey('win', 'd')  # AREA DE TRABALHO
    pyautogui.click(x=689, y=381)  # CLICAR NO MEIO DA DESKTOP
    pyautogui.click(x=710, y=750)  # CLICAR NA BARRA DE APLICATIVOS ABERTOS SEMPRE DEIXAR O WMS 5°
    pyautogui.click(x=986, y=21)  # MAXIZIMAR WMS

    # Acessando WMS

    pyautogui.write('igor.menino')  # LOGIN
    pyautogui.press('tab')  # PASSAR PARA SENHA
    pyautogui.write('Veh12062016#')  # SENHA
    pyautogui.click(x=422, y=438)  # ACESSO

    # AVISO PARA O GESTOR RESPOSAVEL FICAR SABENDO

    pyautogui.alert('Iniciando processo de geração, favor não utilizar o computador')


def gerar_imprimir():
    for i in range(300):
        time.sleep(120)  # Quanto tempo vai gerar medido em segundos

        # MARGEM DE SEGURANÇA NÃO REMOVER

        pyautogui.hotkey('win', 'd')  # AREA DE TRABALHO
        pyautogui.click(x=689, y=381)  # CLICAR NO MEIO DA DESKTOP
        pyautogui.click(x=710, y=750)  # CLICAR NA BARRA DE APLICATIVOS ABERTOS SEMPRE DEIXAR O WMS 5°

        # MARGEM DE SEGURANÇA NÃO REMOVER

        # MENU WMS

        pyautogui.click(x=13, y=202)  # Clicar em COLETA E EXPEDIÇÃO
        pyautogui.click(x=32, y=243)  # Clicar em COLETA
        pyautogui.click(x=91, y=265)  # Clicar em PROGRAMA+ONDA
        pyautogui.press('enter')  # Clicar ENTER para abrir PROGRAMA+ONDA
        time.sleep(1)

        # PROGRAMA+ONDA

        pyautogui.write('CAJA2')  # Inserir PLANTA
        pyautogui.press('tab')
        pyautogui.write('Wave 4.0')  # Inserir NOME DO PROGRAMA
        pyautogui.press('tab')
        pyautogui.click(x=879, y=132)  # Removendo flegue de DT MINIMA EXPEDIÇÃO
        pyautogui.press('tab')

        #PROGRAMADO
        pyautogui.click(x=453, y=422)  # Clicar em PROGRAMA
        pyautogui.press('enter')

        #ONDA
        pyautogui.click(x=786, y=425)  # Clicar em ONDA
        pyautogui.press('enter')

        #COPIANDO ENTREGA
        pyautogui.doubleClick(x=510, y=454)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1.5)

        # MENU WMS 2

        pyautogui.click(x=15, y=157)
        pyautogui.click(x=97, y=222)
        pyautogui.press('enter')
        time.sleep(1)

        # PICKING + COURIER SEM AUTOMAÇÃO

        pyautogui.write('CAJA2')
        pyautogui.press('tab')
        pyautogui.doubleClick(x=688, y=125)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.click(x=904, y=149)
        pyautogui.press('enter')
        pyautogui.doubleClick(x=688, y=125)
        pyautogui.press('backspace')
        pyautogui.click(x=874, y=217)
        pyautogui.click(x=876, y=299)
        pyautogui.press('enter')

        time.sleep(1)

        # Fechando programas

        pyautogui.click(x=961, y=88)  # fechando tela de impressão
        pyautogui.click(x=1103, y=91)  # fechando tela de geração
        pyautogui.click(x=16, y=155)  # diminuindo lista de etiquetas
        pyautogui.click(x=34, y=241)  # diminuindo lista coleta
        pyautogui.click(x=15, y=202)  # diminuindo lista COLETA E EXPEDIÇÃO

    # Fechando WMS

def fechar_wms():
    pyautogui.click(x=1339, y=8)  # Clicar no X
    pyautogui.click(x=712, y=457)  # Clicar sim
    pyautogui.hotkey('win', 'd')  # AREA DE TRABALHO
    pyautogui.alert('Fim de turno, bom descanso')


# Layout

sg.theme('Dark')  # Tema da Janela

layout = [
    [sg.Text('Usuario: '), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha: '), sg.Input(key='senha', password_char=' ', size=(21, 1))],
    [sg.Button('Entrar')]
]

# Janela

Janela = sg.Window('Wave 4.0', layout)

# ler os eventos

while True:
    eventos, valores = Janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'Entrar':
        if valores['usuario'] == 'cajamar' and valores['senha'] == 'caja2':
            Janela.close()

            acessar = acessar_wms()
            gerar = gerar_imprimir()
            fechar = fechar_wms()
            break