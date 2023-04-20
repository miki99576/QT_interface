import PySimpleGUI as sg
import os.path
import csv
import time
import pandas as pd

from Student_menu_official import Student_menu
from Scripts_page import script_window
from create_test import create_test
from functions import table
from functions import display_image
from functions import show_graph
from functions import append_csv
from functions import read_csv
from functions import getlines
from functions import search
from functions import display_csv


#append new line to a csv file

qt = [
	 [sg.Image('/home/qtrobot/catkin_ws/src/Interface_official_build-20230412T073658Z-001/Interface_official_build/QT.png',size = (250,200))]
]
main_menu = [
	[sg.Button("Script",key="script",),sg.Button("Create a test",key="-TEST-",),sg.Button("Class List",key="-CLASS LIST-",),]
]
# ----- Full layout -----
layout = [
    [sg.Frame('QT Main Menu', main_menu, font='Arial 14 bold', title_color='black',background_color='#DAE0E6')],[qt]
]



window = sg.Window("Main Menu Window", layout,background_color='#DAE0E6')
# Run the Event Loop
while True:

    event, values = window.read()
    
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event=="script":
        script_window()
    if event == "-CLASS LIST-":
        Student_menu()
    if event == "-TEST-":
    	create_test()
