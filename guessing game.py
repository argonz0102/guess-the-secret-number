import PySimpleGUI as sg
from random import randint

def create_window():

    sg.theme('Black')
    layout = [
        [(sg.Text('Guess The Number 1-20', font = 'Calibri 20'))],
        [sg.VPush()],
        [],
        [sg.Input('', key = 'Skriv'), sg.Button('Enter')],
        [sg.VPush()],
        [sg.Text('', key = 'Output', font = 'Calibri 20')],
        [sg.VPush()],
        [sg.Button('Reset')]


    ]

    return sg.Window('Guess game',layout, size = (500,400), element_justification = 'center')


window = create_window()

active = False
nr = randint(1, 20)

while True:
    event, values = window.read(timeout = 10)
    if event in (sg.WIN_CLOSED, '-Close-'):
        break

    if event == 'Enter':
        input_value = int(values['Skriv'])
        if input_value == nr:
            window['Output'].update('Correct')
        if input_value < nr:
            window['Output'].update('bigger')
        if input_value > nr:
            window['Output'].update('Smaller')


    if event == 'Reset':
        window.close()
        window = create_window()
        nr = randint(1, 20)

window.close()