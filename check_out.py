"""check out from atm"""

info = "Available ATM services: "
print(info)


def service_choice(services):
    for service in services:
        print(service)


services_list = ("1 - Balance service", "2 - Withdraw service", "3 - Deposit service", "4 - Exit service")
service_choice(services_list)

service_list = int(input("\nPlease, choose your service by entering number: "))
if service_list == 1:
    print("Balance service")
elif service_list == 2:
    print("Withdraw service")
elif service_list == 3:
    print("Deposit service")
else:
    print("\nExit service")
    print("Please, take out your credit card!!!")
    print("Thank you for using ATM !!!")
