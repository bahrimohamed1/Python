from Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        
    def play(slef, game_stats: dict) -> dict:
        return super().play(game_stats)
    
    def attack_target(self, target: int) -> dict:
        pass