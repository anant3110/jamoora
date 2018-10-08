import speech_recognition as sr
from threading import Thread, Lock
import paramiko
import sys



r = sr.Recognizer()
mic = sr.Microphone()
sr.Microphone.list_microphone_names()


# def express(audio1):
#     try:
#     	print(r.recognize_google(audio1)) #, show_all=True))
#     except:
#     	pass

# while(True):
# 	with mic as source:
# 		audio = r.listen(source)
# 		print(" ")
# 		#print(r.recognize_google(audio))
# 		thread = Thread(target = express, args=(audio,))
# 		thread.start()


# #print(r.recognize_google(audio))

## EDIT SSH DETAILS ##

SSH_ADDRESS = "192.168.2.22"
SSH_USERNAME = "pi"
SSH_PASSWORD = "raspberrypi"
SSH_COMMAND = "cd Desktop/jamoora; python moveTest.py"

## CODE BELOW ##

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_stdin = ssh_stdout = ssh_stderr = None

try:
    ssh.connect(SSH_ADDRESS, username=SSH_USERNAME, password=SSH_PASSWORD)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(SSH_COMMAND)
except Exception as e:
    sys.stderr.write("SSH connection error: {0}".format(e))

if ssh_stdout:
    sys.stdout.write(ssh_stdout.read())
if ssh_stderr:
    sys.stderr.write(ssh_stderr.read())


