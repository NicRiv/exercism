def square(number):
    if number >= 1 and number <= 64:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")

def total():
    tam = 64
    total = int((1 - 2 ** tam) / (1 - 2)) - 1
    return total