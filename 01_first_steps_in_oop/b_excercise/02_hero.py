class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int):
        if damage >= self.health:
            self.health = 0
            return f"{self.name} was defeated"
        self.health -= damage

    def heal(self, heal: int):
        self.health += heal


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
hero_2 = Hero("Martin", 150)
print(hero.defend(99))
print(hero.defend(1))

