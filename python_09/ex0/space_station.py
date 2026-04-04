from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    space_station = SpaceStation(
        station_id='ISS001',
        name='International Space Station',
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2026, 4, 4),
        # Pydantic can also parse:
        # last_maintenance="2026-04-04T00:00:00"
        is_operational=False
    )

    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")

    print(f"ID: {space_station.station_id}")
    print(f"Name: {space_station.name}")
    print(f"Crew: {space_station.crew_size} ", end="")
    print("person" if space_station.crew_size == 1 else "people")
    print(f"Power: {space_station.power_level}%")
    print(f"Oxygen: {space_station.oxygen_level}%")
    print("Status:",
          "Operational" if space_station.is_operational else "Non Operational")

    print()
    print("========================================")
    print("Expected validation error:")

    try:
        SpaceStation(
            station_id='ISS001',
            name='International Space Station',
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 4, 4),
            is_operational=True
        )
    except ValidationError as e:
        print(e.errors()[0].get('msg'))


if __name__ == '__main__':
    main()
