
def is_armstrong_number(number):
    result = [int(x) ** len(str(number)) for x in str(number)]
    return sum(result) == number
