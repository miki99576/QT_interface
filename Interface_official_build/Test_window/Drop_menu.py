"""

import PySimpleGUI as psg
names = []
lst = psg.Combo(names, font=('Arial Bold', 14),  expand_x=True, enable_events=True,  readonly=False, key='-COMBO-')
layout = [[lst,
   psg.Button('Add', ),
   psg.Button('Remove'),
   psg.Button('Exit')],
   [psg.Text("", key='-MSG-',
      font=('Arial Bold', 14),
      justification='center')]
   ]
window = psg.Window('Combobox Example', layout, size=(715, 200))
while True:
   event, values = window.read()
   print(event, values)
   if event in (psg.WIN_CLOSED, 'Exit'):
      break
   if event == 'Add':
      names.append(values['-COMBO-'])
      print(names)
      window['-COMBO-'].update(values=names, value=values['-COMBO-'])
      msg = "A new item added : {}".format(values['-COMBO-'])
      window['-MSG-'].update(msg)
   if event == '-COMBO-':
      ch = psg.popup_yes_no("Do you want to Continue?", title="YesNo")
   if ch == 'Yes':
      val = values['-COMBO-']
      names.remove(val)
   window['-COMBO-'].update(values=names, value=' ')
   msg = "A new item removed : {}".format(val)
   window['-MSG-'].update(msg)
window.close()
"""
import PySimpleGUI as psg
names = ['Hello','thank you']
lst = psg.Listbox(names, size=(20, 4), font=('Arial Bold', 14), expand_y=True, enable_events=True, select_mode='multiple',key='-LIST-')
layout = [[psg.Input(size=(20, 1), font=('Arial Bold', 14), expand_x=True, key='-INPUT-'),
   psg.Button('Add'),
   psg.Button('Remove'),
   psg.Button('Exit')],
   [lst],
   [psg.Text("", key='-MSG-', font=('Arial Bold', 14), justification='center')]
]
window = psg.Window('Listbox Example', layout, size=(600, 200))
while True:
   event, values = window.read()
   print(event, values)
   if event in (psg.WIN_CLOSED, 'Exit'):
      break
   if event == 'Add':
      names.append(values['-INPUT-'])
      window['-LIST-'].update(names)
      msg = "A new item added : {}".format(values['-INPUT-'])
      window['-MSG-'].update(msg)
   if event == 'Remove':
      val = lst.get()[0]
      names.remove(val)
      window['-LIST-'].update(names)
      msg = "A new item removed : {}".format(val)
      window['-MSG-'].update(msg)
window.close()