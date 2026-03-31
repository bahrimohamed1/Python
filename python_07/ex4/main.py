from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print()
    print("=== DataDeck Tournament Platform ===")
    print()
    print("Registering Tournament Cards...")
    print()

    platform = TournamentPlatform()

    fire_dragon = TournamentCard(
        card_id="dragon_001",
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack_power=7,
        health=5,
        rating=1200,
    )

    ice_wizard = TournamentCard(
        card_id="wizard_001",
        name="Ice Wizard",
        cost=4,
        rarity="Epic",
        attack_power=5,
        health=4,
        rating=1150,
    )

    platform.register_card(fire_dragon)
    platform.register_card(ice_wizard)

    print("Fire Dragon (ID: dragon_001):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("- Rating:", fire_dragon.calculate_rating())
    print(f"- Record: {fire_dragon.wins}-{fire_dragon.losses}")

    print()
    print("Ice Wizard (ID: wizard_001):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("- Rating:", ice_wizard.calculate_rating())
    print(f"- Record: {ice_wizard.wins}-{ice_wizard.losses}")

    print()
    print("Creating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", match_result)

    print()
    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for index, entry in enumerate(leaderboard, start=1):
        print(
            f"{index}. {entry['name']} - Rating: {entry['rating']} "
            f"({entry['record']})"
        )

    print()
    print("Platform Report:")
    print(platform.generate_tournament_report())

    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
