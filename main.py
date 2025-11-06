import numpy as np
import scipy as sp

from functions import *

position = [0,0,0]
velocity = [0,0,0]
acceleration = [0,0,-sp.constants.g]

drag_coefficient = 1.28 # flat plate
air_density = 1.204 # 1atm 20C 
mass = 10
area = [10,10,10]

position[2] = int(input("How high is the cube? (m) "))

time=0
while position[2] > 0:
    position = update_position(position,velocity,acceleration,time)
    velocity = update_velocity(velocity,acceleration,time)

    print("\n\n\nElapsed Time = {}s".format(time))
    print("------------------")
    print("Position:\n x = {:.2f} m\n y = {:.2f} m\n z = {:.2f} m".format(position[0],position[1],position[2]))
    print("Velocity:\n x = {:.2f} m/s\n y = {:.2f} m/s\n z = {:.2f} m/s".format(velocity[0],velocity[1],velocity[2]))
    print("Acceleration:\n x = {:.2f} m/s^2\n y = {:.2f} m/s^2\n z = {:.2f} m/s^2".format(acceleration[0],acceleration[1],acceleration[2]))

    time+=1