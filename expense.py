expenses = []

def add_expense():
    name = input("Enter expense name: ")
    
    try:
        amount = float(input("Enter amount: "))
    except:
        print("Invalid amount ❌")
        return

    expenses.append({"name": name, "amount": amount})
    print("Expense added ✅")


def view_expenses():
    if not expenses:
        print("No expenses found ❌")
        return

    print("\n📋 Expense List:")
    total = 0

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ₹{expense['amount']}")
        total += expense['amount']

    print(f"\n💰 Total Expense: ₹{total}")


def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        index = int(input("Enter expense number to delete: ")) - 1

        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            print(f"{removed['name']} deleted ✅")
        else:
            print("Invalid number ❌")

    except:
        print("Invalid input ❌")


while True:
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        print("Exiting... 👋")
        break

    else:
        print("Invalid choice ❌")