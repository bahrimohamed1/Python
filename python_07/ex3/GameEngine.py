from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory
        self.strategy: GameStrategy
        self.hand: list = []
        self.battlefield: list = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

        self.hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell("fireball"),
        ]
        self.battlefield = []
        self.cards_created = len(self.hand)

    def simulate_turn(self) -> dict:
        actions = self.strategy.execute_turn(self.hand, self.battlefield)

        self.turns_simulated += 1
        self.total_damage += actions["damage_dealt"]

        return {
            "strategy": self.strategy.get_strategy_name(),
            "actions": actions,
        }

    def get_engine_status(self) -> dict:
        strategy_name = self.strategy.get_strategy_name()

        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
