from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        rating: int = 1200,
    ) -> None:
        super().__init__(name, cost, rarity)

        self.card_id = card_id
        self.attack_power = attack_power
        self.health = health
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card deployed to battlefield",
        }

    def attack(self, target) -> dict:
        target_name = target.name if hasattr(target, "name") else target
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack_power,
            "combat_resolved": True,
        }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            raise ValueError("incoming_damage must be a non-negative integer")

        damage_blocked = min(2, incoming_damage)
        damage_taken = incoming_damage - damage_blocked
        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health,
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        if not isinstance(wins, int) or wins < 0:
            raise ValueError("wins must be a non-negative integer")
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        if not isinstance(losses, int) or losses < 0:
            raise ValueError("losses must be a non-negative integer")
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
        }

    def get_tournament_stats(self) -> dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
            "attack": self.attack_power,
            "health": self.health,
        }
