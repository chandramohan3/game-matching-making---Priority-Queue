# Game Matchmaking System

A Python implementation of a multiplayer game matchmaking system using advanced data structures and algorithms.

## Key Features

- Priority Queue-based player waiting system
- Graph-based matching algorithm for optimal player pairing
- Skill-based matchmaking with configurable skill difference threshold
- Wait time consideration to prevent indefinite waiting
- Queue statistics tracking

## Data Structures & Algorithms Used

1. **Priority Queue (Heap)**: Used for managing waiting players, prioritizing those who have waited longer
2. **Graph Matching**: Implements maximum weight matching for optimal player pairing
3. **Binary Search** (implicit in the heap operations): Used in the priority queue operations

## Requirements

- Python 3.8+
- numpy
- networkx
- pytest

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the test script to see the matchmaking system in action:
```bash
python test_matchmaking.py
```

## Implementation Details

- `Player`: Class representing a player with ID, skill level, and wait time
- `MatchmakingSystem`: Main class implementing the matchmaking logic
  - Uses a priority queue for managing waiting players
  - Implements graph-based matching for optimal player pairing
  - Considers both skill difference and wait time when matching players
