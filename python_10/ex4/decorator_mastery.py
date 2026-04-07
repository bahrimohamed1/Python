from functools import wraps
from collections.abc import Callable
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper() -> Callable:
        print(f"Casting {func.__nmae__}...")

        start = time.time()
        res = func()
        time.sleep(0.3)
        end = time.time()

        print(f"Spell completed in {(start - end):.2f} seconds")

        return res

    return wrapper

@spell_timer
def fireball() -> None:
    return "Fireball cast!"

def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper():
            pass
        
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    pass


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass
