# Ingredient App Simulator.py

# The Ingredients in Season application will set up the socket connection and listen for a microservice connection.
# Once a microservice is connected, the Ingredients application sends an encoded request to the microservice.
# The microservice will respond, and the Ingredients app will receive the message.

import time, socket, sys
import json

print("Initializing....\n")
time.sleep(1)

s = socket.socket()
host = 'localhost'                      # specify host
port = 1234                             # specify port
s.bind((host, port))                    # associate socket with host and port
name = "Ingredients App"

print("Listening on:", host, "on port:", port)
s.listen(1)                             # listens for connections from microservices
conn, addr = s.accept()                 # accept microservice connection to establish connection
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)                # receive microservice name
s_name = s_name.decode()                # store name of microservice for ease of identification
print("Type EXIT to quit")
conn.send(name.encode())                # send app name

#######################################################################################################
# example messages
#
#
#######################################################################################################
example_message1 = {
    "amount": 1,
    "from_units": "tbsp",
    "to_units": "tsp"
}

example_message2 = {
    "amount": 4,
    "from_units": "tbsp",
    "to_units": "tsp"
}

example_message3 = {
    "amount": 9,
    "from_units": "tsp",
    "to_units": "tbsp"
}

example_message4 = {
    "amount": 7,
    "from_units": "tsp",
    "to_units": "tbsp"
}

example_message5 = {
    "amount": 5,
    "from_units": "tsp",
    "to_units": "tbsp"
}

example_message6 = {
    "amount": 35,
    "from_units": "tsp",
    "to_units": "cups"
}

example_message7 = {
    "amount": 35,
    "from_units": "tsp",
    "to_units": "floz"
}

example_message8 = {
    "amount": 4,
    "from_units": "cups",
    "to_units": "floz"
}

example_message9 = {
    "amount": 4,
    "from_units": "floz",
    "to_units": "tsp"
}

example_message10 = {
    "amount": 4,
    "from_units": "tsp",
    "to_units": "tsp"
}


#######################################################################################################
# Communication Pipeline
#
#
#######################################################################################################
# Continuous Communication Pipeline
while True:
    message = input(str(name+": "))
    if message == "EXIT":               # exit if the message is EXIT
        conn.send(message.encode())
        print("Exiting...\n")
        break
    elif message == "example1":
        serialized_dict = json.dumps(example_message1)
        message = serialized_dict
    elif message == "example2":
        serialized_dict = json.dumps(example_message2)
        message = serialized_dict
    elif message == "example3":
        serialized_dict = json.dumps(example_message3)
        message = serialized_dict
    elif message == "example4":
        serialized_dict = json.dumps(example_message4)
        message = serialized_dict
    elif message == "example5":
        serialized_dict = json.dumps(example_message5)
        message = serialized_dict
    elif message == "example6":
        serialized_dict = json.dumps(example_message6)
        message = serialized_dict
    elif message == "example7":
        serialized_dict = json.dumps(example_message7)
        message = serialized_dict
    elif message == "example8":
        serialized_dict = json.dumps(example_message8)
        message = serialized_dict
    elif message == "example9":
        serialized_dict = json.dumps(example_message9)
        message = serialized_dict
    elif message == "example10":
        serialized_dict = json.dumps(example_message10)
        message = serialized_dict
    conn.send(message.encode())         # send app message
    message = conn.recv(1024)           # receive message from microservice
    message = message.decode()
    print(s_name + ":", message)        # display message from microservice
