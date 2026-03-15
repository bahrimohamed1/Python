import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        if ":" not in arg:
            continue

        key, value = arg.split(":")
        try:
            value = int(value)
            if value < 0:
                raise ValueError
        except ValueError:
            print(f"{value} is not a valid number!")
            sys.exit(1)

        inventory.update({key: value})

    return inventory


def main() -> None:
    inventory: dict[str, int] = parse_inventory(sys.argv[1:])

    print("=== Inventory System Analysis ===")
    total_items: int = 0
    for v in inventory.values():
        total_items += v
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    for name, qty in sorted(inventory.items(),
                            key=lambda x: x[1], reverse=True):
        percent: float = (qty / total_items * 100) if total_items > 0 else 0
        print(f"{name}: {qty} units ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most_item: tuple[str, int] = sorted(inventory.items(),
                                        key=lambda x: x[1], reverse=True)[0]
    least_item: tuple[str, int] = sorted(
        inventory.items(), key=lambda x: x[1])[0]
    print(f"Most abundant: {most_item[0]} ({most_item[1]} units)")
    print(f"Least abundant: {least_item[0]} ({least_item[1]} units)")

    print("\n=== Item Categories ===")
    categories: dict[str, dict[str, int]] = {"Moderate": {}, "Scarce": {}}
    for name, qty in inventory.items():
        if qty >= 4:
            categories["Moderate"].update({name: qty})
        else:
            categories["Scarce"].update({name: qty})

    for cat, items in categories.items():
        print(f"{cat}: {items}")

    print("\n=== Management Suggestions ===")
    restock: list[str] = []
    for name, qty in inventory.items():
        if qty <= 1:
            restock.append(name)
    if len(restock) > 0:
        print("Restock needed: " + ", ".join(restock))
    else:
        print("Restock needed: None")

    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys: " + ", ".join(inventory.keys()))
    print("Dictionary values: " + ", ".join(str(value)
          for value in inventory.values()))
    sample_lookup = inventory.get("sword") is not None
    print(f"Sample lookup - 'sword' in inventory: {sample_lookup}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No items provided!")
        sys.exit(1)
    main()
