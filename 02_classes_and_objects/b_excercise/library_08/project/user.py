
class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        for book in library.rented_books.values():
            if book_name in book:
                return f'The book "{book_name}" is already rented and will be available in {book[book_name]} days!'
        if author in library.books_available:
            if book_name in library.books_available[author]:
                library.books_available[author].remove(book_name)
                if not self.username in library.rented_books:
                    library.rented_books[self.username] = {}
                self.books.append(book_name)
                library.rented_books[self.username].update({book_name: days_to_return})
                return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author, book_name, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        self.books.remove(book_name)
        del library.rented_books[self.username][book_name]
        if author not in library.books_available:
            library.books_available[author] = [book_name]
        library.books_available[author].append(book_name)

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"

    def info(self):
        return f"{', '.join(sorted(self.books))}"
