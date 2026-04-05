def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    pass


def spell_transformer(spells: list[str]) -> list[str]:
    pass


def mage_stats(mages: list[dict]) -> dict:
    pass


def main() -> None:
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'scrying'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Healing Amulet', 'power': 45, 'type': 'trinket'},
        {'name': 'Thunder Hammer', 'power': 100, 'type': 'weapon'}
    ]

    print(artifact_sorter(artifacts))


if __name__ == '__main__':
    main()
