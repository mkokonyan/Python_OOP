from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("UACEG")

    def test_init_creates_all_attributes(self):
        self.assertEqual("UACEG", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_setter_name_raises_exception(self):
        with self.assertRaises(ValueError) as ex:
            library = Library("")
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_adding_book(self):
        self.library.add_book("J.K.Rowling", "HARRY POTTER AND THE ORDER OF THE PHOENIX")
        self.assertEqual({"J.K.Rowling": ["HARRY POTTER AND THE ORDER OF THE PHOENIX"]}, self.library.books_by_authors)
        self.library.add_book("J.K.Rowling", "HARRY POTTER AND THE HALF-BLOOD PRINCE")
        self.assertEqual(
            {"J.K.Rowling": ["HARRY POTTER AND THE ORDER OF THE PHOENIX", "HARRY POTTER AND THE HALF-BLOOD PRINCE"]},
            self.library.books_by_authors)
        self.library.add_book("J.K.Rowling", "HARRY POTTER AND THE HALF-BLOOD PRINCE")
        self.assertEqual(
            {"J.K.Rowling": ["HARRY POTTER AND THE ORDER OF THE PHOENIX", "HARRY POTTER AND THE HALF-BLOOD PRINCE"]},
            self.library.books_by_authors)

    def test_add_member_successfully(self):
        self.library.add_reader("Martin")
        self.assertEqual({"Martin": []}, self.library.readers)

    def test_add_registered_member(self):
        self.library.add_reader("Martin")

        self.assertEqual("Martin is already registered in the UACEG library.", self.library.add_reader("Martin"))

    def test_rent_book_not_valid_reader(self):
        self.assertEqual("Martin is not registered in the UACEG Library.",
                         self.library.rent_book("Martin", "J.K.Rowling", "HARRY POTTER AND THE ORDER OF THE PHOENIX"))

    def test_rent_book_not_valid_author(self):
        self.library.add_reader("Martin")
        self.assertEqual("UACEG Library does not have any Nakov's books.",
                         self.library.rent_book("Martin", "Nakov", "Python Basics"))

    def test_rent_book_not_valid_book_title(self):
        self.library.add_reader("Martin")
        self.library.add_book("J.K.Rowling", "HARRY POTTER AND THE ORDER OF THE PHOENIX")
        self.library.add_book("J.K.Rowling", "HARRY POTTER AND THE HALF-BLOOD PRINCE")
        self.assertEqual('UACEG Library does not have J.K.Rowling\'s "Python Basics".',
                         self.library.rent_book("Martin", "J.K.Rowling", "Python Basics"))

    def test_rent_book_successful(self):
        self.library.add_reader("Martin")
        self.assertEqual({"Martin": []}, self.library.readers)
        self.library.add_book("J.K.Rowling", "HARRY POTTER AND THE ORDER OF THE PHOENIX")
        self.library.add_book("J.K.Rowling", "HARRY POTTER AND THE HALF-BLOOD PRINCE")
        self.assertEqual(
            {"J.K.Rowling": ["HARRY POTTER AND THE ORDER OF THE PHOENIX", "HARRY POTTER AND THE HALF-BLOOD PRINCE"]},
            self.library.books_by_authors)
        self.library.rent_book("Martin", "J.K.Rowling", "HARRY POTTER AND THE HALF-BLOOD PRINCE")
        self.assertEqual({"Martin": [{"J.K.Rowling": "HARRY POTTER AND THE HALF-BLOOD PRINCE"}]}, self.library.readers)
        self.assertEqual(
            {"J.K.Rowling": ["HARRY POTTER AND THE ORDER OF THE PHOENIX"]},
            self.library.books_by_authors)


if __name__ == '__main__':
    main()
