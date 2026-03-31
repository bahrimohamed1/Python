from ex2.EliteCard import EliteCard


def main() -> None:
    print()
    print("=== DataDeck Ability System ===")
    print()

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    arcane_warrior = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity="Epic",
        attack_power=5,
        health=10,
        mana=4,
        magic_power=6,
    )

    print()
    print("Playing Arcane Warrior (Elite Card):")
    print()

    print("Combat phase:")
    print("Attack result:", arcane_warrior.attack("Enemy"))
    print("Defense result:", arcane_warrior.defend(5))
    print()

    print("Magic phase:")
    print(
        "Spell cast:",
        arcane_warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"]),
    )
    print("Mana channel:", arcane_warrior.channel_mana(3))

    print()
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
