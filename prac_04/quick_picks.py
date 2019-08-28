import random


def main():
    all_quick_picks = []
    number_of_quick_picks = int(input("How many quick picks? "))
    for number_of_quick_picks in range(number_of_quick_picks):
        one_quick_pick = make_a_quick_pick()
        all_quick_picks.append(one_quick_pick)
    for all_quick_pick in all_quick_pick in all_quick_picks
        print(all_quick_pick[0])
# TODO enumirate through list thing


def make_a_quick_pick():
    quick_picks = []
    repeats = []
    for pick in range(6):
        pick = random.randint(1, 45)
        if pick in quick_picks:
            repeats.append(pick)
        else:
            quick_picks.append(pick)
    quick_picks.sort()
    return quick_picks


main()
