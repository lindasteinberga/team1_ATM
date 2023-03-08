#loan option

loan = int(input("Please enter the amount of EUR you want to loan:    "))
if loan <= 1000:
    print("Selected loan will be transferred to your account soon!")
else:
    print("Unfortunately loan was denied. Please enter smaller amount of EUR. Maximum loan is 1000 EUR.")
