def add(a, b):
    return a + b


def run_tests():
    test_cases = [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (10, 5, 15),
    ]

    for a, b, expected in test_cases:
        result = add(a, b)
        if result != expected:
            print(f"Test Failed ❌ for inputs ({a}, {b}) | Expected: {expected}, Got: {result}")
            return False

    print("All Tests Passed ✅🔥")
    return True


if __name__ == "__main__":
    if not run_tests():
        exit(1)
