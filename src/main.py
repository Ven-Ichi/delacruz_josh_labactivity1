def get_grade_info(score, passing_rate=70):
    """
    Evaluates score based on Mapúa grading scale table.
    Returns a dictionary with Numerical Grade, Letter Grade, and Description.
    """
    if passing_rate == 70:
        if 98 <= score <= 100:
            return {"numerical": 1.00, "letter": "A", "description": "Excellent"}
        elif 95 <= score < 98:
            return {"numerical": 1.25, "letter": "A-", "description": "Highly Meritorious"}
        elif 91 <= score < 95:
            return {"numerical": 1.50, "letter": "B+", "description": "Meritorious"}
        elif 88 <= score < 91:
            return {"numerical": 1.75, "letter": "B", "description": "Very Good"}
        elif 85 <= score < 88:
            return {"numerical": 2.00, "letter": "B-", "description": "Good"}
        elif 81 <= score < 85:
            return {"numerical": 2.25, "letter": "C+", "description": "Satisfactory"}
        elif 77 <= score < 81:
            return {"numerical": 2.50, "letter": "C", "description": "Fair"}
        else:
            return {"numerical": 5.00, "letter": "F", "description": "Failed"}
    elif passing_rate == 80:
        if 98 <= score <= 100:
            return {"numerical": 1.00, "letter": "A", "description": "Excellent"}
        elif 96 <= score < 98:
            return {"numerical": 1.25, "letter": "A-", "description": "Highly Meritorious"}
        elif 94 <= score < 96:
            return {"numerical": 1.50, "letter": "B+", "description": "Meritorious"}
        elif 92 <= score < 94:
            return {"numerical": 1.75, "letter": "B", "description": "Very Good"}
        elif 90 <= score < 92:
            return {"numerical": 2.00, "letter": "B-", "description": "Good"}
        elif 88 <= score < 90:
            return {"numerical": 2.25, "letter": "C+", "description": "Satisfactory"}
        elif 86 <= score < 88:
            return {"numerical": 2.50, "letter": "C", "description": "Fair"}
        else:
            return {"numerical": 5.00, "letter": "F", "description": "Failed"}
    else:
        raise ValueError("Invalid passing rate option. Use 70 or 80.")

if __name__ == "__main__":
    score = 96.5
    result = get_grade_info(score, passing_rate=70)
    print(f"Score: {score} -> Grade: {result['numerical']} ({result['letter']}) - {result['description']}")