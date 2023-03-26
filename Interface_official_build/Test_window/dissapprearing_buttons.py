# this code is to create a function that create a number of buttons (hidden by default,number is specifice by user).
import PySimpleGUI as sg
import os.path
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as psg






"""
layout=[[sg.Button("Hello",key="-HOME-")]]

window = sg.Window("Main Menu Window", layout,background_color='#DAE0E6')
# Run the Event Loop
while True:

    event, values = window.read()
    
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event=="Hello":
    	layout.append([sg.Button("Nice Job")])
    	print(layout)
    	window.extend_layout(window["-HOME-"])
"""        