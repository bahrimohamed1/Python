import sys
import math

if len(sys.argv) == 2:
    print("=== Game Coordinate System ===\n")
    x, y, z = sys.argv[1].split(',')
    try:
        position: tuple = (int(x), int(y), int(z))
        x1, y1, z1 = position
        test_position: tuple = (0, 0, 0)
        x2, y2, z2 = test_position
        print(f'Parsing coordinates: "{sys.argv[1]}"')
        print("Parsed position:", position)
        result = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        print(f"Distance between {test_position} and {position}: {result}")
        print("\nUnpacking demonstration:")
        print(f"Player at x={x1}, y={y1}, z={z1}")
        print(f"Coordinates: X={x1}, Y={y1}, Z={z1}")
    except ValueError as e:
        print("Parsing invalid coordinates:", sys.argv[1])
        print("Error parsing coordinates:", e)
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
