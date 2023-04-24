#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String
from qt_nuitrack_app.msg import Faces
from qt_robot_interface.srv import *
import time
from qt_nuitrack_app.msg import Gestures
import csv

now = time.time()
future = now + 20

def empty(csv_name):
    f = open("hello.csv", "w")
    f.truncate()
    f.close()
    print("emptying successfull")
    
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

def emotion(emo):
        faces_list = ["angry","happy","neutral"]
        emotionShow = rospy.ServiceProxy('/qt_robot/emotion/show', emotion_show)
        emotionShow("QT/"+faces_list[emo])
    
def face_callback(msg):
        print("starting callback")
        emotions = [msg.faces[0].emotion_angry,msg.faces[0].emotion_happy, msg.faces[0].emotion_surprise,msg.faces[0].emotion_neutral]
        em = max(emotions)
        em_index = emotions.index(em)
        

        # open the file in the write mode
        with open('hello.csv', 'a') as f:
    # create the csv writer
            writer = csv.writer(f)

    # write a row to the csv file
            writer.writerow(emotions)
        if time.time()>future:
            print("time is now")
            unregister(face)

def unregister(face):
    face.unregister()
# define ros subscriber

empty("hello.csv")
speechSay = rospy.ServiceProxy('/qt_robot/speech/say', speech_say)


rospy.init_node('my_tutorial_node')
#speechSay("Coucou, le programme commence maintenant, s'il vous plaît soyez attentifs.")
#speechSay("devinez l'émotion suivante")
emotion(0)
rospy.sleep(10)
print("start showing faces")
face = rospy.Subscriber('/qt_nuitrack_app/faces', Faces,face_callback)
rospy.sleep(30)

if emotion_check("hello.csv",0,"Angry")>0:
    print("the subject is Angry")
    
"""""
emotion(1)
rospy.sleep(20)
print("start showing faces")
face = rospy.Subscriber('/qt_nuitrack_app/faces', Faces,face_callback)
rospy.sleep(50)

if emotion_check("hello.csv",1,"Happy")>0:
    print("the subject is Happy")
"""    
try:
        rospy.spin()
except KeyboardInterrupt:
        pass
rospy.loginfo("finsihed!")
