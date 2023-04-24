#!/bin/python

# this code will aim to create that does two things: show emotion, ask a question about the correct emotion and analyze the child's response, keep a score

import rospy
import sys
from std_msgs.msg import String
from qt_robot_interface.srv import *



# Show emotion.
def emotion(emo):
    faces_list = ["angry","happy","neutral"]
    emotionShow = rospy.ServiceProxy('/qt_robot/emotion/show',emotion_show)
    emotionShow("QT/"+faces_list[emo])


emotion(0)


# Asking a question.

# wait for a child's reply.
