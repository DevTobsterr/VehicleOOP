import time

noise = "Broom Broom"
class Vehicle:
    def __init__(self, numberOfWheels, tankType, numberOfSeats, maxSpeed):
        self.numberOfWheels = numberOfWheels
        self.numberOfSeats = numberOfSeats
        self.tankType = tankType
        self.maxSpeed = maxSpeed

    #
    # def set_numberOfWheels(self, number=2):
    #     self.numberOfSeats = number

    def get_numberOfWheels(self):
        return self.numberOfWheels

    def make_noise(self, noise):
        print(noise)


if __name__ == '__main__':
    seat_model=Vehicle(4,"petrol", 5, 250)
    print(seat_model.numberOfSeats)

    # seat_model.set_numberOfWheels()
    print(seat_model.get_numberOfWheels())

    seat_model.make_noise(noise)



input()
