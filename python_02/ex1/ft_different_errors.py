def garden_operations(test_str) -> None:
    if test_str == 'key':
        try:
            test_dict = {}
            print(test_dict['plant'])
        except KeyError as e:
            print(f"Caught KeyError: {e}")

    elif test_str == 'all':
        try:
            int(test_str)
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Caught an error, but program continue!")
    else:
        try:
            convert_str = int(test_str)
            1 / convert_str
            open('./missing.txt')
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except ValueError as e:
            print(f"Caught ValueError: {e}")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("\nTesting ValueError...")
    garden_operations('hello')
    print("\nTesting ZeroDivisionError...")
    garden_operations('0')
    print("\nTesting FileNotFoundError...")
    garden_operations('1')
    print("\nTesting KeyError...")
    garden_operations('key')
    print("\nTesting multiple errors together...")
    garden_operations('all')
    print("\nAll error types tested successfully!")


test_error_types()
