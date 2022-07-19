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

# example message
example_message = {
    "amount": 1,
    "from_units": "tbsp",
    "to_units": "tsp"
}

# Continuous Communication Pipeline
while True:
    message = input(str(name+": "))
    if message == "EXIT":               # exit if the message is EXIT
        conn.send(message.encode())
        print("Exiting...\n")
        break
    elif message == "example":
        serialized_dict = json.dumps(example_message)
        message = serialized_dict
    conn.send(message.encode())         # send app message
    message = conn.recv(1024)           # receive message from microservice
    message = message.decode()
    print(s_name + ":", message)        # display message from microservice
