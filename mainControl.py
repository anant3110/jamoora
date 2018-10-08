import speech_recognition as sr
from threading import Thread, Lock
import os

r = sr.Recognizer()
mic = sr.Microphone()
sr.Microphone.list_microphone_names()

filename = "commands.txt"

# ssh = paramiko.SSHClient()
# ssh.connect("192.168.2.22", username="pi", password="raspberri")
# ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls')
# print(ssh_stdout) #print the output of ls command


# client = paramiko.SSHClient()
# client.load_system_host_keys()
# client.connect('pi@raspberripi.local')
# # stdin, stdout, stderr = client.exec_command('ls -l')


def express(audio1):
	try:
		
		command = r.recognize_google(audio1, show_all=True)
		
		finalComm = ""

		for i in command["alternative"]:			
			finalComm += " " + i["transcript"]

		print finalComm

		file = open(filename, "w")
		file.writelines(finalComm)
		file.close()
		os.system("scp commands.txt pi@192.168.2.22:Desktop/jamoora/")


	except:
		pass



while(True):
	with mic as source:
		audio = r.record(source, duration=3) #listen
		#print(" ")
		#print(r.recognize_google(audio))
		thread = Thread(target = express, args=(audio,))
		thread.start()

#print(r.recognize_google(audio))






