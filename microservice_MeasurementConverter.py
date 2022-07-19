# Ingredient Measurement Converter

# This microservice communicates with the Ingredients in Season application. 
# The Ingredients app sets up the socket connection and the microservice connects to the socket.
# The Ingredients app will send an encoded request to the microservice.
# The microservice will respond, and the Ingredients app will receive the message.

import time, socket, sys
import json

print("Initializing....\n")
time.sleep(1)

s = socket.socket()
shost = 'localhost'                             # specify publishing host (Ingredients App)
host = 'localhost'                              # specify subscribing host  (App)
name = "Measurement Converter"
port = 1234                                     # specify port
print("Trying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())                           # send microservice name
s_name = s.recv(1024)                           # receive app name (Ingredients App)
s_name = s_name.decode()                        # store name of app for ease of identification
print("Type EXIT to quit")
print("Enter message to send...")

# Measurement Conversions
def tbsp2tsp(msg):
    try:
        tbsp_val = float(msg["amount"])
    except:
        return "Error"
    tsp = tbsp_val * 3
    return tsp

# Continuous Communication Pipeline
while True:
    message = s.recv(1024)                      # receive message from app (Ingredients App)
    try:
        message = json.loads(message)           # convert serialized json to dictionary
    except:
        msg_type = "non_dict"
        message = message.decode()
    print(s_name + ":", message)                # display message from app (Ingredients App)
    if message == "EXIT":                       # exit if the entered message is EXIT
        print("Exiting...")
        break
    elif msg_type != "non_dict":
        if message["from_units"] == "tbsp" and message["to_units"] == "tsp":
            message = str(tbsp2tsp(message))
            s.send(message.encode())
            print(str(name)+": "+str(message))
    else:
        message = input(str(name+": "))         # user enter message to send
        s.send(message.encode())
    msg_type = ""
    