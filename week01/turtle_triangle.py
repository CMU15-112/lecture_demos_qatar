from turtle import *
import math

beta = math.acos(25/100)
beta = math.degrees(beta)
alpha = 180 - 2*beta

forward(50)
right(180-beta)
forward(100)
right(180-alpha)
forward(100)