class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km 
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def receipt(self):
        print('RECEIPT')
        print('================')
        print(f'Your fare is {self.fare}')
        print(f'The distance was {self.distance}, and the rate was {self.rate_per_km}')
        print('================')
def main():
    driver_1=TaxiRide(4)
    driver_2=TaxiRide(2)

    driver_1.rate_per_km = 4
    driver_1.distance = 100
    driver_1.calculate_fare(driver_1.distance)
    driver_2.rate_per_km = 2
    driver_2.distance = 100
    driver_2.calculate_fare(driver_2.distance)

    driver_1.receipt()
    driver_2.receipt()


    '''print('RECEIPT')
    print('================')
    print(f'Your fare is {driver_1.fare}')
    print(f'The distance was {driver_1.distance}, and the rate was {driver_1.rate_per_km}')
    print('================')
    print(f'Your fare is {driver_2.fare}')
    print(f'The distance was {driver_2.distance}, and the rate was {driver_2.rate_per_km}')
    print('================')'''


if __name__ == "__main__":
    main()
