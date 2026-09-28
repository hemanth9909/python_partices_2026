balance=50000
def withdraw(balance):
    amount=int(input("enter the amount:"))
    if amount > balance:
        print("insufficent balance")
    else:
        balance = balance - amount
        print(amount)
    return balance

while True:
    print("1.withdraw")
    print("2.credit")
    print("3.ministatement")
    print("4.exit")

    choice = input("enter your choice:")
    if choice =="1":
        balance = withdraw(balance)
    elif choice =="2":
        amount=int(input("enter the amount:"))
        balance += amount
        print("enter balance:",balance)
    elif choice == "3":
        print("mini statement",balance)
        
    else:
        print("exit")
    break









