def garden_operations() -> None:
    print("Testing Value")
    try:
        test_str = int('abc')
    except ValueError:
        print(f"Caught ValueError: invalid literal for int()")
    try:
        number = 1 / 0
    except ZeroDivisionError:
        print(f"Caught ZeroDivisionError: division by zero")


def test_error_types():
    garden_operations()


test_error_types()
