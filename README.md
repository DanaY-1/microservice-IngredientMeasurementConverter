# microservice-IngredientMeasurementConverter
Microservice to the Ingredients in Season Application

A simulated Ingredients application is provided to test socket communication. The simulated Ingredients app
sets up the socket connection and listens for the microservice. The microservice connects to the socket and
sends the microservice name. The simulated Ingredients app can send requests to the microservice and will 
respond.

Requests from the Ingredients app are sent as a stringified dictionary.
The dictionary request should be in the format below:
request = {
    "amount": 1,
    "from_units": "tbsp",
    "to_units": "tsp"
}
Example requests (numbered 1-10) are provided for testing purposes.

How to Run:
1. Start IngredientApp_Simulator.py
2. Start microservice_MeasurementConverter.py
3. Send requests from IngredientApp_Simulator.py to get converted value.
    Example requests are provided for testing purposes.
    User can simply enter "example1" and the example_message1 dictionary will be sent (stringified)
4. Type EXIT to close simulator and microservice
