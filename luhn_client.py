import zmq

def luhnServiceTester():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    testCard = "4532015112830367"
    print(f"Test input sent: {testCard}")
    socket.send_string(testCard)

    result = socket.recv_string()
    print(f"Received from luhn checker: {result} ('0' means invalid, '1' means valid)")

if __name__ == "__main__":
    luhnServiceTester()