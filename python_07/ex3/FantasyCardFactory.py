from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.registry = {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }

    def create_creature(self,
                        name_or_power: str | int
                        | None = None) -> CreatureCard:
        if name_or_power == "dragon":
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

        if name_or_power == "goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 5, 2)

        if isinstance(name_or_power, int):
            return CreatureCard(
                "Custom Creature",
                name_or_power,
                "Rare",
                name_or_power,
                name_or_power,
            )

        raise ValueError("unsupported fantasy creature type")

    def create_spell(self,
                     name_or_power: str | int | None = None) -> SpellCard:
        if name_or_power == "fireball":
            return SpellCard("Lightning Bolt", 3, "Rare", "damage")

        if isinstance(name_or_power, int):
            return SpellCard("Custom Spell", name_or_power, "Rare", "damage")

        raise ValueError("unsupported fantasy spell type")

    def create_artifact(
        self,
        name_or_power: str | int | None = None,
    ) -> ArtifactCard:
        if name_or_power == "mana_ring" or name_or_power is None:
            return ArtifactCard("Mana Ring", 2, "Common", 4,
                                "+1 mana per turn")

        if isinstance(name_or_power, int):
            if name_or_power <= 0:
                raise ValueError("artifact durability must be positive")
            return ArtifactCard(
                "Custom Artifact",
                2,
                "Rare",
                name_or_power,
                "Custom permanent effect",
            )

        raise ValueError("unsupported fantasy artifact type")

    def create_themed_deck(self, size: int) -> dict:
        if not isinstance(size, int) or size <= 0:
            raise ValueError("size must be a positive integer")

        cards = []
        blueprint = [
            self.create_creature("dragon"),
            self.create_creature("goblin"),
            self.create_spell("fireball"),
            self.create_artifact("mana_ring"),
        ]

        for index in range(size):
            cards.append(blueprint[index % len(blueprint)])

        return {
            "theme": "Fantasy",
            "size": size,
            "cards": cards,
        }

    def get_supported_types(self) -> dict:
        return self.registry
