from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Any
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation.lower() not in ['add', 'multiply', 'max', 'min']:
        raise ValueError(f"ERROR: {operation} is not a valid operation")

    if operation.lower() == 'add':
        op = add

    elif operation.lower() == 'multiply':
        op = mul

    elif operation.lower() == 'max':
        op = max

    elif operation.lower() == 'min':
        op = min

    return reduce(op, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchantment = partial(base_enchantment, 50, 'fire')
    water_enchantment = partial(base_enchantment, 50, 'water')
    air_enchantment = partial(base_enchantment, 50, 'air')

    return {
        'fire': fire_enchantment,
        'water': water_enchantment,
        'air': air_enchantment
    }


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} hit for {power} {element} damage"


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n

    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell_system(x: Any) -> str:
        return "Unknown spell type"

    @spell_system.register(int)
    def _(x) -> str:
        return f"{x} damage"

    @spell_system.register(str)
    def _(x) -> str:
        return f"{x}"

    @spell_system.register(list)
    def _(x) -> str:
        return f"{len(x)} spells"

    return spell_system


def main() -> None:
    try:
        spell_powers = [36, 32, 21, 27, 23, 12]

        print()
        print("Testing spell reducer...")
        print(f"Sum: {spell_reducer(spell_powers, 'add')}")
        print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
        print(f"Max: {spell_reducer(spell_powers, 'max')}")
        print()

        print("Testing partial enchanter...")
        enchanters = partial_enchanter(base_enchantment)
        print({element: spell('Dragon') for element, spell in enchanters.items()})

        print()
        print("Testing memoized fibonacci...")
        print(f"Fib(0): {memoized_fibonacci(0)}")
        print(f"Fib(1): {memoized_fibonacci(1)}")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")

        print()
        print("Testing spell dispatcher...")
        result = spell_dispatcher()
        print(f"Damage spell: {result(42)}")
        print(f"Enchantment: {result('fireball')}")
        print(f"Multi-cast: {result(['flash', 'snowball', 'ignite'])}")
        print(result({}))

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
