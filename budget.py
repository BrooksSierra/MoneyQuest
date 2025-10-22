#budget.py

import UTILITY


def run_budget_setup(user_data):
    print("\n=== Budget Setup ===")

    budget = user_data.get("budget", {})

    #Get current percentages, defaults to 50,30,20 in user data
    current_needs = budget.get("Needs", {}).get("percentage", 0)
    current_wants = budget.get("Wants", {}).get("percentage", 0)
    current_savings = budget.get("Savings", {}).get("percentage", 0)

    UTILITY.print_player_info(user_data)
    print("----------------------------------")

    #Display current strategy
    print("\nCurrent Budget Strategy:")
    print(f"Needs: {current_needs}%")
    print(f"Wants: {current_wants}%")
    print(f"Savings: {current_savings}%")

    print("\nWhat would you like to do?")
    print("1. Update Budget Percentages")
    print("2. Return to Main Menu")

    choice = input("Choose an option: ").strip()

    if choice == "2":
        print("\nReturning to the main menu.")
        return

    elif choice == "1":
        try:
            needs = int(input("Enter percentage for Needs: "))
            wants = int(input("Enter percentage for Wants: "))
            savings = int(input("Enter percentage for Savings: "))

            total = needs + wants + savings
            if total != 100:
                print(f"\n Percentages must total 100%. You entered {total}%.")
                input("Press Enter to return to the main menu.")
                return

            #save updates
            budget["Needs"]["percentage"] = needs
            budget["Wants"]["percentage"] = wants
            budget["Savings"]["percentage"] = savings
            user_data["budget"] = budget

            print("\nBudget updated successfully.")
            input("\nPress Enter to return to the main menu.")

        except ValueError:
            print("Invalid input. Please enter whole numbers.")

    else:
        print("Invalid selection. Returning to the main menu.")

