from project.train.train import Train

from unittest import TestCase, main


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train("Company", 6)

    def test_init_creates_all_attributes(self):
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)
        self.assertEqual("Company", self.train.name)
        self.assertEqual(6, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_full_train_raises(self):
        self.train.passengers = ["1", "2", "3", "4", "5", "6"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("7")
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_existing_passenger_raises(self):
        self.train.passengers = ["1", "2", "3", "4", "5"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("1")
        self.assertEqual("Passenger 1 Exists", str(ex.exception))

    def test_add_passenger_successfully(self):
        self.train.passengers = ["1", "2", "3", "4", "5"]
        self.assertEqual("Added passenger 6", self.train.add("6"))
        self.train.passengers = ["1", "2", "3", "4", "5", "6"]

    def test_remove_not_valid_passenger_raises(self):
        self.train.passengers = ["1", "2", "3", "4", "5"]
        with self.assertRaises(ValueError) as ex:
            self.train.remove("6")
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_passenger_successfully(self):
        self.train.passengers = ["1", "2", "3", "4", "5"]
        self.assertEqual("Removed 1", self.train.remove("1"))
        self.train.passengers = ["2", "3", "4", "5", "6"]


if __name__ == '__main__':
    main()
