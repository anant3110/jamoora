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


def unclamp():
	bot.digitalWrite( 24, 0 );
	bot.digitalWrite( 22, 1 );
	sleep(1);
	bot.digitalWrite( 24, 0 );
	bot.digitalWrite( 22, 0 );


def clamp():
	bot.digitalWrite( 24, 1 );
	bot.digitalWrite( 22, 0 );
	sleep(1);
	bot.digitalWrite( 24, 0 );
	bot.digitalWrite( 22, 0 );	


def up():


def down():


if __name__ == '__main__':

	bot = MegaPi()
	bot.start()
	
	print sys.argv[0]
	print sys.argv[1]

	speed=75

	if sys.argv[0] == "reset":
		clamp()
		down()


	if sys.argv[0] == "gloomy":
		speed=50
		down()


	elif sys.argv[0] == "serious": 
		speed=50

	elif sys.argv[0] == "gloomy":
			

	elif sys.argv[0] == "serious"



	print "hola"

	while 1:

		cmd1 = "kill -9 " + str(os.getpid()+1)
		cmd2 = "kill -9 " + str(os.getpid())

		os.system(cmd1)
		os.system(cmd2)

   		sleep(1)














#Comments

	#bot.encoderMotorMove(slot,100,-1000,onBackwardFinish);
	#bot.encoderMotorRun( slot, 100 )





		# try:
		# 	filename = "commands.txt"
		# 	file = open(filename, "r")
		
		# 	for line in file:   			
   				
  #  				if "forward" in line:
  #  					forward(2,100)

  #  				if "backward" in line:
  #  					backward(2,100)

  #  				if "left" in line:
  #  					left(2,100)

  #  				if "right" in line:
  #  					right(2,100)

  #  				if "clamp" in line:
  #  					clamp()

  #  				if "unclamp" in line:
  #  					unclamp()

  #  			file.close()

  #  			os.remove("commands.txt")

  #  		except:

  #  			pass
  #  			#print "Nothing To Do"



	#servoRun( port, slot, angle )
	
	#bot.motorRun(4, 1);

	#singleBackward(1,100);

	# sleep(1);
	# bot.motorRun(4, -50);
