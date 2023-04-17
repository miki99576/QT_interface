import PySimpleGUI as sg
import os.path
import csv
import time
import pandas as pd
import os
import time
import PySimpleGUI as psg



#importing functions
from functions import read_csv
from functions import getlines
from functions import generate_buttons
from Emo_Recog import emotion_recognition
from Simple_questions import simpleQuestions
from functions import simple_search
from functions import gesture_conversion

#Defining the path for questions and student's lists
student_csv_path = "/home/qtrobot/catkin_ws/src/Interface_official_build-20230412T073658Z-001/Interface_official_build/Student_Notes/Student_List.csv"
gesture_questions_csv = "/home/qtrobot/catkin_ws/src/Interface_official_build-20230412T073658Z-001/Interface_official_build/Questions/gesture_questions.csv"
emotion_imitation_csv = "/home/qtrobot/catkin_ws/src/Interface_official_build-20230412T073658Z-001/Interface_official_build/Questions/emotion_questions.csv"
simple_questions_csv= "/home/qtrobot/catkin_ws/src/Interface_official_build-20230412T073658Z-001/Interface_official_build/Questions/Simple_Questions.csv"



# the goal of this script is to generate n number of true,false buttons based on the number of items chosen in a listbox element, then we need to get the values of those buttons chosen

"""
in the current version when Start button is clicked, the first element of the questions_list will be shown (four buttons, true,false,repeat,Play), from there we get the value of the button 
play for a question if play button is clicked in question[j], the buttons associated with buttons question[j+1] will be shown.

Repeat button (if clicked the the we will replay the question)

"""




#------Defining the functions------

def question(question):
    time.sleep(6)
    print(question)



#------Defining the functions------        


def create_test():

#------List that uses the function read_csv to contain all the values of student names------
    student_names = [read_csv(student_csv_path,"Full_Name")[i] for i in range(getlines(student_csv_path))]
    student_list = [[psg.Combo(student_names, font=('Arial Bold', 14),  expand_x=True, enable_events=True,  readonly=False, key='-COMBO-'),sg.Text("Please select a student")]]
#------List that uses the function read_csv to contain all the values of student names------


#------Gesture Frame------

#first we create an element which contains the listbox , then we create a frame element that sorrounds it --> we need to create two variables
    gesture_tab = [[sg.T('Gesture Imitations')],
               [sg.Listbox(values=[read_csv(gesture_questions_csv,"Name",)[i] for i in range(getlines(gesture_questions_csv))], enable_events=True, size=(40, 10),select_mode='multiple' ,key="-GESTURE LIST-"),]]

#------Gesture Frame------


#------emotion Frame------

#first we create an element which contains the listbox , then we create a frame element that sorrounds it --> we need to create two variables

    emotion_tab = [[sg.T('Emotion Imitations')],
                [sg.Listbox(values=[read_csv(emotion_imitation_csv,"Question")[i] for i in range(getlines(emotion_imitation_csv))], enable_events=True, size=(40, 10),select_mode='multiple' ,key="-EMOTION LIST-"),],
                ]
#------emotion Frame------

#------Simple Questions Frame------

#first we create an element which contains the listbox , then we create a frame element that sorrounds it --> we need to create two variables

    question_tab= [[sg.T('Simple Questions')],
                [sg.Listbox(values=[read_csv(simple_questions_csv,"Question")[i] for i in range(getlines(simple_questions_csv))], enable_events=True, size=(40, 10),select_mode='multiple' ,key="-QUESTION LIST-"),],
                ]
#------Simple Questions Frame------


#------Log window------
    log_window =  [sg.Multiline(size=(30,5), font='courier 10', background_color='black', text_color='white', key='-MLINE-')]
#------Log window------


    layout = [[student_list],
        [sg.TabGroup([[sg.Tab('emotion imitations', emotion_tab), sg.Tab('Gesture imitations', gesture_tab),sg.Tab('Simple_Questions', question_tab)]])],
        [sg.Column(generate_buttons("i",False)[3],key="-ROW_PANEL-")],
        [sg.Button('Start Test',key="-START-")]
        ]


    window = sg.Window("Config Window", layout,)

    #-----------------------
    j = 0
    Score = 0
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break    
        #update image if student name is chosen

    #if event == "-EMOTION LIST-":
        emotion_val = values["-EMOTION LIST-"]
        #print(str(emotion_val))
        gesture_val = values["-GESTURE LIST-"]
    #print(str(gesture_val))
        question_val = values["-QUESTION LIST-"]
        
    #print(str(question_val))
        if event== "-START-":
            window["-START-"].update(disabled=True)
           
            if len(emotion_val) != 0:
                emotion_recognition(simple_search(emotion_imitation_csv,emotion_val))

            if len(question_val) != 0:
                simpleQuestions(simple_search(simple_questions_csv,question_val))


            # Part for Gesture Imitation
            window.extend_layout(window['-ROW_PANEL-'],generate_buttons(gesture_val[0],True)[3])
            #question(generate_buttons[0])
        
        if len(gesture_val) != 0:
            gesture_val1 = gesture_conversion(gesture_questions_csv,gesture_val)
            if event == generate_buttons(gesture_val[j],True,)[5]:
                if j != len(gesture_val)-1:
                    print(generate_buttons(gesture_val[j+1],True,)[5])
                    window.extend_layout(window['-ROW_PANEL-'],generate_buttons(gesture_val[j+1],True)[3])
                    j+=1
                    #question(gesture_val[j])
                    os.system("roslaunch gesture_imitation gesture_imitation.launch gesture:="+gesture_val1[j])

            if event == generate_buttons(gesture_val[j],True,)[4]:
                #question(gesture_val[j])
                os.system("roslaunch gesture_imitation gesture_imitation.launch gesture:="+gesture_val1[j])


# the next event is to test if we could get the values of all the true buttons pushed, we did the same loop as above but instead of outputting the question, we output the key from the true buttons
# if the button is clicked it becomes unclickable
        for i in range(len(gesture_val)):
            if event== generate_buttons(gesture_val[i],True)[1]:
                window[generate_buttons(gesture_val[i],True)[1]].update(disabled=True,button_color = ('black','yellow'))
                window[generate_buttons(gesture_val[i],True)[2]].update(disabled=True)
                Score=Score+1
        
            if event== generate_buttons(gesture_val[i],True)[2]:
                window[generate_buttons(gesture_val[i],True)[1]].update(disabled=True)
                window[generate_buttons(gesture_val[i],True)[2]].update(disabled=True,button_color = ('black','yellow'))
            

    window.close()


create_test()