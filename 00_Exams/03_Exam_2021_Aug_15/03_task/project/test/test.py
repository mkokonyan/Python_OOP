from project.pet_shop import PetShop

from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self):
        self.pet_shop = PetShop("Shop")

    def test_init_creates_all_attributes(self):
        self.assertEqual("Shop", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_quantity_below_zero_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("Granules", -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_with_missing_type(self):
        trigger = self.pet_shop.add_food("Granules", 100.00)
        self.assertEqual({"Granules": 100.00}, self.pet_shop.food)
        self.assertEqual(f"Successfully added 100.00 grams of Granules.", trigger)

    def test_add_food_with_existing_type(self):
        self.pet_shop.add_food("Granules", 100.00)
        self.pet_shop.add_food("Granules", 50.50)
        self.assertEqual({"Granules": 150.50}, self.pet_shop.food)

    def test_add_pet_successful(self):
        trigger = self.pet_shop.add_pet("Sharo")
        self.assertEqual(["Sharo"], self.pet_shop.pets)
        self.assertEqual("Successfully added Sharo.", trigger)

    def test_add_pet_existing_name_raises(self):
        self.pet_shop.add_pet("Sharo")
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Sharo")
        self.assertEqual(["Sharo"], self.pet_shop.pets)
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_not_valid_name_raises(self):
        self.pet_shop.add_pet("Sharo")
        self.pet_shop.add_food("Granules", 100.00)
        self.assertEqual({"Granules": 100.00}, self.pet_shop.food)
        self.assertEqual(["Sharo"], self.pet_shop.pets)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Granules", "Balkan")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_not_existing_food_type(self):
        self.pet_shop.add_pet("Sharo")
        self.pet_shop.add_food("Granules", 100.00)
        self.assertEqual(f'You do not have fish', self.pet_shop.feed_pet("fish", "Sharo"))

    def test_feed_pet_low_amount_of_food_return_message(self):
        self.pet_shop.add_pet("Sharo")
        self.pet_shop.add_food("Granules", 99.00)
        self.assertEqual("Adding food...", self.pet_shop.feed_pet("Granules", "Sharo"))
        self.pet_shop.add_food("Granules", 1099.00)

    def test_feed_pet_low_amount_of_food_calculation(self):
        self.pet_shop.add_pet("Sharo")
        self.pet_shop.add_food("Granules", 99.00)
        self.pet_shop.feed_pet("Granules", "Sharo")
        self.assertEqual({"Granules": 1099.00}, self.pet_shop.food)

    def test_feed_pet_successful_return_message(self):
        self.pet_shop.add_pet("Sharo")
        self.pet_shop.add_food("Granules", 101.00)
        self.assertEqual("Sharo was successfully fed", self.pet_shop.feed_pet("Granules", "Sharo"))
        self.assertEqual({"Granules": 1.00}, self.pet_shop.food)

    def test_feed_pet_successful_calculation(self):
        self.pet_shop.add_pet("Sharo")
        self.pet_shop.add_food("Granules", 101.00)
        self.pet_shop.feed_pet("Granules", "Sharo")
        self.assertEqual({"Granules": 1.00}, self.pet_shop.food)

    def test_class_representation(self):
        self.pet_shop.add_pet("Sharo")
        self.pet_shop.add_pet("Balkan")
        self.assertEqual('Shop Shop:\nPets: Sharo, Balkan', repr(self.pet_shop))


if __name__ == '__main__':
    main()
