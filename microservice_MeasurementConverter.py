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

#######################################################################################################
# Measurement Conversions
#
#
#######################################################################################################
def tbsp2tsp(msg):
    """Convert tablespoons to teaspoons
    """
    try:
        tbsp_val = float(msg["amount"])
    except:
        return "Error"
    tsp = round(tbsp_val * 3, 1)
    return tsp

def tsp2tbsp(msg):
    """Convert teaspoons to tablespoons
    """
    try:
        tsp_val = float(msg["amount"])
    except:
        return "Error"
    tbsp = round(tsp_val / 3, 1)
    return tbsp

def tbsp2cups(msg):
    """Convert tablespoons to cups
    """
    try:
        tbsp_val = float(msg["amount"])
    except:
        return "Error"
    cups = round(tbsp_val * 0.0625, 1)
    return cups

def cups2tbsp(msg):
    """Convert cups to tablespoons
    """
    try:
        cups_val = float(msg["amount"])
    except:
        return "Error"
    tbsp = round(cups_val * 16, 1)
    return tbsp

def tbsp2floz(msg):
    """Convert tablespoons to fluid ounces
    """
    try:
        tbsp_val = float(msg["amount"])
    except:
        return "Error"
    floz = round(tbsp_val / 2, 1)
    return floz

def floz2tbsp(msg):
    """Convert fluid ounces to tablespoons
    """
    try:
        floz_val = float(msg["amount"])
    except:
        return "Error"
    tbsp = round(floz_val * 2, 1)
    return tbsp

def cups2floz(msg):
    """Convert cups to fluid ounces
    """
    try:
        cups_val = float(msg["amount"])
    except:
        return "Error"
    floz = round(cups_val * 8, 1)
    return floz

def floz2cups(msg):
    """Convert fluid ounces to cups
    """
    try:
        floz_val = float(msg["amount"])
    except:
        return "Error"
    cups = round(floz_val / 8, 1)
    return cups

def tsp2cups(msg):
    """Convert teaspoons to cups
    """
    try:
        tsp_val = float(msg["amount"])
    except:
        return "Error"
    cups = round(tsp_val / 48, 1)
    return cups

def cups2tsp(msg):
    """Convert cups to teaspoons
    """
    try:
        cups_val = float(msg["amount"])
    except:
        return "Error"
    tsp = round(cups_val * 48, 1)
    return tsp

def tsp2floz(msg):
    """Convert teaspoons to fluid ounces
    """
    try:
        tsp_val = float(msg["amount"])
    except:
        return "Error"
    floz = round(tsp_val / 6, 1)
    return floz

def floz2tsp(msg):
    """Convert fluid ounces to teaspoons
    """
    try:
        floz_val = float(msg["amount"])
    except:
        return "Error"
    tsp = round(floz_val * 6, 1)
    return tsp

#######################################################################################################
# Communication Pipeline
#
#
#######################################################################################################
# Continuous Communication Pipeline
while True:
    message = s.recv(1024)                      # receive message from app (Ingredients App)
    try:
        message = json.loads(message)           # convert serialized json to dictionary
        msg_type = "dict"
    except:
        msg_type = "non_dict"
        message = message.decode()
    print(s_name + ":", message)                # display message from app (Ingredients App)
    if message == "EXIT":                       # exit if the entered message is EXIT
        print("Exiting...")
        break
    elif msg_type != "non_dict":
        if message["from_units"] == message["to_units"]:
            message = str(message["amount"])
            s.send(message.encode())
            print(str(name)+": "+str(message))
        elif message["from_units"] == "tbsp" and message["to_units"] == "tsp":
            message = str(tbsp2tsp(message))
            s.send(message.encode())
            print(str(name)+": "+str(message))
        elif message["from_units"] == "tsp" and message["to_units"] == "tbsp":
            message = str(tsp2tbsp(message))
            s.send(message.encode())
            print(str(name)+": "+str(message))
        elif message["from_units"] == "tsp" and message["to_units"] == "cups":
            message = str(tsp2cups(message))
            s.send(message.encode())
            print(str(name)+": "+str(message))
        elif message["from_units"] == "tsp" and message["to_units"] == "floz":
            message = str(tsp2floz(message))
            s.send(message.encode())
            print(str(name)+": "+str(message))
        elif message["from_units"] == "tbsp" and message["to_units"] == "cups":
            message = str(tbsp2cups(message))
            s.send(message.encode())
            print(str(name)+": "+str(message))
        elif message["from_units"] == "tbsp" and message["to_units"] == "floz":
            message = str(tbsp2floz(message))
            s.send(message.encode())
            print(str(name)+": "+str(message))
        elif message["from_units"] == "cups" and message["to_units"] == "tsp":
            message = str(cups2tsp(message))
            s.send(message.encode())
            print(str(name)+": "+str(message))
        elif message["from_units"] == "cups" and message["to_units"] == "tbsp":
            message = str(cups2tbsp(message))
            s.send(message.encode())
            print(str(name)+": "+str(message))
        elif message["from_units"] == "cups" and message["to_units"] == "floz":
            message = str(cups2floz(message))
            s.send(message.encode())
            print(str(name)+": "+str(message))
        elif message["from_units"] == "floz" and message["to_units"] == "tsp":
            message = str(floz2tsp(message))
            s.send(message.encode())
            print(str(name)+": "+str(message))
        elif message["from_units"] == "floz" and message["to_units"] == "tbsp":
            message = str(floz2tbsp(message))
            s.send(message.encode())
            print(str(name)+": "+str(message))
        elif message["from_units"] == "floz" and message["to_units"] == "cups":
            message = str(floz2cups(message))
            s.send(message.encode())
            print(str(name)+": "+str(message))
    else:
        message = input(str(name+": "))         # user enter message to send
        s.send(message.encode())
    msg_type = ""
    