def score(x, y):

    diagonal = (x ** 2 + y ** 2) ** (1/2)

    if (diagonal <= 1):
        return 10

    if (diagonal > 1) and (diagonal <= 5):
        return 5

    if (diagonal > 5) and (diagonal <= 10):
        return 1

    if (diagonal > 10):
        return 0
