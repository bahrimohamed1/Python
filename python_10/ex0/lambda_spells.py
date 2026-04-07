def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    result = {
        'max_power': max(mages, key=lambda x: x['power'])['power'],
        'min_power': min(mages, key=lambda x: x['power'])['power'],
        'avg_power': round(
            sum(map(lambda x: x['power'], mages)) / len(mages), 2)
    }
    return result


def main() -> None:
    artifacts = [
        {'name': 'Crystal Orb', 'power': 71, 'type': 'accessory'},
        {'name': 'Shadow Blade', 'power': 88, 'type': 'weapon'},
        {'name': 'Ice Wand', 'power': 93, 'type': 'focus'},
        {'name': 'Shadow Blade', 'power': 111, 'type': 'accessory'}
    ]

    mages = [
        {'name': 'Jordan', 'power': 73, 'element': 'wind'},
        {'name': 'Riley', 'power': 74, 'element': 'water'},
        {'name': 'Morgan', 'power': 81, 'element': 'lightning'},
        {'name': 'Phoenix', 'power': 51, 'element': 'earth'},
        {'name': 'Kai', 'power': 69, 'element': 'light'}
    ]

    spells = ['shield', 'meteor', 'tornado', 'blizzard']

    print()
    print("Testing artifact sorter...")
    print(artifact_sorter(artifacts))

    print()
    print("Testing power filter...")
    print(power_filter(mages, 70))

    print()
    print("Testing spell transformer...")
    print(spell_transformer(spells))

    print()
    print("Testing mage stats...")
    print(mage_stats(mages))


if __name__ == '__main__':
    main()
