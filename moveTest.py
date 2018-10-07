from megapi import *
import sys
import os

def doNothing(temp):
	pass

def singleForward(slot,speed):
	sleep(0.4);
	bot.encoderMotorMove(slot,speed,-1000,doNothing);	


def singleBackward(slot,speed):
	sleep(0.4);
	bot.encoderMotorMove(slot,speed,1000,doNothing);


def forward(duration,speed):
	print "forward"
	sleep(0.25);	
	for i in range(0,duration):
		singleForward(3,speed);
		singleBackward(2,speed);


def backward(duration,speed):
	print "backward"
	sleep(0.25);	
	for i in range(0,duration):
		singleForward(2,speed);
		singleBackward(3,speed);


def right(duration,speed):
	print "right"
	sleep(0.25);	
	for i in range(0,duration):
		singleForward(3,speed);
		singleForward(2,speed);



def left(duration,speed):
	print "left"
	sleep(0.25);	
	for i in range(0,duration):
		singleBackward(3,speed);
		singleBackward(2,speed);



if __name__ == '__main__':

	bot = MegaPi()
	bot.start()
	

	while 1:
		
		try:
			filename = "commands.txt"
			file = open(filename, "r")
		
			for line in file:   			
   				
   				if "forward" in line:
   					forward(2,100)

   				if "backward" in line:
   					backward(2,100)

   				if "left" in line:
   					left(2,100)

   				if "right" in line:
   					right(2,100)

   			file.close()

   			os.remove("commands.txt")

   		except:

   			pass
   			#print "Nothing To Do"

   		sleep(0.01)



#Comments

	#bot.encoderMotorMove(slot,100,-1000,onBackwardFinish);
	#bot.encoderMotorRun( slot, 100 )
