def f(car,order):
    if order == 1: #alfabetycznie
        return sorted(cars, key=lambda d: list(d.keys())[0])

    elif order == 2: #według przejechanych km
        filtered = [d for d in cars if list(d.values())[0] >= 200]
        return sorted(filtered, key=lambda d: list(d.values())[0], reverse=True)




cars = [{"KR333":138},{"WL555":338},{"DB444":438},{"MC222":538}]
# print(f(cars,1))
print(f(cars,2))

