#!/usr/bin/env python
from qt_robot_interface.srv import *
import sys
import rospy
from std_msgs.msg import String
from qt_nuitrack_app.msg import Faces
import time
"""
def emotion(msg):
    faces_list = ["happy","angry","neutral"]
    emotionShow = rospy.ServiceProxy('/qt_robot/emotion/show', emotion_show)
    emotionShow("QT/"+faces_list[msg])


def main():
    speechSay = rospy.ServiceProxy('/qt_robot/speech/say', speech_say)
    speechSay("Coucou, le programme commence maintenant, s'il vous plaît soyez attentifs.")

    speechSay("devinez l'émotion suivante")
    emotion(0)
    
    speechSay("Je vais le répéter une fois de plus")
    emotion(0)
    
    speechSay("prochaine émotion, les yeux ici")
    emotion(1)
    
    speechSay("Je vais le répéter une fois de plus")
    emotion(1)
    
    speechSay("prochaine émotion, les yeux ici")
    emotion(2)
    
    speechSay("Je vais le répéter une fois de plus")
    emotion(2)

main()
"""

def emotion(msg):
    faces_list = ["happy","angry","neutral"]
    emotionShow = rospy.ServiceProxy('/qt_robot/emotion/show', emotion_show)
    emotionShow("QT/"+faces_list[msg])
    
    
def main():
    speechSay = rospy.ServiceProxy('/qt_robot/speech/say', speech_say)
    """
    speechSay("Coucou, le programme commence maintenant, s'il vous plaît soyez attentifs.")

    speechSay("devinez l'émotion suivante")
    emotion(0)
    """
    now = time.time()
    future = now + 10
    while time.time() < future:
        print(time.time())
        emotion(0)

main()        
            
