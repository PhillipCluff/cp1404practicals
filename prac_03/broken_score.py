"""
score checking program with function
"""


def main():
    score = float(input("Enter score: "))
    result = score_checker(score)
    print(result)


def score_checker(score):

    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
