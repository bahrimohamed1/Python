from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard

def main():
    print()
    print("=== DataDeck Deck Builder ===")
    print()
    
    print("Building deck with different card types...")
    deck = Deck()
    
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    lightning_bolt = SpellCard("Lightning Bolt", 3, "Rare", "damage")
    mana_crystal = ArtifactCard("Mana Crystal", 2, "Common", 4, "+1 mana per turn")

    deck.add_card(fire_dragon)
    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)

    print("Deck stats:", deck.get_deck_stats())
    
    print()
    print("Drawing and playing cards:")
    print()
    
    print("Drew: Lightning Bolt (Spell)")
    print("Play result:", lightning_bolt.play({}))
    print()
    
    print("Drew: Mana Crystal (Artifact)")
    print("Play result:", mana_crystal.play({}))
    print()
    
    print("Drew: Fire Dragon (Creature)")
    print("Play result:", fire_dragon.play({}))

    print()
    print("Polymorphism in action: Same interface, different card behaviors!")
    
if __name__ == '__main__':
    main()