# Score categories
# Change the values as you see fit
YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "fullhouse"
FOUR_OF_A_KIND = "fourofakind"
LITTLE_STRAIGHT = "little"
BIG_STRAIGHT = "big"
CHOICE = "choice"


def score(dice, category):
    print(category)
    numbers = {
        "ones": 1,
        "twos": 2,
        "threes": 3,
        "fours": 4,
        "fives": 5,
        "sixes": 6
    }

    if category == YACHT:
        return 50 if dice.count(dice[0]) == len(dice) else 0
    elif category == CHOICE:
        total = 0
        for d in dice:
            total += d
        return total
    elif category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return (numbers[category] * dice.count(numbers[category])
                    if dice.count(numbers[category]) > 0 else 0)
    elif category in (FULL_HOUSE, FOUR_OF_A_KIND):
        three = 0
        two = 0
        for d in dice:
            if category == FOUR_OF_A_KIND:
                if dice.count(d) >= 4:
                    return 4 * d
                else:
                    return 0
            else:
                if dice.count(d) in (4, 5):
                    return 0
                elif dice.count(d) == 3:
                    three = d
                elif dice.count(d) == 2:
                    two = d
        if three > 0 and two > 0:
            return 3 * three + 2 * two
        else:
            return 0
    elif category in (BIG_STRAIGHT, LITTLE_STRAIGHT):
        dice.sort()
        if (category == BIG_STRAIGHT and dice[0] != 2 or 
            category == LITTLE_STRAIGHT and dice[0] != 1):
            return 0
        elif category == BIG_STRAIGHT and dice == [2, 3, 4, 5, 6]:
            return 30
        elif category == LITTLE_STRAIGHT and dice == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0
