import UTILITY

#battles menu
def run_battles(user_data):
    while True:
        print("\n=== Battles Menu ===")
        #resuable data print code
        UTILITY.print_player_info(user_data)
        print("----------------------------------")

        menu_options = [
            "View your Active Battles",
            "Start a New Battle",
            "Add Progress to a Battle",
            "Return to Main Menu"
        ]
        #reusable menu select code
        choice_idx = UTILITY.select_from_menu(menu_options)
        choice = menu_options[choice_idx]

        if choice == "View your Active Battles":
            display_active_battles(user_data)
        elif choice == "Start a New Battle":
            start_new_battle(user_data)
        elif choice == "Add Progress to a Battle":
            update_battle_progress(user_data)
        elif choice == "Return to Main Menu":
            break

#Display active battles
def display_active_battles(user_data):
    battles = user_data.get("battles", [])
    if not battles:
        print("No active battles found.")
        input("\nPress Enter to return...")
        return

    print("\nActive Battles:")
    for i, battle in enumerate(battles, start=1):
        goal = battle["goal"]
        progress = battle["progress"]
        completed = battle.get("completed", False)
        status = "Completed" if completed else "In Progress"
        print(f"{i}. {battle['title']} - {progress}/{goal} saved. [{status}]")
    input("\nPress Enter to return...")

#create new battle
def start_new_battle(user_data):
    title = input("Enter a title for this battle: ").strip()
    #Resuable input validation code
    goal = UTILITY.get_valid_input(
        prompt="Enter the savings goal amount: ",
        input_type=float,
        valid_range=(0.01, float('inf'))
    )

    new_battle = {
        "title": title,
        "goal": goal,
        "progress": 0,
        "completed": False
    }

    user_data["battles"].append(new_battle)
    print(f"'{title}' started! Save ${goal} to defeat it.")
    input("\nPress Enter to return...")

#add savings amount to existing battle
def update_battle_progress(user_data):
    battles = user_data.get("battles", [])
    if not battles:
        print("No active battles found.")
        input("\nPress Enter to return...")
        return

    print("\nWhich battle did you save toward?")
    for i, battle in enumerate(battles, start=1):
        print(f"{i}. {battle['title']} - {battle['progress']}/{battle['goal']} saved")

    #Resuable input validation code
    choice_idx = UTILITY.get_valid_input(
        prompt="Enter the number of the battle selection: ",
        input_type=int,
        valid_range=(1, len(battles))
    ) - 1

    #resuable input validation code
    amount = UTILITY.get_valid_input(
        prompt="How much did you save toward this goal? ",
        input_type=float,
        valid_range=(0.01, float('inf'))
    )

    battles[choice_idx]["progress"] += amount

    #gain XP for contributing to the battle
    contribution_xp = max(1, int(10 * (amount / battles[choice_idx]["goal"])))
    #reusable user XP gain code
    UTILITY.gain_xp(user_data, contribution_xp)
    print(f"You gained {contribution_xp} XP for your contribution!")

    #check for completion
    if battles[choice_idx]["progress"] >= battles[choice_idx]["goal"] and not battles[choice_idx]["completed"]:
        print(f"Battle won! '{battles[choice_idx]['title']}' was defeated!")
        battles[choice_idx]["completed"] = True

        # reusable user XP gain code
        #100 XP for goal completion
        UTILITY.gain_xp(user_data, 100)

    input("\nPress Enter to return...")