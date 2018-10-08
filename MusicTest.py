import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server
from queue import Queue

Happy = {59+12,48+12,50+12,53+12,55+12,59+12,60+12, 60+12,58+12,57+12,53+12,52+12,50+12,55+12,53+12,52+12,50+12,52+12,57+12,48+12}

Serious = {48+12,50+12,51+12,53+12,55+12,57+12,58+12,60+12,60+12,58+12,57+12,55+12,53+12,51+12,50+12,48+12}

Angry = {48+12,49+12,54+12,59+12,60+12,60+12,59+12,56+12,55+12,54+12,52+12,49+12,48+12}

Gloomy = {48+12,50+12,53+12,55+12,56+12,58+12,60+12,58+12,56+12,55+12,53+12,51+12,50+12,48+12}

volumePrev = 0
q = Queue(5)

def is_a_in_x(A, X):
  for i in range(len(X) - len(A) + 1):
    if A == X[i:i+len(A)]: return True
  return False

def print_volume_handler(unused_addr, args, volume):
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
      print("Happy")
    if(which[1]):
      print("Serious")
    if(which[2]):
      print("Angry")
    if(which[3]):
      print("Gloomy")


parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1", help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=8000, help="The port the OSC server is listening on")
args = parser.parse_args()

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/pitch", print_volume_handler, "Pitch")
server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()


