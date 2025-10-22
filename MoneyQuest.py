#This file acts as the home screen for the moneyquest project

import json
import os
import UTILITY
from leveling import display_level
from battles import run_battles
#from spend_tracker import run_spend_tracker
from budget import run_budget_setup
#from summary import display_spending_summary


#data file path
DATA_FILE = "data/user_data.json"

#Define JSON file structure
def create_default_user_data():
    return {
        "net_income": 0,
        "budget": {
            "Needs": {
                "percentage": 50
               # "subcategories": {
               #     "Fixed Expenses": [],
               #     "Variable Expenses": []
               # }
            },
            "Wants": {
                "percentage": 30
               # "subcategories": {
               #     "Leisure": [],
               #     "Subscriptions": []
               # }
            },
            "Savings": {
                "percentage": 20
               # "subcategories": {
              #      "Debt Repayment": [],
              #      "Savings Account": []
              #  }
            }
        },
        "expenses": [],
        "player": {
            "name": "Hero",
            "xp": 0,
            "level": 1
        },
        "battles": []
    }

#save user data
def save_user_data(data, file_path=DATA_FILE):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

#load/create user data
def load_user_data(file_path=DATA_FILE):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
    else:
        print("No existing data found. Creating new save file.")

        return create_default_user_data()


#Display Main menu
def home_menu():
    user_data = load_user_data()

    while True:

        #CLI UI
        print("[MoneyQuest]")
        print("----------------------------------")
        UTILITY.print_player_info(user_data)
        print("----------------------------------")
        print("1. Leveling")
        print("2. Spend Tracker")
        print("3. Budget Setup")
        print("4. Battles")
        print("5. Spending Summary")
        print("6. Save & Exit")

    #Navigate based on user input
        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_level(user_data)

        elif choice == "2":
            #run_spend_tracker(user_data)
            input("Feature in Progress. Press Enter to return.")

        elif choice == "3":
            run_budget_setup(user_data)

        elif choice == "4":
            run_battles(user_data)

        elif choice == "5":
            #display_spending_summary(user_data)
            input("Feature in Progress. Press Enter to return.")

        elif choice == "6":
            save_user_data(user_data)
            print("Game saved.")
            break
        else:
            print("Please select a number from 1 to 6.")
            input("Press Enter to continue...")

#start app
home_menu()
