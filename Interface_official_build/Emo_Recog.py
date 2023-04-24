# the function emotion_recognition takes in a list of lists as input, the first element of the list is always the question while the rest are all possible answers
# 



#!/usr/bin/env python
import sys
import csv
import PySimpleGUI as sg
import os.path
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as psg
import shutil

import rospy
from qt_robot_interface.srv import *
from qt_vosk_app.srv import *

from functions import simple_search

# this function shows faces
def emotion(emo):
        faces_list = ["angry","happy","neutral","afraid","sad","disgusted"]
        emotionShow = rospy.ServiceProxy('/qt_robot/emotion/show', emotion_show)
        emotionShow("QT/"+emo)


#questions=["angry","happy","sad"]

#simple_search("emotion_recog_sample.csv",questions)

#print(search("Simple_questions_sample.csv","Questions","What's is your name","Answers"))    



def emotion_recognition(questions):

    rospy.loginfo("Simple questions launched, waiting for the services to initialized!")
    
    # define the ros service
    speechSay = rospy.ServiceProxy('/qt_robot/speech/say', speech_say)
    recognize = rospy.ServiceProxy('/qt_robot/speech/recognize', speech_recognize)

    # block/wait for ros service
    rospy.wait_for_service('/qt_robot/speech/say')
    rospy.wait_for_service('/qt_robot/speech/recognize')
    rospy.loginfo("Services initiated")
    
                  
    try:

        # call a ros service with text message
        rospy.loginfo("Explaining rules !")
        speechSay("Je vais te montrer des emotion et tu dois les identifier.")
        score = 0
        interaction = 0
        for i in range(len(questions)):
            question = questions[i][0]
            answers = []
            for j in range(1, len(questions[i])):
                answers.append(questions[i][j])

            rospy.loginfo("Reading emotion: %s", question)
            rospy.loginfo("Possible answers: %s", answers)
            emotion(question)
            resp = recognize("fr_FR", [], 10)
            rospy.loginfo("Words found: %s", resp.transcript)
            
            
            if any(answer in resp.transcript for answer in answers):
                speechSay("Super c'est la bonne réponse")
                rospy.loginfo("Acceptable answer")
                score += 1
                interaction += 1


            elif not resp.transcript:
                speechSay("Je n'ai pas bien entendu ta réponse.")
                rospy.loginfo("No answer detected")
                i = i-1
                
            else:
                #speechSay("Merci pour ta réponse.")
                rospy.loginfo("Answer is not right")
                interaction += 1

        rospy.loginfo("End of the exercise")
        speechSay("Fin de l'exercice, merci pour tes réponses !")
        if interaction == 0:
            finalScore = 0
        else:
            finalScore = str(int(score/interaction*100))
        rospy.loginfo("The answers are %s pourcent right !", finalScore)
    except KeyboardInterrupt:
        pass
    
    return finalScore

