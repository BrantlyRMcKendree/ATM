import sys

account_balance = float(500.25)

# The three def functions below have return functions in which return correct outputs.

stop = 0

# A while loop defined by variable stop to allow consumer to complete multiple transactions.

while stop == 0:
  
  def printbalance(account_balance):
    print("Your current balance:")
    return ("{:.2f}".format(account_balance))


  def deposit(balance , deposit):
    return ("Deposit was $" + str("{:.2f}".format(deposit_amount)) + ", current balance is $" + str("{:.2f}".format(balance + deposit)))
    


  def withdraw(balance,withdraw):
    return ("Withdrawal amount was $" + str("{:.2f}".format(withdraw_amount))+ ", current balance is $" + str("{:.2f}".format(balance - withdraw)))


  userchoice = input ("What would you like to do? (D) for deposit, (W) for withdraw, (B) for Balance, and (Q) for Quit.\n")

#Below is the Deposit Option
  if (userchoice == 'D' or userchoice == 'd'):
    deposit_amount = float(input("How much would you like to deposit today?\n"))  
    print(deposit(account_balance,deposit_amount))
    account_balance = account_balance + deposit_amount
    
  elif (userchoice == 'B' or userchoice == 'b'):
    print(printbalance(account_balance))
  
#Below is the Withdraw Option
  
  elif (userchoice == 'W' or userchoice == 'w'):
    withdraw_amount = float(input("How much would you like to withdraw today?\n"))
    
    if withdraw_amount <= account_balance:
      print(withdraw(account_balance,withdraw_amount))
      account_balance = account_balance - withdraw_amount
      
    elif withdraw_amount >= account_balance:
      print("$" + str("{:.2f}".format(withdraw_amount)) + " is greater than your account balance of " + "$" + str("{:.2f}".format(account_balance)))

#Below is the Quit Option
    
  elif (userchoice == 'Q' or userchoice == 'q'):
    stop = 1
    print("Thank you for banking with us.")
