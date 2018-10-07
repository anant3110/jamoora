import speech_recognition as sr
from threading import Thread, Lock

r = sr.Recognizer()
mic = sr.Microphone()
sr.Microphone.list_microphone_names()


def express(audio1):
    try:
    	print(r.recognize_google(audio1)) #, show_all=True))
    except:
    	pass

while(True):
	with mic as source:
		audio = r.listen(source)
		print(" ")
		#print(r.recognize_google(audio))
		thread = Thread(target = express, args=(audio,))
		thread.start()


#print(r.recognize_google(audio))
