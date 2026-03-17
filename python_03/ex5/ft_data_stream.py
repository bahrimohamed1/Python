from typing import Generator


def event_generator(events: list[dict]) -> Generator[dict, None, None]:
    for event in events:
        yield event


def fibonacci_generator(n: int = 10) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(nb: int) -> bool:
    if nb < 2:
        return False
    if nb == 2:
        return True
    if nb % 2 == 0:
        return False

    for i in range(3, int(nb**0.5) + 1, 2):
        if nb % i == 0:
            return False
    return True


def prime_generator(count: int = 5) -> Generator[int, None, None]:
    nb = 2
    found = 0
    while found < count:
        if is_prime(nb):
            found += 1
            yield nb
        nb += 1


players_data = [
    {"player": "alice", "event_type": "login", "data": {"level": 5}},
    {"player": "bob", "event_type": "login", "data": {"level": 12}},
    {"player": "alice", "event_type": "kill", "data": {"level": 5}},
    {"player": "charlie", "event_type": "login", "data": {"level": 3}},
    {"player": "alice", "event_type": "level_up", "data": {"level": 6}},
    {"player": "bob", "event_type": "kill", "data": {"level": 12}},
    {"player": "alice", "event_type": "item_found", "data": {"level": 6}},
    {"player": "bob", "event_type": "logout", "data": {"level": 12}},
    {"player": "charlie", "event_type": "death", "data": {"level": 3}},
    {"player": "alice", "event_type": "item_found", "data": {"level": 6}},
]

print("=== Game Data Stream Processor ===\n")
print(f"Processing {len(players_data)} game events...\n")

events: Generator[dict, None, None] = event_generator(players_data)

high_level_count: int = 0
treasure_events: int = 0
level_up_events: int = 0
event_count: int = 0

for i, event in enumerate(events, 1):
    event_count = i

    if event['data']['level'] >= 10:
        high_level_count += 1

    if event['event_type'] == 'login':
        print(f"Event {i}: Player {event['player']} "
              f"(level {event['data']['level']}) logged in")
    elif event['event_type'] == 'logout':
        print(f"Event {i}: Player {event['player']} "
              f"(level {event['data']['level']}) logged out")
    elif event['event_type'] == 'level_up':
        level_up_events += 1
        print(f"Event {i}: Player {event['player']} "
              f"(level {event['data']['level']}) leveled up")
    elif event['event_type'] == 'death':
        print(f"Event {i}: Player {event['player']} "
              f"(level {event['data']['level']}) died")
    elif event['event_type'] == 'kill':
        print(f"Event {i}: Player {event['player']} "
              f"(level {event['data']['level']}) killed monster")
    elif event['event_type'] == 'item_found':
        treasure_events += 1
        print(f"Event {i}: Player {event['player']} "
              f"(level {event['data']['level']}) found treasure")
    else:
        print(f"Event {i}: Unknown event type - {event['event_type']}")

print("\n=== Stream Analytics ===")
print(f"Total events processed: {event_count}")
print(f"High-level players (10+): {high_level_count}")
print(f"Treasure events: {treasure_events}")
print(f"Level-up events: {level_up_events}\n")

print("=== Generator Demonstration ===")
fib_gen: Generator[int, None, None] = fibonacci_generator(10)
print("Fibonacci sequence (first 10): ", end="")
print(*fib_gen, sep=", ")

prime_gen: Generator[int, None, None] = prime_generator(5)
print("Prime numbers (first 5): ", end="")
print(*prime_gen, sep=", ")
