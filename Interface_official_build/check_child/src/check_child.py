#!/usr/bin/env python

# this script was created to check the child's attention before running a test.

import sys
import csv
import rospy
from qt_robot_interface.srv import *
from qt_vosk_app.srv import *
from qt_nuitrack_app.msg import Faces
import time
import PySimpleGUI as psg




csv_name="check_child.csv"


def empty(csv_name):
    f = open(csv_name, "w")
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
        with open(csv_name, 'a') as f:
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



	 # check chile
def check_child():
    empty(csv_name)
    rospy.loginfo("Checking child's attention Launched, waiting for the services to initialized!")
    global now 
    now = time.time()
    global future 
    future = now + 20

    # define the ros service
    speechSay = rospy.ServiceProxy('/qt_robot/speech/say', speech_say)
    recognize = rospy.ServiceProxy('/qt_robot/speech/recognize', speech_recognize)

    # block/wait for ros service
    rospy.wait_for_service('/qt_robot/speech/say')
    rospy.wait_for_service('/qt_robot/speech/recognize')
    rospy.loginfo("Services initiated")
    child_well= False
                  
    try:

        # call a ros service with text message
        rospy.loginfo("Explaining rules!")
        #speechSay("Je vais maintenant vous poser une question")
        print("Je vais maintenant vous poser une question")
        good_answers = ["ça va","oui","merci","hello","ça roule"]
        bad_answers = ["ça va pas","non"]
        # asks a question to check child, ex: "How are you doing?"
        speechSay("Comment vas-tu aujourd'hui ?")
        print("Comment vas-tu aujourd'hui ?")
        resp = recognize("fr_FR", [], 10)
     
        
        # if the child's answer is in the good answers list then we return that the child is well
        if any(good_answer in resp.transcript for good_answer in good_answers):
            emotion(1)
            #print(good_answer)
            speechSay("wow, content que tu te sois senti en pleine forme !")
            rospy.loginfo("Acceptable answer")
            child_well= True

        # if the child's answer is in the bad answers list or no answer is detected then we read the emotion of the child:
            # if child is angry --> pop message and the script is paused
            # if child is happy --> return child is well and continue the script 
        else:
                print(child_well)
                #speechSay("oh non")
                #print(bad_answer)
                rospy.loginfo("Not Acceptable answer")
                print("Attempting to read faces")
                global face
                face = rospy.Subscriber('/qt_nuitrack_app/faces', Faces,face_callback)
                rospy.sleep(20)
                rospy.loginfo("reading child's emotion")
                if emotion_check(csv_name,1,"happy")>0:
                    
                    child_well= True
                else:
                    psg.popup_ok("the child seems to disturbed, please click Ok to Resume the program")
                    child_well= True

        rospy.loginfo("End of the exercise")
        
    except KeyboardInterrupt:
        pass
    print(child_well)


# if child answers not good --> pop up message on the mainframe to call teacher

# if no answer detected --> check child's emotion
	# if angry --> pop message call teacher
	# if happy --> begin assessement

#if answer good --> begin test
