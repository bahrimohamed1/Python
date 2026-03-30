from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")

        self.attack = attack
        self.health = health
        self.type = "Creature"

    def play(self, game_state: dict) -> dict:
        game_state.update({
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': "Creature summoned to battlefield"
        })

        return game_state

    def get_card_info(self) -> dict:
        result = super().get_card_info()
        result.update({
            'type': self.type,
            'attack': self.attack,
            'health': self.health
        })
        return result

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }
