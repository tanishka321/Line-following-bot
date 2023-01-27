from gym_line_follower.helper import LaRoboLigaEnv

import LRL_main_arena
import gym
import time
import pybullet as p
import cv2
import os
import numpy as np


env = gym.make("la_robo_liga_arena-v0")
if _name_ == '_main_':
    parent_path = os.path.dirname(os.getcwd()) # This line is to switch the directories for getting resources.
    os.chdir(parent_path)                      # you don't need to change anything in here.    

        # This loads the arena.
   
    # Initialize your global variables/constants here. 
    
    
    while True:   
        env.move_husky(20,-20,20,-20)
        p.stepSimulation()                             # main loop to run the simulation.             
         
        image=env.get_camera_image()
                      # capture images, extract data from them and take actions accordingly to complete the obj.
        #img=cv2.imread(image)
                                                    
        #finding for yellow
        hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)     #converting to hsv and masking
        lowerbound=np.array([20,80,80])
        upperbound=np.array([30,255,255])
        
        mask=cv2.inRange(hsv,lowerbound,upperbound)
        cv2.imshow("mask",mask)
        cv2.waitKey(1)
        #cv2.destroyAllWindows()