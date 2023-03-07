""" verify if pin is valid. create 3 inputs."""

def verify_pin(pin):
    if pin == "1234":
        return True
    else:
        return False

greeting = "Welcome to our atm service!!"
print(greeting.upper())

greeting = "you have 3 attempts to enter your pin code.\n"
print(greeting.upper())


tries = 0
while tries < 3:
    pin = input("Please enter your PIN code: ")
    if verify_pin(pin):
        print("PIN code is correct!!")
        break
    else:
        print("PIN code is incorrect.")
    tries +=1
print(('\nThank you for choosing our atm services!!!').upper())