import sys
import sqlite3

#The data from this line to line 16 are used to create a DB called account to allow the code to run. Can be deleted once Sqllite database is set up.
data = [
  {"id": 1,"balance": 550.0},
  {"id": 2,"balance": 320.00},
  {"id": 3,"balance": 8000.00},
  ]

con = sqlite3.connect("atmPython.db")
cur = con.cursor()
cur.executemany("INSERT INTO account VALUES(:id,:balance)", data)
con.close()


#Below are defined variables for while loops
stop = 0
accountSelect = 0

#While loops defined by variable stop and account select to allow consumers to complete multiple transactions. userID defines the users account theyve chosen to interact with
while accountSelect == 0:
  userID = input ("Please enter your account number.\n\n")
  while stop == 0:

#The three def functions below have return functions in which return outputs according to their names
    def printbalance(account_balance):
      print("Your current balance:")
      return ("{:.2f}".format(account_balance))

    def deposit(balance , deposit):
      return ("Deposit was $" + str("{:.2f}".format(deposit_amount)) + ", current balance is $" + str("{:.2f}".format(balance + deposit)))

    def withdraw(balance,withdraw):
      return ("Withdrawal amount was $" + str("{:.2f}".format(withdraw_amount))+ ", current balance is $" + str("{:.2f}".format(balance - withdraw)))

    con = sqlite3.connect("atmPython.db")
    cur = con.cursor()
    userchoice = input ("\nWhat would you like to do? (D) for deposit, (W) for withdraw, (B) for Balance, and (Q) for Quit.\n\n")

#Below is the Deposit Option and user input amount
    if (userchoice == 'D' or userchoice == 'd'):
      deposit_amount = float(input("How much would you like to deposit today?\n\n"))
#Below is the selection and conversion of data from the account DB for deposit 
      cur.execute("SELECT balance FROM account")
      account_balance = float('.'.join(str(elem) for elem in cur.fetchall()[int(userID) - 1]))
#Below is use of deposit function 
      print(deposit(account_balance,deposit_amount))
      account_balance = account_balance + deposit_amount
#Below is the UPDATE of account balance in the DB
      cur.execute("UPDATE account SET balance=? WHERE id=?", (account_balance,int(userID)))
      con.commit()
      cur.close()
    
    elif (userchoice == 'B' or userchoice == 'b'):
      cur.execute("SELECT balance FROM account")
      account_balance = float('.'.join(str(elem) for elem in cur.fetchall()[int(userID) - 1]))
      print(account_balance)
#Below is the Withdraw Option
  
    elif (userchoice == 'W' or userchoice == 'w'):
      withdraw_amount = float(input("How much would you like to withdraw today?\n\n"))
      
#Below is the selection and conversion of data from the account DB for deposit 
      cur.execute("SELECT balance FROM account")
      account_balance = float('.'.join(str(elem) for elem in cur.fetchall()[int(userID) - 1]))
      
#Below is a if statement that allows user to withdraw if the funds are sufficient     
      if withdraw_amount <= account_balance:
        print(withdraw(account_balance,withdraw_amount))
        account_balance = account_balance - withdraw_amount
        
#Below is the UPDATE of account balance in the DB
        cur.execute("UPDATE account SET balance=? WHERE id=?", (account_balance,int(userID)))
        con.commit()
        cur.close()
#Below is a elif statement to determine if the account has sufficient funds        
      elif withdraw_amount >= account_balance:
        print("$" + str("{:.2f}".format(withdraw_amount)) + " is greater than your account balance of " + "$" + str("{:.2f}".format(account_balance)))

#Below is the Quit Option to return to the account select screen
    
    elif (userchoice == 'Q' or userchoice == 'q'):
      stop = 1
      print("Thank you for banking with us.\n")

