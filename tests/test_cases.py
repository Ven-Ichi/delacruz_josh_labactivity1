import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import calculate_grade

def run_tests():
    print("--- Running Test Cases ---")
    
    # Test Case 1
    res1 = calculate_grade(95)
    print(f"Test 1 (Score: 95) -> Expected: A, Got: {res1}")
    assert res1 == "A"

    # Test Case 2
    res2 = calculate_grade(75)
    print(f"Test 2 (Score: 75) -> Expected: C, Got: {res2}")
    assert res2 == "C"

    # Test Case 3
    res3 = calculate_grade(50)
    print(f"Test 3 (Score: 50) -> Expected: F, Got: {res3}")
    assert res3 == "F"

    print("All test cases passed successfully!")

if __name__ == "__main__":
    run_tests()