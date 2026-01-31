alice_achievement: set = {'first_kill',
                          'level_10', 'treasure_hunter', 'speed_demon'}
bob_achievement: set = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie_achievement: set = {'level_10', 'treasure_hunter', 'boss_slayer',
                            'speed_demon', 'perfectionist'}

unique_achievements = alice_achievement | bob_achievement | charlie_achievement
common_achievements = alice_achievement & bob_achievement & charlie_achievement

alice_only: set = alice_achievement - (bob_achievement | charlie_achievement)
bob_only: set = bob_achievement - (alice_achievement | charlie_achievement)
charlie_only: set = charlie_achievement - (alice_achievement | bob_achievement)
rare_achievements: set = alice_only | bob_only | charlie_only

print("=== Achievement Tracker System ===\n")
print(f"Player alice achievements: {alice_achievement}")
print(f"Player bob achievements: {bob_achievement}")
print(f"Player charlie achievements: {charlie_achievement}")
print("\n=== Achievement Analytics ===")
print(f"All unique achievements: {unique_achievements}")
print("Total unique achievements:", len(unique_achievements))
print("\nCommon to all players:", common_achievements)
print("Rare achievements (1 player):", rare_achievements)
print("\nAlice vs Bob common:", alice_achievement & bob_achievement)
print("Alice unique:", alice_achievement - bob_achievement)
print("Bob unique:", bob_achievement - alice_achievement)
