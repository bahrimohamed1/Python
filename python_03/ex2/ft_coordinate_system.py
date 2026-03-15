import sys
import math

print("=== Game Coordinate System ===\n")

try:
    if len(sys.argv) == 2:
        x, y, z = sys.argv[1].split(",")
        x, y, z = int(x), int(y), int(z)
    elif len(sys.argv) == 4:
        x, y, z = (int(value) for value in sys.argv[1:4])
    else:
        print("Error: Please provide exactly 3 coordinates (x y z)")
        sys.exit(1)

    position: tuple[int, int, int] = (x, y, z)
    origin: tuple[int, int, int] = (0, 0, 0)

    x1, y1, z1 = position
    x2, y2, z2 = origin

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    print(f"Parsed position: {position}")
    print(f"Distance between {origin} and {position}: {distance:.2f}")
    print("\nUnpacking demonstration:")
    print(f"Player at x={x1}, y={y1}, z={z1}")
    print(f"Coordinates: X={x1}, Y={y1}, Z={z1}")

except ValueError as e:
    print(f'Parsing invalid coordinates: "{sys.argv[1]}"')
    print(f"Error: Invalid coordinate - {e}")
    print(f'Error details - Type: {e.__class__.__name__}, Args: ("{e}".)')
    sys.exit(1)
