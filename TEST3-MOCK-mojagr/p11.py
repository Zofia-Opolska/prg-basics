def f(cars, order):
    if order == 1:
        return sorted(cars, key=lambda d: list(d.keys())[0])
    elif order == 2:
        return sorted(cars, key=lambda d: list(d.values())[0], reverse=True)
