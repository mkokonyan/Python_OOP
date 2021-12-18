from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero(username="Warlock", level=5, health=100.0, damage=50.0)
        self.enemy_hero = Hero(username="Warrior", level=2, health=300.0, damage=40.0)

    def test_init_creates_all_attributes(self):
        self.assertEqual("Warlock", self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(50.0, self.hero.damage)

    def test_battle_enemy_name_raises(self):
        enemy_hero = Hero(username="Warlock", level=10, health=100.0, damage=120.0)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_lower_than_zero(self):
        self.hero.health = -20
        self.assertEqual(-20.0, self.hero.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_enemy_hero_health_lower_than_zero(self):
        self.enemy_hero.health = -20
        self.assertEqual(-20.0, self.enemy_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight Warrior. He needs to rest", str(ex.exception))

    def test_battle_hero_lose_case_params(self):
        self.hero.battle(self.enemy_hero)
        self.assertEqual(20, self.hero.health)
        self.assertEqual(55.0, self.enemy_hero.health)
        self.assertEqual(3, self.enemy_hero.level)
        self.assertEqual(45, self.enemy_hero.damage)

    def test_battle_hero_win_case_params(self):
        enemy_hero = Hero(username="Warrior", level=2, health=250.0, damage=40.0)
        self.hero.battle(enemy_hero)
        self.assertEqual(25, self.hero.health)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(55, self.hero.damage)

    def test_battle_hero_lose_case_return(self):
        self.assertEqual("You lose", self.hero.battle(self.enemy_hero))

    def test_battle_hero_draw_case_return(self):
        self.enemy_hero = Hero(username="Warrior", level=5, health=100.0, damage=40.0)
        self.assertEqual("Draw", self.hero.battle(self.enemy_hero))

    def test_battle_hero_win_case_return(self):
        self.enemy_hero = Hero(username="Warrior", level=1, health=1, damage=1)
        self.assertEqual("You win", self.hero.battle(self.enemy_hero))

    def test_battle_str_represent(self):
        result = str(self.hero)
        expected_result = "Hero Warlock: 5 lvl\nHealth: 100.0\nDamage: 50.0\n"
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
