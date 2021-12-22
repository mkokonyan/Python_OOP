from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = name

    def add_food(self, food_type: str, name: str, price: float):
        if name in [food.name for food in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type not in ["Bread", "Cake"]:
            return
        if food_type == "Bread":
            self.food_menu.append(Bread(name, price))
        elif food_type == "Cake":
            self.food_menu.append(Cake(name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if name in [drink.name for drink in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type not in ["Tea", "Water"]:
            return
        if drink_type == "Tea":
            self.drinks_menu.append(Tea(name, portion, brand))
        elif drink_type == "Water":
            self.drinks_menu.append(Water(name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_number in [table.table_number for table in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type not in ["InsideTable", "OutsideTable"]:
            return
        if table_type == "InsideTable":
            self.tables_repository.append(InsideTable(table_number, capacity))
        elif table_type == "OutsideTable":
            self.tables_repository.append(OutsideTable(table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        if table_number not in [table.table_number for table in self.tables_repository]:
            return f"Could not find table {table_number}"
        current_table = [table for table in self.tables_repository if table_number == table.table_number][0]
        ordered_food = []
        invalid_food = []
        for food_to_add in args:
            searched_food = [food for food in self.food_menu if food_to_add == food.name]
            if searched_food:
                current_table.order_food(searched_food[0])
                ordered_food.append(searched_food[0])
            else:
                invalid_food.append(food_to_add)

        ordered_food_data = '\n'.join([repr(food) for food in ordered_food])
        unordered_food_data = '\n'.join(invalid_food)
        result = f"Table {table_number} ordered:\n{ordered_food_data}\n" \
                 f"{self.name} does not have in the menu:\n{unordered_food_data}"
        return result

    def order_drink(self, table_number: int, *args):
        if table_number not in [table.table_number for table in self.tables_repository]:
            return f"Could not find table {table_number}"
        current_table = [table for table in self.tables_repository if table_number == table.table_number][0]
        ordered_drinks = []
        invalid_drinks = []
        for drink_to_add in args:
            searched_drink = [drink for drink in self.drinks_menu if drink_to_add == drink.name]
            if searched_drink:
                current_table.order_drink(searched_drink[0])
                ordered_drinks.append(searched_drink[0])

            else:
                invalid_drinks.append(drink_to_add)

        ordered_drinks_data = '\n'.join([repr(drink) for drink in ordered_drinks])
        unordered_drinks_data = '\n'.join(invalid_drinks)
        result = f"Table {table_number} ordered:\n{ordered_drinks_data}\n" \
                 f"{self.name} does not have in the menu:\n{unordered_drinks_data}"
        return result

    def leave_table(self, table_number: int):
        if [table for table in self.tables_repository if table_number == table.table_number]:
            searched_table = [table for table in self.tables_repository if table_number == table.table_number][0]
            table_bill = searched_table.get_bill()
            searched_table.clear()
            self.total_income += table_bill
            return f"Table: {table_number}\nBill: {table_bill:.2f}"

    def get_free_tables_info(self):
        free_tables = [table for table in self.tables_repository if not table.is_reserved]
        result_data = []
        if free_tables:
            for table in free_tables:
                result_data.append(table.free_table_info())
        return '\n'.join(result_data)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"



bakery = Bakery("Chochko")

print(bakery.add_food("Bread", "Bread1", 2.20))
print(bakery.add_food("Cake", "Cake1", 4.50))
print(bakery.add_food("Bread", "Bread2", 5.20))
print(bakery.add_food("Cake", "Cake2", 11.50))

print(bakery.add_drink("Tea", "Tea1", 200, "fruittea"))
print(bakery.add_drink("Water", "Water1", 100, "normal"))
print(bakery.add_drink("Tea", "Tea2", 250, "blacktea"))
print(bakery.add_drink("Water", "Water2", 220, "carbonated"))


print(bakery.add_table("InsideTable", 1, 4))
print(bakery.add_table("InsideTable", 2, 7))
print(bakery.add_table("InsideTable", 3, 5))
print(bakery.add_table("OutsideTable", 51, 12))
print(bakery.add_table("OutsideTable", 52, 5))
print(bakery.add_table("OutsideTable", 53, 5))

print(bakery.reserve_table(6))
print(bakery.reserve_table(11))
print(bakery.reserve_table(2))
print(bakery.order_food(-2, "Bread1", "Cake1", "meat1", "Cake2", "meat2"))
print(bakery.order_food(2, "Bread1", "Cake1", "meat1", "Cake2", "meat2"))

print(bakery.order_drink(124, "Tea1", "Alcohol", "Water1", "Tea2", "Water2", "alcohol2"))
print(bakery.order_drink(51, "Tea1", "Alcohol", "Water1", "Tea2", "Water2", "alcohol2"))

print(bakery.leave_table(51))
print(bakery.leave_table(2))
print(bakery.get_free_tables_info())
print(bakery.get_total_income())