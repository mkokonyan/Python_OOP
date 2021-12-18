from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "Tiger", "Grr")

    def test_init_creates_all_attributes(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("Tiger", self.mammal.type)
        self.assertEqual("Grr", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("Test makes Grr", self.mammal.make_sound())

    def test_get_kind(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        result = self.mammal.info()
        expected_result = "Test is of type Tiger"
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
