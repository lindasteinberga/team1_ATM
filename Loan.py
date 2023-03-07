import interface as itf
import operations as op

response = input("Please select from the following options: \nWithdraw_(W) \nDeposit_(D) \nBalance_(B) \nLoan_(L) \nQuit_(Q) \n Receipt_(R) Choose one letter: ").lower()
valid_response = ["w", "d", "b", "l", "q", "r"]
response = response.lower()
    if response == "l":
        print("By selecting loan you confirm that you understand and accept "Terms & Comditions"")
        loan = int(input("\n 100\n 200\n 500\n Select the amount in Euros you want to loan"))
            if loan == 100:
                 print(f"You selected 100 EUR loan. This amount of EUR will be added to your account soon.")
            if loan == 200:
                print(f"You selected 200 EUR loan. This amount of EUR will be added to your account soon.")
            if loan == 500:
                print(f"You selected 500 EUR loan. This amount of EUR will be added to your account soon.")
            else:
                print("Try again")
