from matchmaking import MatchmakingSystem, Player
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_player_bar(skill_level, width=50):
    normalized = (skill_level - 1000) / 1000  # Normalize between 1000-2000 skill range
    bar_length = int(normalized * width)
    return f"[{'#' * bar_length}{' ' * (width - bar_length)}] {skill_level}"

def visualize_match(p1, p2):
    print("\n" + "=" * 60)
    print(f"MATCH FOUND!")
    print(f"Player {p1.id}: {print_player_bar(p1.skill_level)}")
    print(f"Player {p2.id}: {print_player_bar(p2.skill_level)}")
    print(f"Skill Difference: {abs(p1.skill_level - p2.skill_level)}")
    print("=" * 60)
    time.sleep(1)  # Add dramatic pause

def main():
    system = MatchmakingSystem(max_skill_diff=300)
    
    # Create test players
    players = [
        Player(1, 1500),  # Average player
        Player(2, 1700),  # Above average player
        Player(3, 1300),  # Below average player
        Player(4, 1600),  # Slightly above average
        Player(5, 1400),  # Slightly below average
        Player(6, 2000),  # High skill player
    ]
    
    clear_screen()
    print("🎮 Game Matchmaking Visualization 🎮")
    print("\nAdding players to queue...")
    
    for player in players:
        system.add_player(player)
        print(f"\nPlayer {player.id} joined queue:")
        print(print_player_bar(player.skill_level))
        time.sleep(0.5)
    
    print("\nFinding optimal matches...")
    time.sleep(1)
    
    matches = system.match_players()
    
    for p1, p2 in matches:
        visualize_match(p1, p2)

if __name__ == "__main__":
    main()
