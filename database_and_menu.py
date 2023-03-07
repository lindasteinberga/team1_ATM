import string
import os
import int



#Creating database, adding new client with a pin and balance statements

client = ["client1", "client2", "client3"]
pin = ["1234", "2345", "3456"]
balance = [1000, 500, 250]
count = 0

#Creating function with a single new client
def client(client1, pin, balance =0):
    client1.pin = pin
    client1.balance = balance


#Listing ATM meniu

response = input("Please select from the following options: \nWithdraw_(W) \nDeposit_(D) \nBalance_(B) \nLoan_(L) \nQuit_(Q) \n Receipt_(R) Choose one letter: ").lower()
    valid_response = ["w", "d", "b", "l", "q", "r"]
    response = response.lower()
    if response == "b":
        print(f"Your balance is: ", balance, "EUR")
    elif response == "w":
        print ==
    elif response == "d":
