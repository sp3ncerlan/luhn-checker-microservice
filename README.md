# luhn-checker-microservice
Microservice that completes a Luhn Algorithm check on inputs.

# How to Request Data

1. Establish ZeroMQ connection to the microservice via REQ socket
2. Send a string through the input stream (in this case, a credit card number)
3. Wait for the response from the microservice to finish parsing the string and use the Luhn Checker function

```
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

cardNumber = "{insert card number here}" # You can manually input, or write a function to extract it from main program
socket.send_string(cardNumber)
```
# How to Receive Data

1. Wait for response using ZeroMQs recv_string() method
2. The microservice will send a "0" for invalid or "1" for valid
3. Utilize this response as needed in the main program

```
response = socket.recv_string()

if response == "1":
  {do something}
else:
  {do something else}
```

# UML Diagram
![Microservice Luhn Checker UML](https://github.com/user-attachments/assets/55e0d9ca-c380-4f21-8ce3-887a3b0d6909)


# Communication Contract

- Communication method: Discord
- Team members are declared non-responsive after 48 hours.
- Once a team member has been declared non-responsive, we can post our concerns in the #need-help channel on Discord so all team members can work together on a backup plan.
- We will post progress updates every 24 hours, but only if relevant; specifically, when work is shared between team members or pertains to the entire group.
- We will host our projects using private GitHub repositories.
- Any repository a team member creates will be shared with the rest of the team so we can learn from each other.
- We will enable code review functionality to help each other improve our programming skills.

