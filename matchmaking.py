import heapq
import networkx as nx
from typing import List, Dict, Tuple
import time

class Player:
    def __init__(self, player_id: int, skill_level: float):
        self.id = player_id
        self.skill_level = skill_level
        self.wait_time = 0
        self.timestamp = time.time()

    def __lt__(self, other):
        # Priority based on wait time and skill level
        return self.wait_time > other.wait_time

class MatchmakingSystem:
    def __init__(self, max_skill_diff: float = 200):
        self.waiting_players = []  # Priority queue
        self.max_skill_diff = max_skill_diff
        self.matches = []

    def add_player(self, player: Player):
        """Add a player to the matchmaking queue"""
        heapq.heappush(self.waiting_players, player)
        self._update_wait_times()

    def _update_wait_times(self):
        """Update wait times for all players in queue"""
        current_time = time.time()
        for player in self.waiting_players:
            player.wait_time = current_time - player.timestamp

    def _find_suitable_matches(self) -> List[Tuple[Player, Player]]:
        """Find suitable matches using graph matching"""
        if len(self.waiting_players) < 2:
            return []

        # Create a graph for potential matches
        G = nx.Graph()
        players = self.waiting_players.copy()
        
        # Add nodes for each player
        for player in players:
            G.add_node(player.id, player=player)

        # Add edges between compatible players
        for i, p1 in enumerate(players):
            for p2 in players[i+1:]:
                if abs(p1.skill_level - p2.skill_level) <= self.max_skill_diff:
                    # Edge weight considers both skill difference and wait time
                    weight = 1 / (abs(p1.skill_level - p2.skill_level) + 1) * (p1.wait_time + p2.wait_time)
                    G.add_edge(p1.id, p2.id, weight=weight)

        # Find maximum weight matching
        matches = nx.max_weight_matching(G)
        
        # Convert matching to list of player pairs
        matched_pairs = []
        for p1_id, p2_id in matches:
            p1 = next(p for p in players if p.id == p1_id)
            p2 = next(p for p in players if p.id == p2_id)
            matched_pairs.append((p1, p2))

        return matched_pairs

    def match_players(self) -> List[Tuple[Player, Player]]:
        """Match players and remove them from the queue"""
        matches = self._find_suitable_matches()
        
        # Remove matched players from queue
        matched_players = set()
        for p1, p2 in matches:
            matched_players.add(p1)
            matched_players.add(p2)
        
        self.waiting_players = [p for p in self.waiting_players if p not in matched_players]
        heapq.heapify(self.waiting_players)
        
        return matches

    def get_queue_stats(self) -> Dict:
        """Get current matchmaking queue statistics"""
        if not self.waiting_players:
            return {"queue_size": 0, "avg_wait_time": 0, "avg_skill": 0}
        
        total_wait = sum(p.wait_time for p in self.waiting_players)
        total_skill = sum(p.skill_level for p in self.waiting_players)
        queue_size = len(self.waiting_players)
        
        return {
            "queue_size": queue_size,
            "avg_wait_time": total_wait / queue_size,
            "avg_skill": total_skill / queue_size
        }
