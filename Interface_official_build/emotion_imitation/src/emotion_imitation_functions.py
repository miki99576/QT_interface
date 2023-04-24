#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String
from qt_nuitrack_app.msg import Faces
from qt_robot_interface.srv import *
import time
from qt_nuitrack_app.msg import Gestures
import csv


speechSay = rospy.ServiceProxy('/qt_robot/speech/say', speech_say)

def rules_emotion():
    try:
        # call a ros service with text message
        rospy.loginfo("Explaining rules !")
        speechSay("Je vais te montrer des émotions et tu dois les imiter.")
    except KeyboardInterrupt:
        pass

def end_emotion():
    try:
        # call a ros service with text message
        rospy.loginfo("End of the exercise")
        speechSay("Fin de l'exercice, merci pour tes réponses !")
    except KeyboardInterrupt:
        pass

# this function is used in emotion_imitation and responsible for emptying the csv once program is completed to avoid having alot of data, we only need one reading.
def empty(csv_name):
    f = open(csv_name, "w")
    f.truncate()
    f.close()
    print("emptying successfull")


# this function is used in emotion_imitation and responsible for reading a csv file (contains readings for emotions), and searches if the index of a particular emotion is higher 
#(meaning the child displayed that emotion)

def emotion_check(csv_name,index,emotion_checked):
    i = 0
    with open(csv_name, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if len(row)!=0:
                #print("Curently examining row: ")
                #print(row)
                em = max(row)
                #print("the max of the row: "+ em)
                em_index = row.index(em)
                if em_index == index:
                    i = i+1
                    print("the subject is angry at row: "+ str(row))   
                else:
                    pass
    if i == 0:
        print("emotion not registered")
    else:
        print("correct emotion")    
        print(i)
    return i

# let's the robot show an emotion
def emotion(emo):
        faces_list = ["angry","happy","neutral"]
        emotionShow = rospy.ServiceProxy('/qt_robot/emotion/show', emotion_show)
        emotionShow("QT/"+str(emo))
