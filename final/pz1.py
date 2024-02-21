#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from gs_flight import FlightController, CallbackEvent
from gs_board import BoardManager
from gs_module import ModuleLedController
from time import sleep

rospy.init_node("flight_test_node")
coordinates = [
    [1.4,3.5,0.7],
    [2.7,4.6,1.2],
    [0.1,4.6,1.2],
    [0.1,4.4,1.2],
    [0.4,2.3,1.2],
    [0.6,0.1,1.2],
    [2.6,2.3,1.2],
    [1.3,1.2,0.8]
]

run = True
position_number = 0

def callback(event):
    global ap
    global run
    global coordinates
    global position_number

    event=event.data
    if event == CallbackEvent.ENGINES_STARTED:
        print("engine started")
        ap.takeoff()
    elif event == CallbackEvent.TAKEOFF_COMPLETE:
        # ModuleLedController.changeAllColor(0, 255, 0, 0) 
        # sleep(1) 
        print("takeoff complete")
        position_number = 0
        ap.goToLocalPoint(coordinates[position_number][0], coordinates[position_number][1], coordinates[position_number][2])
    elif event == CallbackEvent.POINT_REACHED:
        print(f"point {position_number} reached")
        # ModuleLedController.changeAllColor(0, 0, 255, 0) 
        # sleep(0.4)
        position_number += 1
        if position_number < len(coordinates):
            ap.goToLocalPoint(coordinates[position_number][0], coordinates[position_number][1], coordinates[position_number][2])
        else:
            ap.landing()
    elif event == CallbackEvent.COPTER_LANDED:
        print("finish programm")
        run = False

board = BoardManager()
ap = FlightController(callback)

once = False

while not rospy.is_shutdown() and run:
    if board.runStatus() and not once:
        print("start programm")
        ap.preflight()
        once = True
    pass