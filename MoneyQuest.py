import json
import os
import UTILITY
from leveling import display_level
from battles import run_battles
from spend_tracker import run_spend_tracker
from budget import run_budget_setup
from summary import display_spending_summary

#data file path
DATA_FILE = "data/user_data.json"

#define JSON file structure
def create_default_user_data():
    return {
        "net_income": 0,
        "budget": {
            "Needs": {"percentage": 50},
            "Wants": {"percentage": 30},
            "Savings": {"percentage": 20}
        },
        "expenses": [],
        "player": {"name": "Hero", "xp": 0, "level": 1},
        "battles": []
    }

#Save user data
def save_user_data(data, file_path=DATA_FILE):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

#Load/create user data
def load_user_data(file_path=DATA_FILE):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    else:
        print("No existing data found. Creating new save file.")
        return create_default_user_data()

#display Main menu
def home_menu():
    user_data = load_user_data()

    menu_options = [
        "Leveling",
        "Spend Tracker",
        "Budget Setup",
        "Battles",
        "Spending Summary",
        "Save & Exit"
    ]

    while True:
        print("\n[MoneyQuest]")
        print("----------------------------------")
        #reusable code data print
        UTILITY.print_player_info(user_data)
        print("----------------------------------")

        #reusable code menu selector
        choice_idx = UTILITY.select_from_menu(menu_options)
        choice = menu_options[choice_idx]

        if choice == "Leveling":
            display_level(user_data)

        elif choice == "Spend Tracker":
            run_spend_tracker(user_data)

        elif choice == "Budget Setup":
            run_budget_setup(user_data)

        elif choice == "Battles":
            run_battles(user_data)

        elif choice == "Spending Summary":
            display_spending_summary(user_data)

        elif choice == "Save & Exit":
            save_user_data(user_data)
            print("Game saved.")
            break

if __name__ == "__main__":
    home_menu()
