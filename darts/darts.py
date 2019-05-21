def score(x, y):
    def test(x, y): 
        return x**2 + y**2

    if test(x, y) > 100:
        return 0
    elif test(x, y) > 25:
        return 1
    elif test(x, y) > 1:
        return 5
    else:
        return 10

