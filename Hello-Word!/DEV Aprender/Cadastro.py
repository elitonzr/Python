# -*- coding: utf-8 -*-
# Como Criar Uma Tela Em Python c/ PySimpleGUI [Fácil] - https://youtu.be/UnfmxnFpfdM

from PySimpleGUI import PySimpleGUI as sg

tentativa = 0

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# Janelas
janela = sg.Window('Tela de Login', layout)
# Ler Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        print('Fim!')
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'elitonz' and valores['senha'] == '123456':
            print('Bem-vindo')
        else:
            tentativa += 1
            print(tentativa)
            print('Usuário ou senha Incorreto!')
            if tentativa == 3:
                break
