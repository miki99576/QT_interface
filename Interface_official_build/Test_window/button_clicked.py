"""
this code demonstrates how when a button is clicked, it stays clicked, its used for when selecting an answer for a simple question
"""
import PySimpleGUI as psg
import time
layout = [
   [psg.Button('Test'),psg.Button('test1')],
]
window = psg.Window('Progress Bar', layout,)
while True:
   event, values = window.read()
   print(event, values)
   if event == 'Test' or event =='test1':
      window['Test'].update(disabled=True)
      window['test1'].update(disabled=True)
      
   if event == 'Cancel':
      window['-PBAR-'].update(max=100)
   if event == psg.WIN_CLOSED or event == 'Exit':
      break
window.close()