# this code is to create a log window instead of the subbar

import PySimpleGUI as sg
import os.path
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as psg

layout = [
        [sg.Multiline(size=(30,5), font='courier 10', background_color='black', text_color='white', key='-MLINE-')],
        [sg.T('Promt> '), sg.Input(key='-IN-', focus=True, do_not_clear=False)],
        [sg.Button('Run', bind_return_key=True), sg.Button('Exit')]]

window = sg.Window('Realtime Shell Command Output', layout)

while True:  # Event Loop
        event, values = window.read()
        # print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Run':
        	for i in range(10):
        		#command = values["-IN-"]
        		#print(command)
        		window['-MLINE-'].update("command"+ '\n',append=True,autoscroll=True)
        		time.sleep(3)
        		window.refresh()
window.close()
