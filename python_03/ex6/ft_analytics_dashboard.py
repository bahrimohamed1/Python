players: list[dict] = [
    {"name": "alice", "score": 2300,
     "achievements": [
         "first_kill", "level_10", "treasure_hunter",
         "speed_demon", "boss_slayer", "explorer"],
     "region": "north", "active": True},
    {"name": "bob", "score": 1800,
     "achievements": [
         "first_kill", "level_5", "collector", "veteran", "hunter"],
     "region": "east", "active": True},
    {"name": "charlie", "score": 2150,
     "achievements": [
         "level_10", "treasure_hunter", "speed_demon", "boss_slayer",
         "perfectionist", "legend", "master", "slayer"],
     "region": "central", "active": True},
    {"name": "diana", "score": 2050,
     "achievements": [
         "first_kill", "level_10", "boss_slayer",
         "explorer", "conqueror", "champion"],
     "region": "north", "active": False}
]

print("=== Game Analytics Dashboard ===")

print("\n=== list Comprehension Examples ===")
high_scorers: list[str] = [p["name"] for p in players if p["score"] > 2000]
print(f"High scorers (>2000): {high_scorers}")

doubled_scores: list[int] = [(player["score"] * 2) for player in players]
print(f"Scores doubled: {doubled_scores}")

active_players: list[str] = [p["name"] for p in players if p["active"]]
print(f"Active players: {active_players}")


print("\n=== dict Comprehension Examples ===")
player_scores: dict[str, int] = {p["name"]: p["score"] for p in players}
print(f"Player scores: {player_scores}")

high_count: int = len([p for p in players if p["score"] > 2000])
medium_count: int = len([p for p in players if 1500 <= p["score"] <= 2000])
low_count: int = len([p for p in players if p["score"] < 1500])
score_categories: dict[str, int] = {
    "high": high_count, "medium": medium_count, "low": low_count}
print(f"Score categories: {score_categories}")

ach_counts: dict[str, int] = {player["name"]: len(
    player["achievements"]) for player in players}
print(f"Achievement counts: {ach_counts}")


print("\n=== set Comprehension Examples ===")
unique_players: set[str] = {player["name"] for player in players}
print(f"Unique players: {unique_players}")

unique_achievements: set[str] = {a for p in players for a in p["achievements"]}
print(f"Unique achievements: {unique_achievements}")

active_regions: set[str] = {p["region"] for p in players if p["active"]}
print(f"Active regions: {active_regions}")


print("\n=== Combined Analysis ===")
total_players: int = len(players)
print(f"Total players: {total_players}")

total_unique_achs: int = len(unique_achievements)
print(f"Total unique achievements: {total_unique_achs}")

avg_score: float = sum(player["score"] for player in players) / len(players)
print(f"Average score: {avg_score:.1f}")

top_player: dict = max(players, key=lambda player: player["score"])
print(
    f"Top performer: {top_player['name']} ({top_player['score']} points, "
    f"{len(top_player['achievements'])} achievements)")
