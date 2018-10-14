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
		singleForward(2,speed);
		singleBackward(3,speed);	
	


def backward(duration,speed):
	print "backward"
	sleep(0.25);	
	for i in range(0,duration):
		singleForward(3,speed);
		singleBackward(2,speed);



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


def unclamp(duration):
	print "unclamp"
	bot.digitalWrite( 24, 0 );
	bot.digitalWrite( 22, 1 );
	sleep(duration);
	bot.digitalWrite( 24, 0 );
	bot.digitalWrite( 22, 0 );


def clamp(duration):
	print "clamp"
	bot.digitalWrite( 24, 1 );
	bot.digitalWrite( 22, 0 );
	sleep(duration);
	bot.digitalWrite( 24, 0 );
	bot.digitalWrite( 22, 0 );	


def up(duration,speed):
	print "up"
	sleep(0.25);	
	for i in range(0,duration):
		singleForward(1,speed);

def down(duration,speed):
	print "down"
	sleep(0.25);	
	for i in range(0,duration):
		singleBackward(1,speed);


if __name__ == '__main__':

	bot = MegaPi()
	bot.start()
	

	speed=100

	# down(1,50)

	#RESET SYSTEM
	# if sys.argv[0] == "reset":
	# 	clamp()
	# 	down()

	#clamp()

	# sleep(1);

	# bot.encoderMotorSetCurPosZero(3);
	# bot.encoderMotorSetCurPosZero(2);


	#MANUAL COMMANDS
	if sys.argv[1] == "up":
		up(1,100)
	if sys.argv[1] == "down":
		down(1,100)
	if sys.argv[1] == "forward":
		forward(5,75)
	if sys.argv[1] == "backward":
		backward(5,75)
	if sys.argv[1] == "right":
		right(5,75)
	if sys.argv[1] == "left":
		left(5,75)
	if sys.argv[1] == "clamp":
		clamp(3)
	if sys.argv[1] == "unclamp":
		unclamp(3)
	#End Manual


	if sys.argv[1] == "gloomy":
		speed=50
		down(1,100) #medium to down

	elif sys.argv[1] == "happy": 
		speed=100
		up(2,100)

	elif sys.argv[1] == "angry":
		speed=75
		#down(1,100)

	elif sys.argv[1] == "serious":
		speed=75
		#Neck
	


	if sys.argv[2] == "thirst":
		thirsty(speed)
	elif sys.argv[2] == "find":
		finds(speed)
	elif sys.argv[2] == "low":
		low(speed)
	elif sys.argv[2] == "fill":
		fill(speed)
	elif sys.argv[2] == "drink":
		drink(speed)
	elif sys.argv[2] == "interactive":
		interactive(sys.argv[1])

	
	try:


		if sys.argv[2] == "thirst":
			left(4,speed)
			sleep(1);
			forward(4,speed)
			sleep(1);
			backward(4,speed)
			sleep(1);
			right(10,speed)
			pass
			
		elif sys.argv[2] == "find":

			clamp(1)
			unclamp(1)
			clamp(1)
			unclamp(1)
			forward(5,speed)
			pass

		elif sys.argv[2] == "low":
			backward(3,speed)
			down(1, speed)
			clamp(1)
			forward(1,speed)
			pass

		elif sys.argv[2] == "fill":
			
			left(6,speed)
			forward(3,speed)
			unclamp(2)
			clamp(2)
			backward(3,speed)
			right(7,speed)
			unclamp(2)
			pass

		elif sys.argv[2] == "drink":
			#drink
			up(2,speed)
			clamp(1)
			unclamp(1)
			clamp(1)
			unclamp(1)
			clamp(1)
			unclamp(1)
			clamp(1)
			unclamp(1)


	except:
		pass
		

	# print "hola"

	while 1:

		cmd1 = "kill -9 " + str(os.getpid()+1)
		cmd2 = "kill -9 " + str(os.getpid())

		os.system(cmd1)
		os.system(cmd2)

		sleep(1)


def interactive(mood):
	if(mood == "happy"):
		up()
		unclamp()
		sleep(1)
		forward(2,100)
		backward(2,100)
		down()
	if(mood == "gloomy"):
		down(1,10)
		clamp()
		forward(2,25)
		sleep(2)
		backward(2,25)
		up(1,100)
		unclamp()
	if(mood == "angry"):
		forward(1,10)
		up(1,100)
		clamp()
		sleep(1)
		down(1,100)
		unclamp()
		sleep(1)
		up(1,100)
		clamp()
		backward(1,10)
		down(1,100)
		unclamp()
		sleep(1)
	if(mood == "serious"):
		down(1,100)
		unclamp()
		unclamp()
		forward(2,100)
		backward(2,100)
		clamp()
		clamp()
		up(1,100)












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
