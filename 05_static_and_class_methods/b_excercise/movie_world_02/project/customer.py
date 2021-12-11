class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        return f"{self.id}: {self.name} of age " \
               f"{self.age} has {len(self.rented_dvds)} " \
               f"rented DVD's ({', '.join(list(map(lambda x: str(x.name), self.rented_dvds)))})"

