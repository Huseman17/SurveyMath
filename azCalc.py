#Azimuth Calculator
#Daniel Huseman
#8/20/2019
#
#Input two coordinates and program returns azimuth from point
#A to Point B, and displays an arrow pointing in the direction
#of that azimuth.
#
#To Do: Build a GUI for the program

import math
from PIL import Image
#import matplotlib
#import numpy

def boatPic(az):
	#PIL rotates images counterclockwise, thus requiring the 
	#input azimuth to be negative to achieve a clockwise rotation
	azForPil = az * -1
	pic = Image.open("C:\\Users\\Sonny\\Documents\\Python\\arrow.jpg")
	rotated = pic.rotate(azForPil)
	rotated.show()	
	
def azimuth(coordinates):
	dX = coordinates[1][0]-coordinates[0][0]
	dY = coordinates[1][1]-coordinates[0][1]
	range = round(float(math.sqrt(dX**2+dY**2)),3)
	az = math.atan2(dY,dX)
	az = 90 - math.degrees(az)
	az = round(az % 360,3)
	return([az, range])
	
def getCoordinates():
	coord1 = input(str("Input coordinate 1 in format x,y:"))
	coord2 = input(str("Input coordinate 2 in format x,y:"))
	#coord1 = '0,0'
	#coord2 = '1,1'	
	
	coord1 = coord1.split(',')
	coord1list = [float(coord1[0]),float(coord1[1])]
	
	coord2 = coord2.split(',')
	coord2list = [float(coord2[0]),float(coord2[1])]
	
	return([coord1list,coord2list])

def main():
	coordinates = getCoordinates()
	az_range = azimuth(coordinates)
	print("Azimuth: ", az_range[0])
	print("Range:   ", az_range[1])
	boatPic(az_range[0])
	
main()