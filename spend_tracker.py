# spend_tracker.py
import UTILITY
from datetime import datetime

#Subcategories for each main category
SUBCATEGORIES = {
    "Needs": ["Rent", "Utilities", "Groceries", "Transportation", "Other Needs"],
    "Wants": ["Dining", "Leisure", "Subscription", "Other Wants"],
    "Savings": ["Emergency Fund", "Debt Repayment", "Investments", "Other Savings"]
}

def run_spend_tracker(user_data):
    print("\n=== Spend Tracker ===")
    UTILITY.print_player_info(user_data)
    print("----------------------------------")

    #Enter net income if not already set
    if user_data.get("net_income", 0) <= 0:
        net_income = UTILITY.get_valid_input(
            "Enter your monthly net income: ",
            input_type=float,
            valid_range=(0.01, float('inf'))
        )
        user_data["net_income"] = net_income

    net_income = user_data["net_income"]
    budget = user_data.get("budget", {})
    needs_budget = net_income * budget.get("Needs", {}).get("percentage", 0) / 100
    wants_budget = net_income * budget.get("Wants", {}).get("percentage", 0) / 100
    savings_budget = net_income * budget.get("Savings", {}).get("percentage", 0) / 100

    while True:
        print("\nYour Monthly Budget Allocation:")
        print(f"Needs: ${needs_budget:.2f}")
        print(f"Wants: ${wants_budget:.2f}")
        print(f"Savings: ${savings_budget:.2f}")

        print("\nWhat would you like to do?")
        print("1. Log an Expense")
        print("2. View Current Expenses")
        print("3. Reset/Archive Expenses & Net Income")
        print("4. Return to Main Menu")

        choice = UTILITY.get_valid_input("Choose an option: ", int, valid_range=(1, 4))

        if choice == 4:
            break

        elif choice == 2:
            expenses = user_data.get("expenses", [])
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("\nCurrent Expenses:")
                for e in expenses:
                    sc = f" ({e['subcategory']})" if e.get("subcategory") else ""
                    print(f"- {e['name']}: ${e['amount']:.2f}{sc}")
            input("\nPress Enter to continue...")

        elif choice == 3:
            confirm = UTILITY.get_valid_input(
                "Archive current expenses and reset net income? (y/n): ",
                str,
                valid_options=["y", "n"]
            )
            if confirm.lower() == "y":
                archive_expenses(user_data)
                user_data["net_income"] = 0
                print("Expenses archived and net income reset.")
            continue

        elif choice == 1:
            expense_name = input("Enter expense name: ").strip()
            amount = UTILITY.get_valid_input(
                "Enter expense amount: ",
                float,
                valid_range=(0.01, float('inf'))  # must be > 0
            )

            #main category selection
            print("\nSelect main category:")
            main_categories = ["Needs", "Wants", "Savings", "None"]
            cat_idx = UTILITY.select_from_menu(main_categories)
            category = main_categories[cat_idx] if cat_idx is not None else "None"

            #subcategory selection
            subcategory = None
            if category != "None":
                print(f"\nSelect subcategory for {category}:")
                subs = SUBCATEGORIES.get(category, [])
                sub_idx = UTILITY.select_from_menu(subs)
                if sub_idx is not None:
                    subcategory = subs[sub_idx]

            expense_entry = {
                "name": expense_name,
                "amount": amount,
                "subcategory": subcategory
            }

            user_data.setdefault("expenses", []).append(expense_entry)
            print(f"Expense '{expense_name}' of ${amount:.2f} recorded under {category} -> {subcategory or 'None'}.")

            #budget overspending check
            total_needs = sum(e["amount"] for e in user_data["expenses"] if e.get("subcategory") in SUBCATEGORIES["Needs"])
            total_wants = sum(e["amount"] for e in user_data["expenses"] if e.get("subcategory") in SUBCATEGORIES["Wants"])
            total_savings = sum(e["amount"] for e in user_data["expenses"] if e.get("subcategory") in SUBCATEGORIES["Savings"])

            for cat, total, budget_amt in [
                ("Needs", total_needs, needs_budget),
                ("Wants", total_wants, wants_budget),
                ("Savings", total_savings, savings_budget)
            ]:
                if total > budget_amt:
                    over_pct = (total - budget_amt) / budget_amt
                    penalty = int(user_data["player"]["xp"] * min(over_pct * 0.2, 0.5))  # Max 50% XP penalty
                    print(f"{cat} budget exceeded by ${total - budget_amt:.2f}! XP penalty: {penalty}")
                    UTILITY.gain_xp(user_data, -penalty)


def archive_expenses(user_data):
    if "expenses" in user_data and user_data["expenses"]:
        archive = user_data.setdefault("expenses_archive", [])
        archive.append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "expenses": user_data["expenses"]
        })
        user_data["expenses"] = []
