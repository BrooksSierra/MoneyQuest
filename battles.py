#battles.py

from leveling import calculate_xp_for_next_level
import UTILITY

#battles menu
def run_battles(user_data):

    while True:
        print("\n=== Battles Menu ===")
        UTILITY.print_player_info(user_data)
        print("----------------------------------")
        print("\n1. View your Active Battles")
        print("2. Start a New Battle")
        print("3. Add Progress to a Battle")
        print("4. Return to Main Menu")

#user input navigation
        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_active_battles(user_data)
        elif choice == "2":
            start_new_battle(user_data)
        elif choice == "3":
            update_battle_progress(user_data)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose 1-4.")


#display active goals
#currently also displays completed goals
def display_active_battles(user_data):
    battles = user_data.get("battles", [])
    if not battles:
        print("No active battles found.")
        return

    print("\nActive Battles:")
    for i, battle in enumerate(battles, start=1):
        goal = battle["goal"]
        progress = battle["progress"]
        completed = progress >= goal
        status = "Completed" if completed else "In Progress"
        print(f"{i}. {battle['title']} - {progress}/{goal} saved. [{status}]")

#create new battle
def start_new_battle(user_data):
    title = input("Enter a title for this battle: ").strip()
    try:
        goal = float(input("Enter the savings goal amount: "))
        if goal <= 0:
            print("Goal must be greater than 0.")
            return
    except ValueError:
        print("Invalid amount. Try again.")
        return

#add battle to user data
    new_battle = {
        "title": title,
        "goal": goal,
        "progress": 0,
        "completed": False
    }

    user_data["battles"].append(new_battle)
    print(f"'{title}' started! Save ${goal} to defeat it.")

#Add savings amount to existing battle
def update_battle_progress(user_data):
    battles = user_data.get("battles", [])
    if not battles:
        print("No active battles found.")
        return

#display existing battles
    print("\nWhich battle did you save toward?")
    for i, battle in enumerate(battles, start=1):
        print(f"{i}. {battle['title']} - {battle['progress']}/{battle['goal']} saved")

#user selects existing battle
    try:
        choice = int(input("Enter the number of the battle selection: ")) - 1
        if not (0 <= choice < len(battles)):
            print("Invalid selection.")
            return

#user enters amount
        amount = float(input("How much did you save toward this goal? "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    #update amount
        battles[choice]["progress"] += amount

        #check for completion
        if battles[choice]["progress"] >= battles[choice]["goal"] and not battles[choice]["completed"]:
            print(f"Battle won! '{battle['title']}' was defeated!")
            battles[choice]["completed"] = True

            #50 xp for goal complettion
            gain_xp(user_data, 50)

    except (ValueError, IndexError):
        print("Invalid input. Try again.")

#leveling function to give XP to user
def gain_xp(user_data, amount):
    player = user_data["player"]
    player["xp"] += amount

#determine xp required for next level
    xp_needed = calculate_xp_for_next_level(player["level"])
   #level up as long as there is enough xp
    while player["xp"] >= xp_needed:
        player["xp"] -= xp_needed
        player["level"] += 1
        print(f"Level Up! You are now Level {player['level']}!")
        xp_needed = calculate_xp_for_next_level(player["level"])
