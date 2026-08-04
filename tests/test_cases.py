import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import get_grade_info

def run_tests():
    print("--- Running Test Cases (70% Passing Rate Table) ---")
    
    # Test Case 1: Excellent (1.00 / A)
    res1 = get_grade_info(99)
    print(f"Test 1 (Score: 99)  -> Expected: 1.00 (A) Excellent, Got: {res1['numerical']} ({res1['letter']}) {res1['description']}")
    assert res1["numerical"] == 1.00 and res1["letter"] == "A"

    # Test Case 2: Very Good (1.75 / B)
    res2 = get_grade_info(89.5)
    print(f"Test 2 (Score: 89.5) -> Expected: 1.75 (B) Very Good, Got: {res2['numerical']} ({res2['letter']}) {res2['description']}")
    assert res2["numerical"] == 1.75 and res2["letter"] == "B"

    # Test Case 3: Fair (2.50 / C)
    res3 = get_grade_info(78)
    print(f"Test 3 (Score: 78)  -> Expected: 2.50 (C) Fair, Got: {res3['numerical']} ({res3['letter']}) {res3['description']}")
    assert res3["numerical"] == 2.50 and res3["letter"] == "C"

    print("All test cases passed successfully!")

if __name__ == "__main__":
    run_tests()