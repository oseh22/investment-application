import sys

def investment():
    try:
        name = input("Please input your name: ")
        amount = int(input("Please input your amount: N"))
    except ValueError:
        print("Invalid input. Please enter a valid integer amount.")
        return
     #this try: function above is a special function that prevent the user from inputing any other data  type that is not Integer for the amount.
    
    welcome_bonus = 0.5  # assuming welcome bonus is 50% which we expressed as a decimal.
    
    bonus_amount = amount * welcome_bonus
    total_amount = amount + bonus_amount
    
    
    print(f"Thank you, {name}! Your initial investment of N{amount} has earned you a welcome bonus of N{bonus_amount} bringing your total investment balance to N{total_amount} ")

    print(f"Total Balance: N{total_amount}")

    print(f"Hello!! {name} you are eligible to withraw any mount from your wallet balance, and 7% VAT will be deducted from every withdrwal you make.")

    request_Withdrawal = input("Would you like to make a withdrawal from your wallet balance? Type yes else type no ")

    if request_Withdrawal == "yes":
        
        print("Request for your withdrawal")
    else:
        print(f"thank you for investing with us {name}.")
        return
    
    Bal = total_amount
    VAT = 0.07  # assuming VAT is 7% expressed as a decimal
    withdrew = int(input("Input amount to withdraw: N"))
    

    if Bal == (withdrew + (withdrew * VAT)) > Bal:
        print("You cannot withdraw up to that amount 7% VAT inclusive.")
    else:
        Bal -= withdrew 
        Bal -= (withdrew * VAT)
        print(f"Successful withdrawal. 7% VAT has been deducted from your wallet balance, current balance now: N{Bal} ")

        print("hello!! we are always here to serve you and to give you the best service. please don't forget to reach out to us whenever you have an issue!!")
        return Bal
    
    if withdrew > Bal :
        print(" Amount Exceed Your Balance.")
        return

investment()