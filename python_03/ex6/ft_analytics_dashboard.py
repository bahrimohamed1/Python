players = [
    {
        "name": "Alice",
        "sessions_played": 13,
        "is_active": True,
        "data": {
            "level": 41,
            "achievements_count": 5,
            "total_score": 2300
        },
        "achievements": {
            'first_kill', 'level_10', 'treasure_hunter', 'speed_demon', 'boss_slayer'
        }
    },
    {
        "name": "Bob",
        "sessions_played": 27,
        "is_active": True,
        "data": {
            "level": 16,
            "achievements_count": 3,
            "total_score": 1800
        },
        "achievements": {
            'first_kill', 'boss_slayer', 'collector'
        }
    },
    {
        "name": "Charlie",
        "sessions_played": 21,
        "is_active": True,
        "data": {
            "level": 44,
            "achievements_count": 6,
            "total_score": 2150
        },
        "achievements": {
            'level_10', 'treasure_hunter', 'boss_slayer',
            'speed_demon', 'perfectionist', 'first_kill'
        }
    },
    {
        "name": "Diana",
        "sessions_played": 21,
        "is_active": False,
        "data": {
            "level": 3,
            "achievements_count": 4,
            "total_score": 2050
        },
        "achievements": {
            'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'
        }
    }
]

high_scores: list = [
    player['name'] for player in players
    if player['data']['total_score'] > 2000
]

scores_doubled: list = [
    player['data']['total_score'] * 2 for player in players
]

active_players: list = [
    player['name'] for player in players if player['is_active'] is True
]

player_scores: dict = {
    player['name']: player['data']['total_score'] for player in players
    if player['is_active'] is True
}

achievement_count: dict = {
    player['name']: player['data']['achievements_count'] for player in players
    if player['is_active'] is True
}

unique_players: set = {
    player['name'] for player in players
}

all_achievements: set = {
    achievement for player in players for achievement in player['achievements']
}
unique_achievements: set = {
    achievement for achievement in all_achievements if
    len([player for player in players if
         achievement in player['achievements']]) == 1
}

all_players_scores: dict = {
    player['name']: player['data']['total_score'] for player in players
}
average_score: float = sum(all_players_scores.values()
                           ) / len(all_players_scores)

print("=== Game Analytics Dashboard ===\n")
print("=== List Comprehension Examples ===")
print(f"High scores (>2000): {high_scores}")
print(f"Scores doubled: {scores_doubled}")
print(f"Active players: {active_players}")

print("\n=== Dict Comprehension Examples ===")
print(f"player scores: {player_scores}")
print(f"Achievement counts: {achievement_count}")

print("\n=== Set Comprehension Examples ===")
print(f"Unique players: {unique_players}")
print(f"Unique achievements: {unique_achievements}")

print("\n=== Combined Analytics ===")
print(f"Total players: {len(players)}")
print(f"Total unique achievements: {len(all_achievements)}")
print(f"Average score: {average_score}")
