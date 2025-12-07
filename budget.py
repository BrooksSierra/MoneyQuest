import UTILITY

def run_budget_setup(user_data):
    print("\n=== Budget Setup ===")

    budget = user_data.get("budget", {})

    #Get current percentages, defaults to 50,30,20 in user data
    current_needs = budget.get("Needs", {}).get("percentage", 0)
    current_wants = budget.get("Wants", {}).get("percentage", 0)
    current_savings = budget.get("Savings", {}).get("percentage", 0)

    #reusable print data function
    UTILITY.print_player_info(user_data)
    print("----------------------------------")

    #display current strategy
    print("\nCurrent Budget Strategy:")
    print(f"Needs: {current_needs}%")
    print(f"Wants: {current_wants}%")
    print(f"Savings: {current_savings}%")

    menu_options = [
        "Update Budget Percentages",
        "Return to Main Menu"
    ]

    #reusable menu select code
    choice_idx = UTILITY.select_from_menu(menu_options)
    choice = menu_options[choice_idx]

    if choice == "Return to Main Menu":
        print("\nReturning to the main menu.")
        return

    elif choice == "Update Budget Percentages":
        #Resuable input validation code
        needs = UTILITY.get_valid_input(
            prompt="Enter percentage for Needs: ",
            input_type=int,
            min_value=0,
            max_value=100
        )
        #Resuable input validation code
        wants = UTILITY.get_valid_input(
            prompt="Enter percentage for Wants: ",
            input_type=int,
            min_value=0,
            max_value=100
        )
        #Resuable input validation code
        savings = UTILITY.get_valid_input(
            prompt="Enter percentage for Savings: ",
            input_type=int,
            min_value=0,
            max_value=100
        )

        total = needs + wants + savings
        if total != 100:
            print(f"\nPercentages must total 100%. You entered {total}%.")
            input("Press Enter to return to the main menu.")
            return

        #save
        budget["Needs"]["percentage"] = needs
        budget["Wants"]["percentage"] = wants
        budget["Savings"]["percentage"] = savings
        user_data["budget"] = budget

        print("\nBudget updated successfully.")
        input("\nPress Enter to return to the main menu.")
