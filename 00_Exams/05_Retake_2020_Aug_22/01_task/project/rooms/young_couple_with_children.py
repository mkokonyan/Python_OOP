from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, members_count=2 + len(children))
        self.room_cost = 30
        self.children += list(children)
        self.members_count = 2 + len(children)
        self.appliances = [TV()] * self.members_count + \
                          [Fridge()] * self.members_count + \
                          [Laptop()] * self.members_count

        self.calculate_expenses(self.appliances, self.children)


