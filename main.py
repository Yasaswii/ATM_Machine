from accounts import accounts
from atm_functions import check_balance, deposit, withdraw, transaction_history
def menu():
    while True:
        print("ATM Machine")
        print("1.Check balance")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Transaction History")
        print("5.Exit")
        choice=input("Enter your choice (1-5):")
        name=input("enter your name:")
        pin=int(input("enter your pin:"))
        if choice=="1":
            check_balance(accounts,name,pin)
        elif choice=="2":
            amount=float(input("enter amount to deposit:"))
            deposit(accounts,name,pin,amount)
        elif choice=="3":
            amount=float(input("enter amount to withdraw:"))
            withdraw(accounts,name,pin,amount)
        elif choice == "4":
            transaction_history(accounts, name, pin)
        elif choice=="5":
            print("Thank you ")
            break
        else:
            print(" Invalid option. Please try again")
if __name__ == "__main__":
    menu()





