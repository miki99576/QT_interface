# importing functions from functions.py
from functions import table
from functions import display_image
from functions import show_graph
from functions import append_csv
from functions import read_csv
from functions import getlines
from functions import search
from functions import display_csv
from Add_student import add_student_page


# importing modules
import PySimpleGUI as sg
import os.path
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as psg




#Defining Variables
file_csv = './Student_Notes/Student_List.csv' # contains path torwards list of students
parent_directory = './Student_Notes' #path torwards the directory where the list of students,student directories are kept



# defining the first column of the config window, this column contains the list of students
"""
explanation how do we call values inside listbox:
	functions used:
		read_csv : which reads a csv file by taking the file name and column name as inputs and outputs the valus of a single column
		getlines : which reads a csv file by taking the file name and uses the panda module to output the entire table, the difference with read_csv is that getlines outputs entire table (easier with panda)

	How it works:
		we used a for loop ; for i in range of getlines(file_csv) [contains all the data of the csv file thanks to panda], we output only the Full_Name column thanks to read_csv
"""


def Student_menu():
    file_list_column = [
    [
        sg.Text("Add a Student"),
        sg.Button("ADD",key="-ADD STUDENT-",), 
    ],
    [sg.Button("Refresh",key="-REFRESH-")],
    [
        sg.Listbox(
            values=[read_csv(file_csv,"Full_Name")[i] for i in range(getlines(file_csv))], enable_events=True, size=(40,20), key="-STUDENT LIST-"
        )
    ],
                       ]
    """
# this is the second column, the layout is as follows : 
    1. first we display an image of the student  : sg.Image(key="-STUDENT IMAGE-")
    2. for each of the three tests we have : 
        a. text highlighting the title of the section
        b. an image of the figure made using the notes on that particular test  (done using show_graph() to create the graph and display_image() to show the graph)
        c. a table containing the values of the student on that particular test.
"""                   
    image_viewer_column = [
        [sg.Image(key="-STUDENT IMAGE-",size = (50,50))],

    # Emotion reading section
        [sg.Text("Emotion Reading",key="-EMOTION_READING-",font='Helvitica 18 bold underline')],
        [sg.Image(key="-EMOTION FIGURE IMAGE-")],
        [psg.Table(values="", headings=['Date','Emotion_Reading'],
        auto_size_columns=True,
        display_row_numbers=False,
        justification='center', key='-EMOTION TABLE-',
        selected_row_colors='red on yellow',
        enable_events=True,
        expand_x=True,
        expand_y=True)],

    # simple questions section
        [sg.Text("Simple Questions",key="simple_questions",font='Helvitica 18 bold underline')],
        [sg.Image(key="-SIMPLE FIGURE IMAGE-")],
        [psg.Table(values="", headings=['Date','Simple_Questions'],
        auto_size_columns=True,
        display_row_numbers=False,
        justification='center', key='-SIMPLE TABLE-',
        selected_row_colors='red on yellow',
        enable_events=True,
        expand_x=True,
        expand_y=True)],

    # gesture imitation section
        [sg.Text("Gesture Imitation",key="gesture_imitations",font='Helvitica 18 bold underline')],
        [sg.Image(key="-GESTURE FIGURE IMAGE-")],
        [psg.Table(values="", headings=['Date','Gesture_Imitation'],
        auto_size_columns=True,
        display_row_numbers=False,
        justification='center', key='-GESTURE TABLE-',
        selected_row_colors='red on yellow',
        enable_events=True,
        expand_x=True,
        expand_y=True)]
                            ]


    # ----- Full layout -----
    layout = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(image_viewer_column,scrollable=True,size=(1000,500),key="-COL-"),
        ]
            ]
    window = sg.Window("Config Window", layout,)

    #-----------------------

    while True:
        event, values = window.read()
    
        if event == "Exit" or event == sg.WIN_CLOSED:
            break    
        #update image if student name is chosen
        if event=="-STUDENT LIST-":
            file = values["-STUDENT LIST-"]
            print(str(file[0]))
        #display_image('./Student_Notes',file)
        #display_image('./Student_Notes','John wayne','figure')

        # Displaying student image
            window["-STUDENT IMAGE-"].update(filename=display_image(parent_directory,str(file[0]),'photo'))


        # Show_graph creates the graph for the three test
            show_graph(display_csv(parent_directory,str(file[0])),'Date','Emotion_Reading','Emotion_Reading',parent_directory,str(file[0]))
            show_graph(display_csv(parent_directory,str(file[0])),'Date','Gesture_Imitation','Gesture_Imitation',parent_directory,str(file[0]))
            show_graph(display_csv(parent_directory,str(file[0])),'Date','Simple_Questions','Simple_Questions',parent_directory,str(file[0]))

                
        # Displaying the figures
            window["-EMOTION FIGURE IMAGE-"].update(filename=display_image(parent_directory,str(file[0]),"Emotion_Reading_figure"))
            window["-GESTURE FIGURE IMAGE-"].update(filename=display_image(parent_directory,str(file[0]),"Gesture_Imitation_figure"))
            window["-SIMPLE FIGURE IMAGE-"].update(filename=display_image(parent_directory,str(file[0]),"Simple_Questions_figure"))
            window.refresh()
            window["-COL-"].contents_changed()
            window['-EMOTION TABLE-'].update(values=table(['Date','Emotion_Reading'],display_csv(parent_directory,str(file[0]))))
        if event =="-ADD STUDENT-":
            add_student_page()

        if event =="-REFRESH-":
            window["-STUDENT LIST-"].update(values=[read_csv(file_csv,"Full_Name")[i] for i in range(getlines(file_csv))])

    window.close()




Student_menu()