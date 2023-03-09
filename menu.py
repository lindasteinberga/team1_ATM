#Navigating through the functions

import balance_display
import check_out
import deposit
import loan_on_the_spot
import withdraw
import print_receipt

hello = "Hello"
print(hello)

def menu():
    print("(1) option 1")
    print("(2) option 2")
    print("(3) option 3")
    print("(4) option 4")
    print("(5) option 5")
    print("(6) option 6")

    menu()
    option = int(input("Enter your option:  "))

    while option != 0:
        if option == 1:
            print("Option 1 has been called")
            balance_display.balance()
        elif option == 2:
            print("Option 2 has been called")
            withdraw.withdraw()
        elif option == 3:
            option3()
            print("Option 3 has been called")
            deposit.deposit()
        elif option == 4:
            option4()
            loan_on_the_spot.loan_on_the_spot()
        elif option == 5:
            option5()
            print_receipt.atm_receipt()
        elif option == 6:
            option5()
            check_out.service_choice()
        else:
            print("Invalid option")



print("Thank you for choosing this ATM")








