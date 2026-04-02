# Personal Expense Tracker Project

expenses = []  # list of user's expenses

# function to add expenses to list for OPTION 1
def add_expense():
    category = input("Enter Expense Category: ").strip()
    
    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid Amount. Please Enter a Number.\n")
        return

    expense = {
        "category": category,
        "amount": amount
    }
    expenses.append(expense)
    print("Expense Added Successfully!\n")

# function to total expense OPTION 2
def total_spent():
    if not expenses:
        print("No Expenses Recorded Yet.\n")
        return

    total = sum(exp["amount"] for exp in expenses)
    print(f"Total Amount Spent: ₹{total}\n")

#function to view the highest recorded expense OPTION 3
def highest_expense():
    if not expenses:
        print("No Expenses Recorded Yet.\n")
        return

    highest = max(expenses, key=lambda x: x["amount"])
    print("Highest Expense:")
    print(f"Category: {highest['category']}, Amount: ₹{highest['amount']}\n")

#function to view the lowest recorded expense OPTION 4
def lowest_expense():
    if not expenses:
        print("No Expenses Recorded Yet.\n")
        return

    lowest = min(expenses, key=lambda x: x["amount"])
    print("Lowest Expense:")
    print(f"Category: {lowest['category']}, Amount: ₹{lowest['amount']}\n")
    

# function to view Expenses by Category OPTION 5
def view_by_category():
    if not expenses:
        print("No Expenses Recorded Yet.\n")
        return

    category = input("Enter Category to View: ").strip()
    found = False

    print(f"Expenses in category '{category}':")
    for exp in expenses:
        if exp["category"].lower() == category.lower():
            print(f"₹{exp['amount']}")
            found = True

    if not found:
        print("No expenses found in this category.")
    print()

#function to show all expenses OPTION 6
def show_all_expenses():
    if not expenses:
        print("No Expenses to Show.\n")
        return

    print("All Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['category']} - ₹{exp['amount']}")
    print()


# Program Options
while True:
    print("---- Welcome to Your Personal Expense Tracker ----")
    print("              Spend Your Money Wisely     ")
    print("1. Add Expense")
    print("2. View Total Spent")
    print("3. View Highest Expense")
    print("4. View Lowest Expense")
    print("5. View Expenses by Category")
    print("6. Show All Expenses")
    print("7. Exit")

    choice = input("Enter Your Choice (1-7): ").strip()

    if choice == "1":
        add_expense()
    elif choice == "2":
        total_spent()
    elif choice == "3":
        highest_expense()
    elif choice == "4":
        lowest_expense()
    elif choice == "5":
        view_by_category()
    elif choice == "6":
        show_all_expenses()
    elif choice == "7":
        print("Thank you for using Expense Tracker!")
        break # To stop the program is user wants to exit
    else:
        print("Invalid Choice. Please Try Again.\n")