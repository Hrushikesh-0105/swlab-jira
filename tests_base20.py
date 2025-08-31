from base20 import base20

def run_tests():
    """
    Runs a series of simple tests for the base20 function using conditional checks.
    """
    print("--- Running Simple Base-20 Converter Tests ---")
    all_tests_passed = True

    # Test case 1: Zero
    expected_zero = "A"
    actual_zero = base20(0)
    if actual_zero == expected_zero:
        print("Test for 0 passed.")
    else:
        print(f"Test failed for 0: Expected {expected_zero}, got {actual_zero}")
        all_tests_passed = False

    # Test case 2: Positive numbers
    expected_positive = "BAA"
    actual_positive = base20(400)
    if actual_positive == expected_positive:
        print("Test for 400 passed.")
    else:
        print(f"Test failed for 400: Expected {expected_positive}, got {actual_positive}")
        all_tests_passed = False

    expected_positive_2 = "BBB"
    actual_positive_2 = base20(421)
    if actual_positive_2 == expected_positive_2:
        print("Test for 421 passed.")
    else:
        print(f"Test failed for 421: Expected {expected_positive_2}, got {actual_positive_2}")
        all_tests_passed = False
    
    # Test case 3: Negative numbers
    expected_negative = "-BAA"
    actual_negative = base20(-400)
    if actual_negative == expected_negative:
        print("Test for -400 passed.")
    else:
        print(f"Test failed for -400: Expected {expected_negative}, got {actual_negative}")
        all_tests_passed = False

    expected_negative_2 = "-B"
    actual_negative_2 = base20(-1)
    if actual_negative_2 == expected_negative_2:
        print("Test for -1 passed.")
    else:
        print(f"Test failed for -1: Expected {expected_negative_2}, got {actual_negative_2}")
        all_tests_passed = False

    print("\n--- Test Summary ---")
    if all_tests_passed:
        print("All tests passed successfully!")
    else:
        print("Some tests failed.")


if __name__ == "__main__":
    run_tests()