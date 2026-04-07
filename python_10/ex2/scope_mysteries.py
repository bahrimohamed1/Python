from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total_power = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchanter(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchanter


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        if key in memory:
            return memory[key]

        return "Memory not found"

    return {'store': store, 'recall': recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_a call 3: {counter_a()}")

    print()
    print("Testing spell accumulator...")
    accumulation = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulation(20)}")
    print(f"Base 100, add 30: {accumulation(30)}")

    print()
    print("Testing enchantment factory...")
    factory_a = enchantment_factory('Flaming')
    factory_b = enchantment_factory('Frozen')
    print(factory_a('Sword'))
    print(factory_b('Shield'))

    print()
    print("Testing memory vault...")

    vault_a = memory_vault()
    store = vault_a['store']
    recall = vault_a['recall']

    print("Store 'secret' = 42")
    store('secret', 42)

    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unknown': {recall('unknown')}")


if __name__ == '__main__':
    main()
