
class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        searched_name_list = [name.username for name in self.user_records if name.user_id == user_id]
        if user_id not in [id.user_id for id in self.user_records]:
            return f"There is no user with id = {user_id}!"
        if searched_name_list:
            searched_name = searched_name_list[0]
            if new_username == searched_name:
                return "Please check again the provided username - it should be different than the username used so far!"
            if searched_name in self.rented_books:
                self.rented_books[new_username] = self.rented_books.pop(searched_name)
            for i in range(len(self.user_records)):
                if self.user_records[i].username == searched_name:
                    self.user_records[i].username = new_username
        return f"Username successfully changed to: {new_username} for userid: {user_id}"

