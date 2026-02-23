balance = 0

def deposit(amount):
    global balance
    balance += amount
    print(f"Amount Deposited: {amount}")
    print(f"Current Balance: {balance}")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance -= amount
        print(f"Amount Withdrawn: {amount}")
        print(f"Current Balance: {balance}")

def check_balance():
    print(f"Current Balance: {balance}")

while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)

    elif choice == 3:
        check_balance()

    elif choice == 4:
        print("Exit successfully.")
        break

    else:
        print("Invalid choice")