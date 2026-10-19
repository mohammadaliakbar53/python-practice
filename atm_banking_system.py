balance=50000
name="Mohammad"
pin=5253
attempt=1
login_successfull=False
while True:
    username=input("enter your username").title()
    if(username==name):
        break
    else:
        print("Incorrect Username! Try Again")
        continue
while True:
    passcode=int(input("Enter your 4 digit code:"))
    if(passcode==pin):
        print("Login Successfull\nWelcome", name)
        login_successfull=True
        break
    else:
        if(attempt==3):
            print("you're out of attempts")
            break
        print("Try Again")
        attempt=attempt+1
        continue

if login_successfull:
    while True:
        type=int(input("Enter transaction type\n1> check balance\n2> deposit\n3> withdraw\n4> Exit\n"))
        if(type==1):
            print(f"your balance is {balance}")
            continue
        elif(type==2):
            deposit=int(input("Enter deposit amount:"))
            if(deposit>0):
                balance=balance+deposit
                print("Transaction Successfull\nYour New Balance Is", balance)
            else:
                print("Invalid Deposit Amount")
            continue
        elif(type==3):
            withdraw=int(input("enter amount you want to withdraw:"))
            if(withdraw>balance):
                print("Insufficient Balance")
            else:
                balance=balance-withdraw
                print("Transaction Successfull\nYour new balance is", balance)
            continue
        elif(type==4):
            print("thankyou for using our services")
            break
        else:
            print("Invalid Transaction Type")
