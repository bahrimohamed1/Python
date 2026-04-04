from enum import Enum
from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validation_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith('AC'):
            raise ValueError("ID must start with 'AC'")
        if self.contact_type == 'physical':
            if not self.is_verified:
                raise ValueError("Physical contact reports must be verified")
        if self.contact_type == "telepathic":
            if self.witness_count < 3:
                raise ValueError("Telepathic contact requires at least"
                                 "3 witnesses")
        if self.signal_strength > 7.0:
            if not self.message_received:
                raise ValueError(
                    "Strong signals (> 7.0) should include received messages")

        return self


def main() -> None:
    contact_report = AlienContact(
        contact_id='AC_2024_001',
        timestamp=datetime(2026, 4, 5),
        contact_type=ContactType.RADIO.name,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )

    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")

    print(f"ID: {contact_report.contact_id}")
    print(f"Type: {contact_report.contact_type}")
    print(f"Location: {contact_report.location}")
    print(f"Signal: {contact_report.signal_strength}/10")
    print(f"Duration: {contact_report.duration_minutes} minutes")
    print(f"Witnesses: {contact_report.contact_id}")
    print(f"Message: '{contact_report.contact_id}'")


if __name__ == '__main__':
    main()
