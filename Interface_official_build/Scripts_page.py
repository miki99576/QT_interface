import PySimpleGUI as sg
import os.path
import csv
import time
import pandas as pd


from functions import table
from functions import display_image
from functions import show_graph
from functions import append_csv
from functions import read_csv
from functions import getlines
from functions import search
from functions import display_csv


def script_window():
	file_list_column = [
	    [
	        sg.Text("Search File"),
	        sg.In(size=(25, 1), enable_events=True, key="-FILE-"),
	        sg.FileBrowse(key="-IN-",file_types=(("Python Files","*.py"),)),
	    ],
	    [
	        sg.Listbox(
	            values=[read_csv("rep.csv","name")[i] for i in range(getlines("rep.csv"))], enable_events=True, size=(40, 20), key="-FILE LIST-"
	        )
	    ],
	]

# For now will only show the name of the file that was chosen
	image_viewer_column = [
	    [sg.Text("File location")],
	    [sg.Text(size=(200, 1), key="-TOUT-")],
	    [sg.In(size=(200, 1), enable_events=True, key="-REP-")],
	    [sg.Button("change repositry","-CHANGE-")],
	    [sg.Image(key="-IMAGE-")],
	]

# ----- Full layout -----
	layout = [
	    [
	        sg.Column(file_list_column),
	        sg.VSeperator(),
	        sg.Column(image_viewer_column),
	    ]
	]

	window = sg.Window("Scripts Window", layout,size=(900,200))
	# Run the Event Loop
	while True:

	    event, values = window.read()
	    
	    if event == "Exit" or event == sg.WIN_CLOSED:
	        break
	        
	    # Folder name was filled in, make a list of files in the folde
	    if event == "-FILE-":
	        file_list = []
	        file = values["-FILE-"]
	        basename = os.path.basename(file)
	        #file_list.append(file)
	        append_csv('rep.csv',basename,file)
	        #window["-FILE LIST-"].update(file_list)    
	    if event == "-FILE LIST-":
	        print(values["-FILE LIST-"])
	        window["-TOUT-"].update(search("rep.csv","name",values["-FILE LIST-"][0],"repositry"))
	        window["-REP-"].update(search("rep.csv","name",values["-FILE LIST-"][0],"repositry"))
	        #window["-IMAGE-"].update(filename=filename)  
	   

	window.close()



