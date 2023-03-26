# the goal of this script is to generate n number of true,false buttons based on the number of items chosen in a listbox element, then we need to get the values of those buttons chosen

import PySimpleGUI as sg
import os.path
import csv
import time
import pandas as pd
import os
import time
import PySimpleGUI as psg

#------Defining the paths to csv files------

student_csv_path = "./Student_List.csv"
gesture_questions_csv = "./Questions/gesture_questions.csv"
emotion_imitation_csv = "./Questions/emotion_questions.csv"
simple_questions_csv= "./Questions/Simple_Questions.csv"

#------Defining the paths to csv files------


#------Defining the functions------

#the function generate button takes a question as input and generate a pair of true and false buttons, it returns : the question asked, the keys to the true & false buttons of that particular question 
# the main objective of this function is to generate a pair of buttons for every value chosen of simple questions.
def generate_buttons(question,state):
    true_key = "-TRUE"+question+"-"
    false_key = "-FALSE"+question+"-"
    row = [[sg.Text(question,key=question,visible=state),sg.Button("True",key=true_key,visible=state),sg.Button("False",key=false_key,visible=state)]]
    return [question,true_key,false_key,row]

def read_csv(file_name,col_name):
    file_list = []
    with open(file_name, encoding="utf8") as f:
        csv_reader = csv.DictReader(f,delimiter='/')
        for line in csv_reader:
            file_list.append(line[col_name])

        for i in file_list:    
            #window[key].update(file_list)
            return file_list
            #print(line[col_name])
# First the window layout in 2 columns

def getlines(file_name):
    with open(file_name, encoding="utf8") as f:
        results = pd.read_csv(f)
        return len(results)


#------Defining the functions------        




#------Simple Questions Frame-----
question_elements = [
					[sg.Text("Please select one or more question")],
					[sg.Listbox(values=[read_csv(simple_questions_csv,"Question",)[i] for i in range(getlines(simple_questions_csv))], enable_events=True, size=(40, 10),select_mode='multiple' ,key="-QUESTION LIST-"),],
					]
#question_frame = [[sg.Frame('Simple Questions', question_elements, font='Arial 14 bold', title_color='white')],]
#------Simple Questions Frame-----

tab1_layout =  [[sg.T('Emotion imitations')]]

tab2_layout = [[sg.T('Gesture imitations')],
               [sg.Listbox(values=[read_csv(simple_questions_csv,"Question",)[i] for i in range(getlines(simple_questions_csv))], enable_events=True, size=(40, 10),select_mode='multiple' ,key="-QUESTION LIST-"),]]

tab3_layout = [[sg.T('Simple_Questions')],
               [sg.In(key='n')]]

"""                             
layout = [[sg.TabGroup([[sg.Tab('imitations', tab1_layout), sg.Tab('Gesture imitations', tab2_layout),sg.Tab('Simple_Questions', tab3_layout)]])],
              [sg.Button('Read',key="-BUTTON-")]]
print(layout)
"""

# in the initial layout, we define a column containing a button using the generate buttons function, but we set the visibilty to false
layout=[
        [sg.Column(generate_buttons("i",False)[3],key="-ROW_PANEL-")],
        [sg.Button('Read',key="-BUTTON-")]
        ]
window = sg.Window("Config Window", layout,)

    #-----------------------


score=0
# in the first condition : we set it that if we press the button read, it will generate All the questions from Simple_questions csv file
# first we get the range of the data using getlines function, then we get the values of all the questions column using read_csv function and we put that data into generate_buttons function to generate the buttons
while True:
    event,values= window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
            break  
    if event== "-BUTTON-":
        window["-BUTTON-"].update(disabled=True)
        for i in range(getlines(simple_questions_csv)):
            window.extend_layout(window['-ROW_PANEL-'],generate_buttons(read_csv(simple_questions_csv,"Question")[i],True)[3])

            
# the next event is to test if we could get the values of all the true buttons pushed, we did the same loop as above but instead of outputting the question, we output the key from the true buttons
# if the button is clicked it becomes unclickable
    for i in range(getlines(simple_questions_csv)):
        if event== generate_buttons(read_csv(simple_questions_csv,"Question")[i],True)[1]:
            window[generate_buttons(read_csv(simple_questions_csv,"Question")[i],True)[1]].update(disabled=True,button_color = ('black','yellow'))
            window[generate_buttons(read_csv(simple_questions_csv,"Question")[i],True)[2]].update(disabled=True)
        
        if event== generate_buttons(read_csv(simple_questions_csv,"Question")[i],True)[2]:
            window[generate_buttons(read_csv(simple_questions_csv,"Question")[i],True)[1]].update(disabled=True)
            window[generate_buttons(read_csv(simple_questions_csv,"Question")[i],True)[2]].update(disabled=True,button_color = ('black','yellow'))

    

        

window.close()
