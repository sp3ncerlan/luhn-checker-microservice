import zmq
from typing import List


def _luhnChecksum(digitsToCheck: List[int]) -> int:
    checkSum = 0
    double = False
    for digit in reversed(digitsToCheck):
        # If pointer is on the digit, double it and check if it is greater than or equal to 10
        if double:
            digit *= 2
            if digit > 9:
                digit -= 9

        # Add to total running sum, and switch the double variable to skip next doubling of the
        # number
        checkSum += digit
        double = not double
    return checkSum


def _listen():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    return socket


def luhnCheckService(cardNumber: str) -> bool:
    digitsToCheck = [int(digit) for digit in cardNumber if digit.isdigit()]
    checkSum = _luhnChecksum(digitsToCheck)
    return checkSum % 10 == 0


def runLuhnCheck():
    socket = _listen()
    print("Luhn Check is running...")

    while True:
        message = socket.recv_string()
        print(f"Input message received: {message}")

        result = luhnCheckService(message)

        socket.send_string("1" if result else "0")


if __name__ == "__main__":
    runLuhnCheck()
