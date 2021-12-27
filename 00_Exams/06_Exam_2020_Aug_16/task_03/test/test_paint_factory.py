from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.factory = PaintFactory("Fabric", 14)

    def test_init_creates_all_attributes(self):
        self.assertEqual("Fabric", self.factory.name)
        self.assertEqual(14, self.factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual({}, self.factory.products)

    def test_can_add(self):
        self.ingredients = {"white": 4}
        self.assertEqual(True, self.factory.can_add(4))

    def test_add_ingredient_not_allowed_product_type_raise(self):
        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient("purple", 5)
        self.assertEqual("Ingredient of type purple not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredient_not_enough_space_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient("white", 15)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient_successfully(self):
        self.factory.add_ingredient("white", 4)
        self.assertTrue(self.factory.can_add(4))
        self.assertEqual({"white": 4}, self.factory.ingredients)
        self.factory.add_ingredient("white", 6)
        self.assertEqual({"white": 10}, self.factory.ingredients)
        self.factory.add_ingredient("yellow", 2)
        self.assertEqual({"white": 10, "yellow": 2}, self.factory.ingredients)

    def test_remove_ingredient_invalid_factory_raise(self):
        self.factory.add_ingredient("white", 4)
        self.assertTrue(self.factory.can_add(4))
        self.assertEqual({"white": 4}, self.factory.ingredients)
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient("yellow", 2)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_ingredient_negative_value_raise(self):
        self.factory.add_ingredient("white", 4)
        self.assertTrue(self.factory.can_add(4))
        self.assertEqual({"white": 4}, self.factory.ingredients)
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient("white", 5)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_successfully(self):
        self.factory.add_ingredient("white", 4)
        self.assertTrue(self.factory.can_add(4))
        self.assertEqual({"white": 4}, self.factory.ingredients)
        self.factory.remove_ingredient("white", 3)
        self.assertEqual({"white": 1}, self.factory.ingredients)

    def test_represent_method(self):
        self.factory.add_ingredient("white", 4)
        self.assertEqual({"white": 4}, self.factory.ingredients)
        self.factory.add_ingredient("white", 6)
        self.assertEqual({"white": 10}, self.factory.ingredients)
        self.factory.add_ingredient("yellow", 2)
        self.assertEqual({"white": 10, "yellow": 2}, self.factory.ingredients)
        expected_result = "Factory name: Fabric with capacity 14.\n" \
                          "white: 10\nyellow: 2\n"
        self.assertEqual(expected_result, repr(self.factory))


if __name__ == '__main__':
    main()
