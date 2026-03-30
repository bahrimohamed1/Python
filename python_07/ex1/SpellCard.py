from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        if effect_type not in ['damage', 'heal', 'buff', 'debuff']:
            raise ValueError(
                "effect_type must be one of: damage, heal, buff, debuff")

        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        effects = {
            "damage": "Deal 3 damage to target",
            "heal": "Restore 3 health to target",
            "buff": "Grant +2 attack to target",
            "debuff": "Reduce target attack by 2",
        }

        game_state.update({
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effects[self.effect_type],
        })

        return game_state

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True,
        }
