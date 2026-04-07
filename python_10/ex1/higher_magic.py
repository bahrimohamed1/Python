from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combine(target: str, power: int) -> tuple[str, str]:
        result1 = spell1(target, power)
        result2 = spell2(target, power)

        return (result1, result2)

    return combine


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiply(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return multiply


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast_if_true(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)

        else:
            return "Spell fizzled"

    return cast_if_true


def is_fed(target: str, power: int) -> bool:
    return power > 20


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_all(target: str, power: int) -> list[str]:
        casted_spells = []
        for spell in spells:
            casted_spells.append(spell(target, power))

        return casted_spells

    return cast_all


def main() -> None:
    power = 25
    target = 'Dragon'

    print()

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(combined(target, power))
    print()

    print("Testing power amplifier...")
    multiplied = power_amplifier(fireball, 2)
    print(multiplied(target, power))
    print()

    print("Testing conditional caster...")
    casted = conditional_caster(is_fed, fireball)
    print(casted(target, power))
    print()

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence(target, power))


if __name__ == '__main__':
    main()
