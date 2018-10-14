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
prevMood = 1

Happy = {59+12,48+12,50+12,53+12,55+12,59+12,60+12, 60+12,58+12,57+12,53+12,52+12,50+12,55+12,53+12,52+12,50+12,52+12,57+12,48+12}
Serious = {48+12,50+12,51+12,53+12,55+12,57+12,58+12,60+12,60+12,58+12,57+12,55+12,53+12,51+12,50+12,48+12}
Angry = {48+12,49+12,54+12,59+12,60+12,60+12,59+12,56+12,55+12,54+12,52+12,49+12,48+12}
Gloomy = {48+12,50+12,53+12,55+12,56+12,58+12,60+12,58+12,56+12,55+12,53+12,51+12,50+12,48+12}

volumePrev = 0
q = Queue(6)
#End Music Init


#SSH Command Init
SSH_ADDRESS = "192.168.2.22"
SSH_USERNAME = "pi"
SSH_PASSWORD = "raspberrypi"
SSH_COMMAND_BASE = "cd Desktop/jamoora; python moveTest.py "
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_stdin = ssh_stdout = ssh_stderr = None
#End SSH Command Init


#Music Functions
def is_a_in_x(A, X):
  for i in range(len(X) - len(A) + 1):
    if A == X[i:i+len(A)]: return True
  return False

def print_volume_handler(unused_addr, args, volume):
  global mainMood
  global prevMood
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
  elif(which.count(True) == 1 and prevMood != mainMood):
    prevMood = mainMood
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
    SSH_COMMAND = SSH_COMMAND_BASE + mainMood + " interactive"
	executeCommand(SSH_COMMAND)
#End Music Functions

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





