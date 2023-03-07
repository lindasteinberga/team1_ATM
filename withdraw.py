import operations_withdraw as withdraw
print("How much money would you like to withdraw?")
amount = int(input())

print("You withdrew", withdraw.withdraw(amount), "Euros")
