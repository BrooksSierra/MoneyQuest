#UTILITY.py
from datetime import datetime

def print_player_info(user_data):
    player = user_data.get("player", {})
    name = player.get("name", "Unknown")
    level = player.get("level", 1)
    xp = player.get("xp", 0)
    date = datetime.now().strftime('%Y-%m-%d')

    print(f"Player: {name}")
    print(f"Level: {level} | XP: {xp}")
    print(f"Date: {date}")