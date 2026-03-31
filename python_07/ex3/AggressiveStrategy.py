from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        targets_attacked = []

        sorted_hand = sorted(hand, key=lambda card: card.cost)

        for card in sorted_hand:
            if mana_used >= 5:
                break

            remaining_budget = 5 - mana_used

            if card.cost > remaining_budget:
                continue

            cards_played.append(card.name)
            mana_used += card.cost

            if hasattr(card, "attack"):
                targets_attacked.append("Enemy Player")
                damage_dealt += getattr(card, "attack", 0)

            elif hasattr(card, "effect_type") and card.effect_type == "damage":
                damage_dealt += 3
                if "Enemy Player" not in targets_attacked:
                    targets_attacked.append("Enemy Player")

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: list) -> list:
        if "Enemy Player" in available_targets:
            ordered_targets = ["Enemy Player"]
            for target in available_targets:
                if target != "Enemy Player":
                    ordered_targets.append(target)
            return ordered_targets
        return available_targets
