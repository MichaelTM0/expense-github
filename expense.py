# ------------------------------------------
# Expense Tracker
# Author: Michael Murchie
#
# Features:
# - Add Expense
# - View Expenses
# - Search by Category
# - Monthly Summary
# - Save expenses to CSV
#
# Version: 1.0
# ------------------------------------------
import csv
def load_csv(filename):
    expenses = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                expenses.append(row)
        return expenses
    except FileNotFoundError:
        print("No previous expense file found.")
        print("Starting with an empty expense tracker.")
        return []






def add_expense(expenses):
    expense = {}
    while True:
        try:
            expense ["amount"] = float(input("Enter amount: "))
            if expense["amount"] > 0:
                break
            else:
                print("please try again")
        except ValueError:
            print("Amount entered must be positive! Please try again!")
             
    while True:
        print("1. Wants")
        print("2. Needs")
        print("3. Savings")
        print("4. Income")
        
        choice = input("Enter Category(1-4): ")
  
        
        if choice == "1":
            print("You have chosen Wants")
            expense["category"] = "wants"
            break
        elif choice == "2":
            print("You have chosen Needs")
            expense["category"] = "needs"
            break
        elif choice == "3":
            print("You have chosen Savings")
            expense["category"] = "savings"
            break
        elif choice == "4":
            print("You have chosen Income")
            expense["category"] = "income"
            break
        else:
            print("Please enter a valid number!")
        
    expense["store"] = input("Enter Store: ").lower().strip()
    expense["purpose"] = input("What category does this purchase fall under?(Food/transportation/Entertainment/Bills/shopping): ").lower().strip()
    expense["date"] = input("Enter Date: ")

    while True:
        print("1. Debit Card")
        print("2. Credit Card")
        print("3. Cash")
        selection = input("Enter payment Method(1-3)")
        
        
        if selection == "1":
            print("You have chosen Debit Card")
            expense["payment_method"] = "debit card"
            break
        elif selection == "2":
            print("You have chosen Credit Card")
            expense["payment_method"] = "credit card"
            break
        elif selection == "3":
            print("You have chosen Cash")
            expense["payment_method"] = "cash"
            break
        else:
            print("Please enter a valid number!")                                

        
    
    expenses.append(expense)
    print("Expense saved successfully!")
    return expenses
    
    
    
    
def view_expenses(expenses):
    if not expenses:
        print("No expenses available.")
        return
    for row in expenses:
        print(row)

def search_category(expenses):
    while True:
        print("Choose a Category")
        print("1. Needs")
        print("2. Wants")
        print("3. Savings")
        print("4. Income")
    
        selected_category = input("Please Choose a number(1-4): ")

                          
        if selected_category == "1":
            selected_category = "needs"
        elif selected_category == "2":
            selected_category = "wants"
        elif selected_category == "3":
            selected_category = "savings"
        elif selected_category == "4":
            selected_category = "income"
        else:
            print("please enter a valid number!")
            continue
        found = False
        for expense in expenses:
            if expense["category"] == selected_category:
                print(expense)
                found = True
        if not found:
            print("No records at this time!")
            break


def monthly_summary(expenses):
    needs_total = 0
    wants_total = 0
    savings_total = 0
    income_total = 0
    for expense in expenses:
        if expense["category"] == "needs":
            needs_total += float(expense["amount"])
        elif expense["category"] == "wants":
            wants_total += float(expense["amount"])
        elif expense["category"] == "savings":
            savings_total += float(expense["amount"])
        elif expense["category"] == "income":
            income_total += float(expense["amount"])
                
    print("\n" + "=" * 50)
    print("             MONTHLY SUMMARY")
    print("=" * 50)
    print(f"Needs total: ${needs_total:.2f}")
    print(f"Wants total: ${wants_total:.2f}")
    print(f"Savings total: ${savings_total:.2f}")
    print(f"Income total: ${income_total:.2f}")


        
        
        
                          
                          
                          

def save_csv(expenses):
    if not expenses:
        print("No expenses to save!")
        return
    with open("new_expenses.csv", "w", newline ="") as file:
        writer = csv.DictWriter(file, fieldnames = expenses[0].keys())
        
        writer.writeheader()
        
        for expense in expenses:
            writer.writerow(expense)
    print("Expense tracker saved succesfully!")
                    
                    
def main(expenses):
    print("\n" + "=" * 50)
    print("             PERSONAL EXPENSE TRACKER")
    print("=" * 50)
   
    
    while True:
        print("\n" + "="*50)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Monthly Summary")
        print("5. Save and exit")
        print("6. Exit without saving")
        print("="*50)
        
        response = input("Please choose an option (1-6):")
        
        if response == "1":
            add_expense(expenses)
        elif response == "2":
            view_expenses(expenses)
        elif response == "3":
            search_category(expenses)
        elif response == "4":
            monthly_summary(expenses)
        elif response == "5":
            save_csv(expenses)
            print("Goodbye!")
            break
        elif response == "6":
            print("Thanks for using the expense tracker app! Goodbye!")
            break
        else:
            print("Please eneter a valid option!")
        
expenses = load_csv("expenses.csv")
main(expenses)
        