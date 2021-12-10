class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def is_enough_capacity(self, person):
        if person == "animals":
            if len(self.animals) < self.__animal_capacity:
                return True
        elif person == "workers":
            if len(self.workers) < self.__workers_capacity:
                return True
        return False

    def is_enough_budget(self, price):
        if self.__budget >= price:
            return True
        return False

    def add_animal(self, animal, price):
        if not self.is_enough_budget(price) and self.is_enough_capacity("animals"):
            return "Not enough budget"
        if not self.is_enough_capacity("animals"):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if not self.is_enough_capacity("workers"):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        worker_obj = [w for w in self.workers if w.name == worker_name]
        if not worker_obj:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker_obj[0])
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        total_workers_salaries = sum([w.salary for w in self.workers])
        if not self.is_enough_budget(total_workers_salaries):
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_workers_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_animals_costs = sum([w.money_for_care for w in self.animals])
        if not self.is_enough_budget(total_animals_costs):
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_animals_costs
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        cheetahs = []
        tigers = []
        lions = []

        for i in range(len(self.animals)):
            if self.animals[i].__class__.__name__ == "Lion":
                lions.append(self.animals[i])
            elif self.animals[i].__class__.__name__ == "Tiger":
                tigers.append(self.animals[i])
            elif self.animals[i].__class__.__name__ == "Cheetah":
                cheetahs.append(self.animals[i])

        nl = "\n"
        result = f"You have {len(self.animals)} animals\n" \
                 f"----- {len(lions)} Lions:\n{nl.join(map(str, lions))}\n" \
                 f"----- {len(tigers)} Tigers:\n{nl.join(map(str, tigers))}\n" \
                 f"----- {len(cheetahs)} Cheetahs:\n{nl.join(map(str, cheetahs))}"
        return result

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []

        for i in range(len(self.workers)):
            if self.workers[i].__class__.__name__ == "Keeper":
                keepers.append(self.workers[i])
            elif self.workers[i].__class__.__name__ == "Caretaker":
                caretakers.append(self.workers[i])
            elif self.workers[i].__class__.__name__ == "Vet":
                vets.append(self.workers[i])

        nl = "\n"
        result = f"You have {len(self.workers)} workers\n" \
                 f"----- {len(keepers)} Keepers:\n{nl.join(map(str, keepers))}\n" \
                 f"----- {len(caretakers)} Caretakers:\n{nl.join(map(str, caretakers))}\n" \
                 f"----- {len(vets)} Vets:\n{nl.join(map(str, vets))}"
        return result
