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





# when initiating the node, this function is responsible for doing the reading of the child's emotions and then puts those emotions in a csv
def face_callback(msg):
        
        print("starting callback")
        emotions = [msg.faces[0].emotion_angry,msg.faces[0].emotion_happy, msg.faces[0].emotion_surprise,msg.faces[0].emotion_neutral]
        em = max(emotions)
        em_index = emotions.index(em)
        

        # open the file in the write mode
        with open('emotion_imitation.csv', 'a') as f:
    # create the csv writer
            writer = csv.writer(f)

    # write a row to theempty("emotion_imitation.csv") csv file
            writer.writerow(emotions)
        if time.time()>future:
            print("time is now")
            unregister(face)


#face = rospy.Subscriber('/qt_nuitrack_app/faces', Faces,face_callback)
# turns off the node
def unregister(face):
    face.unregister()          


def emotion_imitation(emotion_shown):
    
    score = 0
    if emotion_shown == "angry":

      if emotion_check("emotion_imitation.csv",0,"angry")>0:
        speechSay("Bravo c'est la bonne repose")
        print("the subject is angry")
        score += 1
      else:
          speechSay("Passons à l'emotion suivant")  
    if emotion_shown == "happy":
      if emotion_check("emotion_imitation.csv",1,"happy")>0:
        print("the subject is happy")
        speechSay("Bravo c'est la bonne repose")
        score += 1
      else:
          speechSay("Passons à l'emotion suivant")      
    if emotion_shown == "neutral":
      
      if emotion_check("emotion_imitation.csv",4,"neutral")>0:
        speechSay("Bravo c'est la bonne repose")
        print("the subject is neutral")
        score += 1
      else:
          speechSay("Passons à l'emotion suivant")  
    finalScore = str(int(score/100))
    return finalScore

def emotion_imitation_detection(imitation_face):
    global now 
    now = time.time()
    global future 
    future = now + 20
    #emotion_imitation("angry")
    
    empty("emotion_imitation.csv")
    
    emotion(imitation_face)
    #rospy.sleep(10)
    print("the user can start showing faces")
    global face 
    face = rospy.Subscriber('/qt_nuitrack_app/faces', Faces,face_callback)
    rospy.sleep(30)
    emotion_imitation(imitation_face)

