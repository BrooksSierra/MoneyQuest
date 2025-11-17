#UTILITY.py
from datetime import datetime
from leveling import calculate_xp_for_next_level

def print_player_info(user_data):
    player = user_data.get("player", {})
    name = player.get("name", "Unknown")
    level = player.get("level", 1)
    xp = player.get("xp", 0)
    date = datetime.now().strftime('%Y-%m-%d')

    print(f"Player: {name}")
    print(f"Level: {level} | XP: {xp}")
    print(f"Date: {date}")

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

#input validation function
def get_valid_input(prompt, input_type=str, valid_range=None, valid_options=None, allow_blank=False):

    while True:
        user_input = input(prompt).strip()
        if allow_blank and user_input == "":
            return None

        #type validation
        try:
            if input_type in [int, float]:
                value = input_type(user_input)
            else:
                value = user_input
        except ValueError:
            print(f"Invalid input. Please enter a {input_type.__name__}.")
            continue

        #range validation for numbers
        if valid_range and isinstance(value, (int, float)):
            min_val, max_val = valid_range
            if not (min_val <= value <= max_val):
                print(f"Input must be between {min_val} and {max_val}.")
                continue

        #strings options validation
        if valid_options and isinstance(value, str):
            if value.lower() not in [opt.lower() for opt in valid_options]:
                print(f"Invalid option. Choose from: {', '.join(valid_options)}")
                continue

        return value

#reusable menu select code
def select_from_menu(options, prompt="Select an option: "):

    if not options:
        print("No options available.")
        return None

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    selection = get_valid_input(prompt, int, valid_range=(1, len(options)))
    return selection - 1