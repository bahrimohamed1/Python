from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class CrewRanks(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = 'planned'
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validation_rules(self) -> 'SpaceMission':
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")

        found = False
        for member in self.crew:
            if member.rank == CrewRanks.COMMANDER or \
                    member.rank == CrewRanks.CAPTAIN:
                found = True
        if not found:
            raise ValueError(
                "Mission must have at least one Commander or Captain")

        experienced = 0
        if self.duration_days > 365:
            for crew in self.crew:
                if crew.years_experience >= 5:
                    experienced += 1

            if experienced < len(self.crew) / 2:
                raise ValueError(
                    r"Long missions (> 365 days) need 50% experienced crew "
                    "(5+ years)")

        for crew in self.crew:
            if not crew.is_active:
                raise ValueError("All crew members must be active")

        return self


def main() -> None:
    sarah = CrewMember(
        member_id='ID_00',
        name="Sarah Connor",
        rank=CrewRanks.COMMANDER,
        age=31,
        specialization="Mission Command",
        years_experience=5,
        is_active=True
    )
    john = CrewMember(
        member_id='ID_01',
        name="John Smith",
        rank=CrewRanks.LIEUTENANT,
        age=38,
        specialization="Navigation",
        years_experience=10,
        is_active=True
    )
    alice = CrewMember(
        member_id='ID_02',
        name="Alice Johnson",
        rank=CrewRanks.OFFICER,
        age=42,
        specialization="Engineering",
        years_experience=15,
        is_active=True
    )

    space_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name='Mars Colony Establishment',
        destination='Mars',
        launch_date=datetime(2026, 4, 5),
        duration_days=900,
        crew=[sarah, john, alice],
        mission_status='planned',
        budget_millions=2500.0
    )

    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    print(f"Mission: {space_mission.mission_name}")
    print(f"ID: {space_mission.mission_id}")
    print(f"Destination: {space_mission.destination}")
    print(f"Duration: {space_mission.duration_days} days")
    print(f"Budget: ${space_mission.budget_millions}M")
    print(f"Crew size: {len(space_mission.crew)}")
    print("Crew members:")
    for crew in space_mission.crew:
        print(f"- {crew.name} ({crew.rank.value}) - {crew.specialization}")

    print()
    print("=========================================")
    print("Expected validation error:")

    try:
        sarah.rank = CrewRanks.OFFICER

        SpaceMission(
            mission_id="M2024_MARS",
            mission_name='Mars Colony Establishment',
            destination='Mars',
            launch_date=datetime(2026, 4, 5),
            duration_days=900,
            crew=[sarah, john, alice],
            mission_status='planned',
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(e.errors()[0].get('msg').split(',')[1].strip())


if __name__ == '__main__':
    main()
