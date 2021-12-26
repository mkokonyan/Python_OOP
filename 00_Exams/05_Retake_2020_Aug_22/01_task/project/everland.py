from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([(room.expenses + room.room_cost) for room in self.rooms])
        return f"Monthly consumtions: {total_consumption:.2f}$."

    def pay(self):
        result = ""
        for room in self.rooms:
            total_room_expenses = room.expenses + room.room_cost
            new_budget = room.budget - total_room_expenses
            if new_budget >= 0:
                room.budget = new_budget
                result += f"{room.family_name} paid {total_room_expenses:.2f}$ and have {new_budget:.2f}$ left.\n"
            else:
                self.rooms.remove(room)
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
        return result.strip()

    def status(self):
        result = f"Total population: {sum([room.members_count for room in self.rooms])}\n"
        child_expenses = 0
        for room in self.rooms:
            room_data = f"{room.name} with {room.members_count} members. " \
                        f"Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if room.children:
                for i in range(len(room.children)):
                    child_expenses += room.children[i].cost*30
                    room_data += f"--- Child {i + 1} monthly cost: {room.children[i].cost*30:.2f}$\n"
            if room.appliances:
                room_data += f"--- Appliances monthly cost: {room.expenses-child_expenses:.2f}$\n"
            result += room_data
        return result.strip()

# from rooms.young_couple import YoungCouple
# from rooms.young_couple_with_children import YoungCoupleWithChildren
# from people.child import Child
#
# everland = Everland()
#
# young_couple = YoungCouple("Johnsons", 150, 205)
#
# child1 = Child(5, 1, 2, 1)
# child2 = Child(3, 2)
# young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
#
# everland.add_room(young_couple)
# everland.add_room(young_couple_with_children)
#
# print(everland.get_monthly_consumptions())
# print(everland.pay())
# print(everland.status())
