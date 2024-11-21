import zmq

def luhnCheckService(cardNumber: str) -> bool:
    # Conversion of the string "cardNumber" to a list of numbers to work with
    digitsToCheck = [int(digit) for digit in cardNumber if digit.isdigit()]

    # checkSum is the total sum of the digits, double is a pointer to only double every other number in the list
    checkSum = 0
    double = False

    # Reverse the list which is required to iterate from back to front
    for digit in reversed(digitsToCheck):
        # If pointer is on the digit, double it and check if it is greater than or equal to 10
        if double:
            digit *= 2
            if digit > 9:
                digit -= 9
        
        # Add to total running sum, and switch the double variable to skip next doubling of the number
        checkSum += digit
        double = not double
    
    # Return true or false depending on if no remainder after dividing by 10 (Luhn's Algorithm)
    return checkSum % 10 == 0

def runLuhnCheck():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("Luhn Check is running...")

    while True:
        message = socket.recv_string()
        print(f"Input message received: {message}")

        result = luhnCheckService(message)

        # The true or false from the check above results in "1" or "0", which is sent over
        socket.send_string("1" if result else "0")

if __name__ == "__main__":
    runLuhnCheck()
