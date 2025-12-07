#leveling.py

import UTILITY

#calculates xp is needed for next level
def calculate_xp_for_next_level(level):
    #100 XP * current level for linear increase
    return 100 * level


def display_xp_bar(current_xp, xp_needed, bar_length=30):
    #visual text level bar for fun
    filled_length = int(bar_length * current_xp // xp_needed)
    bar = '\u2588' * filled_length + '-' * (bar_length - filled_length)
    return f"[{bar}] {current_xp}/{xp_needed} XP"

#display saved user data
def display_level(user_data):
    player = user_data["player"]
    level = player["level"]
    current_xp = player["xp"]
    xp_needed = calculate_xp_for_next_level(level)
    xp_remaining = xp_needed - current_xp

    print("\n=== Leveling Screen ===\n")
    #resuable data print code
    UTILITY.print_player_info(user_data)
    print(display_xp_bar(current_xp, xp_needed))
    print(f"\nYou need {xp_remaining} more XP to level up.")
    input("\nPress Enter to return to the main menu.")