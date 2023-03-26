from functions import table
from functions import display_image
from functions import show_graph
from functions import append_csv
from functions import read_csv
from functions import getlines
from functions import search
from functions import display_csv
from functions import create_student


import PySimpleGUI as sg
import os.path
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as psg
import shutil

file_csv = './Student_Notes/Student_List.csv'


def add_student_page():
	form = [
	[sg.Text("First Name",key="-FIRST NAME-",font='Helvitica 12 bold underline'),sg.InputText(key="-FIRST INPUT-",size=(10,1))],
	[sg.Text("Last Name",key="-LAST NAME-",font='Helvitica 12 bold underline'),sg.InputText(key="-LAST INPUT-",size=(10,1))],
	[sg.Text("Student NUMBER",key="-NUMBER-",font='Helvitica 12 bold underline'),sg.InputText(key="-STUDENT NUMBER-",size=(10,1))],
	[sg.Text("Select Image",font='Helvitica 12 bold underline',),sg.In(size=(25, 1), enable_events=True, key="-IMAGE-"),sg.FileBrowse(file_types=(("Png Files","*.png"),)),],
	[sg.Button('Save',key="-SAVE-",font='bold')]


	]

	layout = [
    [
         [sg.Frame('Add a Student', form, font='Arial 14 bold', title_color='black')],
	]
	]
	window = sg.Window("Config Window", layout,)

	while True:
		event, values = window.read()
		if event == "Exit" or event == sg.WIN_CLOSED:
			break

		if event == "-SAVE-":
			first_name = values["-FIRST INPUT-"]
			last_name = values["-LAST INPUT-"]
			student_number = values["-STUDENT NUMBER-"]
			full_name = str(first_name)+"_"+str(last_name)
			print(str(first_name)+"_"+str(last_name))
			append_csv(file_csv,full_name,str(student_number))
			print(values["-IMAGE-"])
			create_student(full_name,"./Student_Notes/","Date","Emotion_Reading","Gesture_Imitation","Simple_Questions",str(values["-IMAGE-"]))


	window.close()   

