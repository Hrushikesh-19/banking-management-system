import json
import os

# Create files if they don't exist
if not os.path.exists("accounts.json"):
    with open("accounts.json", "w") as f:
        json.dump({}, f)

if not os.path.exists("transactions.json"):
    with open("transactions.json", "w") as f:
        json.dump([], f)


def load_accounts():
    with open("accounts.json", "r") as f:
        return json.load(f)


def save_accounts(accounts):
    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4)


def load_transactions():
    with open("transactions.json", "r") as f:
        return json.load(f)


def save_transactions(transactions):
    with open("transactions.json", "w") as f:
        json.dump(transactions, f, indent=4)


while True:

    print("\n====================================")
    print("     BANKING MANAGEMENT SYSTEM")
    print("====================================")

    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    accounts = load_accounts()
    transactions = load_transactions()

    # ------------------------
    # CREATE ACCOUNT
    # ------------------------
    if choice == "1":

        account_no = input("Enter Account Number: ")

        if account_no in accounts:
            print("Account already exists.")
            continue

        name = input("Enter Customer Name: ")
        balance = float(input("Enter Initial Deposit: $"))

        accounts[account_no] = {
            "name": name,
            "balance": balance
        }

        save_accounts(accounts)

        transactions.append({
            "account": account_no,
            "type": "Account Created",
            "amount": balance
        })

        save_transactions(transactions)

        print("\nAccount Created Successfully!")

    # ------------------------
    # DEPOSIT
    # ------------------------
    elif choice == "2":

        account_no = input("Enter Account Number: ")

        if account_no not in accounts:
            print("Account Not Found")
            continue

        amount = float(input("Enter Deposit Amount: $"))

        accounts[account_no]["balance"] += amount

        save_accounts(accounts)

        transactions.append({
            "account": account_no,
            "type": "Deposit",
            "amount": amount
        })

        save_transactions(transactions)

        print("Money Deposited Successfully.")
        print("Current Balance: $", accounts[account_no]["balance"])

    # ------------------------
    # WITHDRAW
    # ------------------------
    elif choice == "3":

        account_no = input("Enter Account Number: ")

        if account_no not in accounts:
            print("Account Not Found")
            continue

        amount = float(input("Enter Withdrawal Amount: $"))

        if amount > accounts[account_no]["balance"]:
            print("Insufficient Balance")
        else:
            accounts[account_no]["balance"] -= amount

            save_accounts(accounts)

            transactions.append({
                "account": account_no,
                "type": "Withdraw",
                "amount": amount
            })

            save_transactions(transactions)

            print("Withdrawal Successful.")
            print("Current Balance: $", accounts[account_no]["balance"])

    # ------------------------
    # CHECK BALANCE
    # ------------------------
    elif choice == "4":

        account_no = input("Enter Account Number: ")

        if account_no not in accounts:
            print("Account Not Found")
        else:
            print("\nCustomer Name :", accounts[account_no]["name"])
            print("Balance : $", accounts[account_no]["balance"])

    # ------------------------
    # TRANSACTION HISTORY
    # ------------------------
    elif choice == "5":

        account_no = input("Enter Account Number: ")

        found = False

        print("\nTransaction History\n")

        for t in transactions:
            if t["account"] == account_no:
                print(
                    f'{t["type"]} - ${t["amount"]}'
                )
                found = True

        if not found:
            print("No Transactions Found")

    # ------------------------
    # EXIT
    # ------------------------
    elif choice == "6":
        print("\nThank You for Using Banking Management System!")
        break

    else:
        print("Invalid Choice")
