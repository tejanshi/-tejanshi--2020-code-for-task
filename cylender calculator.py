# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:45:18 2020

@author: shilp
"""

import time

print("This app will calculate the surface are, lateral surface area, perimeter and volume of any Cylinder")

H=float(input("height-"))

R=float(input("Radius-"))

P=22/7

time.sleep(1)

print("Volume-"+str(P*R*R*H))

time.sleep(1)

print("Total Surface Area-"+str(2*P*R*(R+H)))

time.sleep(1)

print("Lateral Surface Area-"+str(2*P*R*H))

time.sleep(1)

print("Perimeter-"+str(2*P*R))