import timeit


def is_armstrong_number(number):
    result = [int(x) ** len(str(number)) for x in str(number)]
    return sum(result) == number


def is_armstrong_number2(number):
    result = 0
    for x in range(len(str(number))):
        result += int(str(number)[x]) ** len(str(number))
    return result == number



def benchmark(function, number=1000, repeat=10):
    times = timeit.repeat(function, number=number, globals=globals())

    time = min(times) / number
    precision = 8
    print(f"{number} loops, best of {repeat}: {time:.7f}")

benchmark("is_armstrong_number(15300)")
print(is_armstrong_number(153))
benchmark("is_armstrong_number2(15300)")
print(is_armstrong_number2(153))
