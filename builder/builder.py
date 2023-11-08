from sport_car import SportsCarBuilder
from regular_car import RegularCarBuilder

def main():
    car_builder = SportsCarBuilder()
    car_builder.build_wheels()
    car_builder.build_engine()
    car_builder.build_body()

    car = car_builder.get_car()
    print("The sports car has {} wheels, a {} engine, and a {} body.".format(
        car.get_wheels(), car.get_engine(), car.get_body()))

    car_builder_2 = RegularCarBuilder()
    car_builder_2.build_body()
    car_builder_2.build_engine()
    car_builder_2.build_wheels()

    car2 = car_builder_2.get_car()
    print("The regular car has {} wheels, a {} engine, and a {} body.".format(
        car2.get_wheels(), car2.get_engine(), car2.get_body()))

if __name__ == "__main__":
    main()
