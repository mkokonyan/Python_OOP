from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self):
        self.car = Vehicle(fuel=10.0, horse_power=99.0)

    def test_init_creates_all_attributes(self):
        self.assertEqual(10.0, self.car.fuel)
        self.assertEqual(99.0, self.car.horse_power)
        self.assertEqual(1.25, self.car.fuel_consumption)
        self.assertEqual(10, self.car.capacity)

    def test_drive_fuel_calculation(self):
        self.assertEqual(10, self.car.fuel)
        self.car.drive(2)
        self.assertEqual(7.5, self.car.fuel)

    def test_drive_without_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(40)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_adds_fuel(self):
        self.car.drive(2)
        self.car.refuel(1)
        self.assertEqual(8.5, self.car.fuel)

    def test_refuel_limit_raise(self):
        self.car.drive(2)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(5)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_representation(self):
        result = str(self.car)
        expected_result = "The vehicle has 99.0 horse power with 10.0 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
