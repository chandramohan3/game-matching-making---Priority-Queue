from matchmaking import MatchmakingSystem, Player
import time

def main():
    # Initialize matchmaking system
    system = MatchmakingSystem(max_skill_diff=300)
    
    # Create some test players with different skill levels
    players = [
        Player(1, 1500),  # Average player
        Player(2, 1700),  # Above average player
        Player(3, 1300),  # Below average player
        Player(4, 1600),  # Slightly above average
        Player(5, 1400),  # Slightly below average
        Player(6, 2000),  # High skill player
    ]
    
    # Add players to the queue
    print("Adding players to queue...")
    for player in players:
        system.add_player(player)
        print(f"Added Player {player.id} (Skill: {player.skill_level})")
        
    # Print initial queue stats
    print("\nInitial Queue Stats:")
    print(system.get_queue_stats())
    
    # Wait a bit to simulate time passing
    time.sleep(2)
    
    # Match players
    print("\nMatching players...")
    matches = system.match_players()
    
    # Print matches
    print("\nMatches found:")
    for p1, p2 in matches:
        print(f"Player {p1.id} (Skill: {p1.skill_level}) vs Player {p2.id} (Skill: {p2.skill_level})")
        print(f"Skill difference: {abs(p1.skill_level - p2.skill_level)}")
        print("---")
    
    # Print remaining queue stats
    print("\nRemaining Queue Stats:")
    print(system.get_queue_stats())

if __name__ == "__main__":
    main()
