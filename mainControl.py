import speech_recognition as sr
from threading import Thread, Lock
import os
import paramiko
import sys

#Music Imports
import argparse
import math
from pythonosc import dispatcher
from pythonosc import osc_server
from queue import Queue




#Music Init
mainMood = 0

Happy = {59+12,48+12,50+12,53+12,55+12,59+12,60+12, 60+12,58+12,57+12,53+12,52+12,50+12,55+12,53+12,52+12,50+12,52+12,57+12,48+12}
Serious = {48+12,50+12,51+12,53+12,55+12,57+12,58+12,60+12,60+12,58+12,57+12,55+12,53+12,51+12,50+12,48+12}
Angry = {48+12,49+12,54+12,59+12,60+12,60+12,59+12,56+12,55+12,54+12,52+12,49+12,48+12}
Gloomy = {48+12,50+12,53+12,55+12,56+12,58+12,60+12,58+12,56+12,55+12,53+12,51+12,50+12,48+12}

volumePrev = 0
q = Queue(4)
#End Music Init


#Speech Init
r = sr.Recognizer()
mic = sr.Microphone()
sr.Microphone.list_microphone_names()
#End Speech Init


#SSH Command Init
SSH_ADDRESS = "192.168.2.22"
SSH_USERNAME = "pi"
SSH_PASSWORD = "raspberrypi"
SSH_COMMAND_BASE = "cd Desktop/jamoora; python moveTest.py "
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_stdin = ssh_stdout = ssh_stderr = None

thirstWords = ["oasis", "dried", "desert", "thirsty", "searching"]
findWords = ["hope", "vessel", "water", "ran"]
lowWords = ["unfortunately", "low", "frustrated", "idea"]
fillWords = ["pebbles", "picked", "carefully", "dropped", "level", "rise"]
drinkWords = ["finally", "effort", "drink", "end"]


thirstAction = 0 
findAction = 0 
lowAction = 0
fillAction = 0 
drinkAction = 0

#End SSH Command Init


#Music Functions
def is_a_in_x(A, X):
  for i in range(len(X) - len(A) + 1):
    if A == X[i:i+len(A)]: return True
  return False

def print_volume_handler(unused_addr, args, volume):
  global mainMood
  global q, volumePrev
  if(not q.full() and volume != volumePrev and volume in range(59, 73)):
    q.put(volume)
    volumePrev = volume
  elif(q.full() and volume != volumePrev and volume in range(59,73)):
    q.get()
    q.put(volume)
    volumePrev = volume
  l = list(q.queue)
  s = set(l)
  which = [s.issubset(Happy) , s.issubset(Serious), s.issubset(Angry), s.issubset(Gloomy)]
  if(which.count(True) == 0):
    while(not q.empty):
      q.get()
  elif(which.count(True) == 1):
    if(which[0]):
      #print("Happy")
      mainMood="happy"
    if(which[1]):
      #print("Serious")
      mainMood="serious"
    if(which[2]):
      #print("Angry")
      mainMood="angry"
    if(which[3]):
      #print("Gloomy")
      mainMood="gloomy"
#End Music Functions



#Speech Functions
def executeCommand(SSH_COMMAND):

	print ("executing")
	print (SSH_COMMAND)

	try:
	    ssh.connect(SSH_ADDRESS, username=SSH_USERNAME, password=SSH_PASSWORD)
	    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(SSH_COMMAND)
	except Exception as e:
	    sys.stderr.write("SSH connection error: {0}".format(e))

	try:
		if ssh_stdout:
		    sys.stdout.write(ssh_stdout.read())
		if ssh_stderr:
		    sys.stderr.write(ssh_stderr.read())
	except:
		pass


def detectMotion(mainMood,finalComm):

	global thirstAction  
	global findAction  
	global lowAction 
	global fillAction  
	global drinkAction

	for i in thirstWords:
		if i in finalComm:
			if thirstAction==0:
				SSH_COMMAND = SSH_COMMAND_BASE + mainMood + " thirst"
				thirstAction=1
				executeCommand(SSH_COMMAND)

	for i in thirstWords:
		if i in finalComm:
			if thirstAction==0:
				SSH_COMMAND = SSH_COMMAND_BASE + mainMood + " find"
				findAction=1
				executeCommand(SSH_COMMAND)
			 
	for i in thirstWords:
		if i in finalComm:
			if thirstAction==0:
				SSH_COMMAND = SSH_COMMAND_BASE + mainMood + " low"
				lowAction=1
				executeCommand(SSH_COMMAND)
			

	for i in thirstWords:
		if i in finalComm:
			if thirstAction==0:
				SSH_COMMAND = SSH_COMMAND_BASE + mainMood + " fill"
				fillAction=1
				executeCommand(SSH_COMMAND)
			 

	for i in thirstWords:
		if i in finalComm:
			if thirstAction==0:
				SSH_COMMAND = SSH_COMMAND_BASE + mainMood + " drink"
				drinkAction=1
				executeCommand(SSH_COMMAND)


	if "reset" in finalComm:
		SSH_COMMAND = SSH_COMMAND_BASE + "reset"
		executeCommand(SSH_COMMAND)



	if "clamp" in finalComm:
		SSH_COMMAND = SSH_COMMAND_BASE + "clamp"
		executeCommand(SSH_COMMAND)
		return

	elif "open" in finalComm:
		SSH_COMMAND = SSH_COMMAND_BASE + "unclamp"
		executeCommand(SSH_COMMAND)
		return

	elif "up" in finalComm:
		SSH_COMMAND = SSH_COMMAND_BASE + "up"
		executeCommand(SSH_COMMAND)
		return

	elif "down" in finalComm:
		SSH_COMMAND = SSH_COMMAND_BASE + "down"
		executeCommand(SSH_COMMAND)
		return

	elif "right" in finalComm:
		SSH_COMMAND = SSH_COMMAND_BASE + "right"
		executeCommand(SSH_COMMAND)
		return

	elif "left" in finalComm:
		SSH_COMMAND = SSH_COMMAND_BASE + "left"
		executeCommand(SSH_COMMAND)
		return

	elif "forward" in finalComm:
		SSH_COMMAND = SSH_COMMAND_BASE + "backward"
		executeCommand(SSH_COMMAND)
		return

	elif "backward" in finalComm:
		SSH_COMMAND = SSH_COMMAND_BASE + "forward"
		executeCommand(SSH_COMMAND)
		return



def express(audio1):
	try:
		#print("recog")
		command = r.recognize_google(audio1, show_all=True)
		
		#print (command["alternative"])

		finalComm = ""

		for j in command["alternative"]:
			finalComm += " " + j["transcript"]
		
		print (mainMood, finalComm)
		
		detectMotion(mainMood,finalComm)

	except:
		pass


def continuousRec():
	while(True):
		with mic as source:
			#print ("listening")
			audio = r.record(source, duration=3) #listen
			#print(" ")
			#print(r.recognize_google(audio))
			thread = Thread(target = express, args=(audio,))
			thread.start()

#End Speech Functions


print ("lololololol")


threadSpeech = Thread(target = continuousRec)
threadSpeech.start()


#Manual Intervention
# SSH_COMMAND = str(SSH_COMMAND_BASE + "forward")
# executeCommand(SSH_COMMAND)


print ("lololololol")

'''
#Music Server Setup
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1", help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=8000, help="The port the OSC server is listening on")
args = parser.parse_args()
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/pitch", print_volume_handler, "Pitch")
server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()
#End Server
'''


#print(r.recognize_google(audio))






