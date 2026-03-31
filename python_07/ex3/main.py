from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def format_hand(hand: list) -> str:
    return "[" + ", ".join(f"{card.name} ({card.cost})" for card in hand) + "]"


def main() -> None:
    print()
    print("=== DataDeck Game Engine ===")
    print()

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    print()
    print("Simulating aggressive turn...")
    print("Hand:", format_hand(engine.hand))

    print()
    print("Turn execution:")
    turn_result = engine.simulate_turn()
    print("Strategy:", strategy.get_strategy_name())
    print("Actions:", turn_result["actions"])

    print()
    print("Game Report:")
    print(engine.get_engine_status())

    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
