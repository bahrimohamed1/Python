def check_temperature(temp_str: str) -> str:
    """Validates temperature input for agricultural systems."""
    try:
        temp = int(temp_str)
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number"
    if temp < 0:
        return f"Error: {temp}°C is too cold for plants (min 0°C)"
    if temp > 40:
        return f"Error: {temp}°C is too hot for plants (max 40°C)"
    else:
        return f"Temperature {temp}°C is perfect for plants!"


def test_temperature_input() -> None:
    """Tests various temperature inputs and demonstrates error handling."""
    print("\nTesting temperature: 25")
    print(check_temperature('25'))
    print("\nTesting temperature: abc")
    print(check_temperature('abc'))
    print("\nTesting temperature: 100")
    print(check_temperature('100'))
    print("\nTesting temperature: -50")
    print(check_temperature('-50'))


print("=== Garden Temperature Checker ===")
test_temperature_input()
print("\nAll tests completed - program didn't crash!")
