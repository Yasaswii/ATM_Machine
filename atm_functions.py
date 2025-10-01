def get_account(accounts,name,pin):
    for account in accounts:
        if account["name"].lower() == name.lower() and account["pin"] == pin:
            return account
    
def check_balance(accounts, name, pin):
    account = get_account(accounts, name, pin)
    if account:
        print(f"Account Holder: {account['name']}")
        print(f"Current Balance: ₹{account['balance']}")
    else:
        print(" Invalid name or PIN ")

def deposit(accounts,name,pin,amount):
    account=get_account(accounts,name,pin)
    if account:
        account["balance"]+=amount
        account["transactions"].append(amount)
        print(f"{amount}deposited successfully")
    else:
        print("Invalid name or pin")

def withdraw(accounts,name,pin,amount):
    account=get_account(accounts,name,pin)
    if account:
        if account["balance"]>=amount:
            account["balance"]-=amount
            account["transactions"].append(amount)
            print(f"{amount}withdrawn successfully")
        else:
            print("Insufficient Balance")
def transaction_history(accounts, name, pin):
    account = get_account(accounts, name, pin)
    if account:
        print(f"Transaction History for {account['name']}:")
        if account["transactions"]:
            for t in account["transactions"]:
                print(f"- {t}")
        else:
            print("No transactions found.")
        print()
    else:
        print(" Invalid name or PIN")


        









        
