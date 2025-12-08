import UTILITY

#map categories
CATEGORY_MAP = {
    "Needs": ["needs", "fixed", "variable", "rent", "utilities", "groceries"],
    "Wants": ["wants", "leisure", "subscription", "entertainment", "dining"],
    "Savings": ["savings", "debt", "savings account", "debt repayment", "emergency fund"]
}

def display_spending_summary(user_data):
    menu_options = [
        "View Current Summary",
        "View Archived Expenses",
        "Return to Main Menu"
    ]

    while True:
        print("\n=== Spending Summary ===")
        #reusable code data print
        UTILITY.print_player_info(user_data)
        print("----------------------------------")

        #reusable code menu selector
        choice_idx = UTILITY.select_from_menu(menu_options)
        choice = menu_options[choice_idx]

        if choice == "Return to Main Menu":
            break
        elif choice == "View Current Summary":
            display_expenses(user_data.get("expenses", []))
        elif choice == "View Archived Expenses":
            display_archive(user_data.get("expenses_archive", []))

#print expenses to player if exists
def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        input("\nPress Enter to return...")
        return

    category_totals = {key: 0 for key in CATEGORY_MAP.keys()}
    overall_total = 0

#expenses list
    print("\nExpenses:")
    for e in expenses:
        name = e.get("name", "Unknown")
        amount = e.get("amount", 0)
        subcategory = e.get("subcategory", "None") or "None"
        category = "Uncategorized"

        #determines category with mapped keywords, uncategorized if no match
        if subcategory.lower() != "none":
            for cat, keywords in CATEGORY_MAP.items():
                if any(keyword in subcategory.lower() for keyword in keywords):
                    category = cat
                    break

        print(f"- {name}: ${amount:.2f} | Subcategory: {subcategory} | Category: {category}")

        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += amount
        overall_total += amount

    #show distribution over categories
    print("\nCategory Summary:")
    for cat, total in category_totals.items():
        pct = (total / overall_total * 100) if overall_total > 0 else 0
        print(f"{cat}: ${total:.2f} ({pct:.1f}% of total spending)")

    print(f"\nTotal Spending: ${overall_total:.2f}")
    input("\nPress Enter to return...")

#archived expenses list
def display_archive(archive_list):
    if not archive_list:
        print("No archived data.")
        input("\nPress Enter to return...")
        return


    print("\nArchived Dates:")
    for i, entry in enumerate(archive_list, start=1):
        print(f"{i}. {entry['date']}")

    #reusable input validation
    choice = UTILITY.get_valid_input(
        prompt="Select a date to view archived expenses: ",
        input_type=int,
        valid_range=(1, len(archive_list))
    ) - 1

    display_expenses(archive_list[choice].get("expenses", []))
