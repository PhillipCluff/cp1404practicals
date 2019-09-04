import random


def main():
    all_quick_picks = []
    number_of_quick_picks = int(input("How many quick picks? "))
    for number_of_quick_picks in range(number_of_quick_picks):
        one_quick_pick = make_a_quick_pick()
        all_quick_picks.append(one_quick_pick)
    for quick_pick in all_quick_picks:
        for i in quick_pick:
            print("{:>2} ".format(i), end='')
        print()


def make_a_quick_pick():
    quick_picks = []

    for pick in range(6):
        pick = random.randint(1, 45)
        if pick not in quick_picks:
            quick_picks.append(pick)

    quick_picks.sort()
    return quick_picks


main()
