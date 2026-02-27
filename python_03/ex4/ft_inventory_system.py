inventory = {
    'players': {
        'alice': {
            'items': {
                'sword': 1, 'potion': 5, 'shield': 1},
            'total_value': 950, 'item_count': 7},
        'bob': {
            'items': {
                'sword': 1},
            'total_value': 500, 'item_count': 1}},
    'catalog': {
        'sword': {
            'type': 'weapon', 'value': 500, 'rarity': 'rare'},
        'potion': {
            'type': 'consumable', 'value': 50, 'rarity': 'common'},
        'shield': {
            'type': 'armor', 'value': 200, 'rarity': 'uncommon'},
        'magic_ring': {
            'type': 'weapon', 'value': 750, 'rarity': 'rare'}
    }
}


def items_transaction(source: dict,
                      destination: dict,
                      item: str, amount: int) -> None:

    value_of_item = inventory['catalog'][item]['value']
    source['items'][item] -= amount
    source['total_value'] -= value_of_item * amount
    source['item_count'] -= amount
    destination['items'][item] = amount
    destination['total_value'] += value_of_item * amount
    destination['item_count'] += amount
    print("Transaction successful!")


alice_items: dict = inventory['players']['alice']['items']
bob_items: dict = inventory['players']['bob']['items']
alice_total_value = inventory['players']['alice']['total_value']
alice_item_count = inventory['players']['alice']['item_count']
bob_item_count = inventory['players']['bob']['item_count']
bob_total_value = inventory['players']['bob']['total_value']
catalog: dict = inventory['catalog']


print("=== Player Inventory System ===\n")
print("=== Alice's Inventory ===")
for item in alice_items:
    print(f"{item} ({catalog[item]['type']}, {catalog[item]['rarity']}): "
          f"{alice_items[item]}x @ {catalog[item]['value']} gold each = "
          f"{alice_items[item] * catalog[item]['value']} gold")
print("\nInventory value:", alice_total_value, "gold")
print(f"Item count: {inventory['players']['alice']['item_count']} items")
print(
    f"Categories: weapon({alice_items.get('sword')}), consumable("
    f"{alice_items.get('potion')}), armor({alice_items.get('shield')})")
print("\n=== Transaction: Alice gives Bob 2 potions ===")
items_transaction(inventory['players']['alice'],
                  inventory['players']['bob'], 'potion', 2)
print('\n=== Updated Inventories ===')
print("Alice potions:", alice_items['potion'])
print("Bob potions:", bob_items['potion'])
print("\n=== Inventory Analytics ===")
if alice_total_value > bob_total_value:
    most_valuable_player = 'alice'
    most_valuable_inventory = inventory['players']['alice']['total_value']
else:
    most_valuable_player = 'bob'
    most_valuable_inventory = inventory['players']['bob']['total_value']

if alice_item_count > bob_item_count:
    player_with_most_items = 'alice'
    most_items = inventory['players']['alice']['item_count']
else:
    player_with_most_items = 'bob'
    most_items = inventory['players']['bob']['item_count']
print(
    f"Most valuable player: {most_valuable_player} "
    f"({most_valuable_inventory} gold)")
print(f"Most items: {player_with_most_items} ({most_items} items)")
rare_items = []
for item in catalog:
    if catalog[item]['rarity'] == 'rare':
        rare_items.append(item)
print("Rarest items: ", end="")
print(*rare_items, sep=", ")
