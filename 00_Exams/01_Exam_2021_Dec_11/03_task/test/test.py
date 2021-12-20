from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("Chelsea")

    def test_init_creates_all_attributes(self):
        self.assertEqual("Chelsea", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_get_name_with_numbers_raises(self):
        with self.assertRaises(ValueError) as ex:
            team = Team("Chelsea_1")
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member_successfully(self):
        team = self.team.add_member(Lukaku=29, Werner=26)
        self.assertEqual({"Lukaku": 29, "Werner": 26}, self.team.members)
        self.assertEqual("Successfully added: Lukaku, Werner", team)

    def test_add_members_with_repeated_member_name(self):
        self.team.add_member(Lukaku=29, Werner=26)
        self.assertEqual({"Lukaku": 29, "Werner": 26}, self.team.members)
        team = self.team.add_member(Lukaku=32, Pulisic=24, Kepa=22)
        self.assertEqual({"Lukaku": 29, "Werner": 26, "Pulisic": 24, "Kepa": 22}, self.team.members)
        self.assertEqual("Successfully added: Pulisic, Kepa", team)

    def test_remove_member_not_existing_member(self):
        self.team.add_member(Lukaku=29, Werner=26)
        self.assertEqual("Member with name Kante does not exist", self.team.remove_member("Kante"))
        self.assertEqual({"Lukaku": 29, "Werner": 26}, self.team.members)

    def test_remove_member_successfully(self):
        self.team.add_member(Lukaku=29, Werner=26)
        removed_member = self.team.remove_member("Lukaku")
        self.assertEqual({"Werner": 26}, self.team.members)
        self.assertEqual("Member Lukaku removed", removed_member)

    def test_greater_than_members_true_result(self):
        self.team.add_member(Lukaku=29, Werner=26)
        self.assertEqual({"Lukaku": 29, "Werner": 26}, self.team.members)
        team_2 = Team("Liverpool")
        team_2.add_member(Firmino=30)
        self.assertEqual({"Firmino": 30}, team_2.members)
        self.assertTrue(self.team > team_2)

    def test_greater_than_members_false_result(self):
        self.team.add_member(Lukaku=29, Werner=26)
        self.assertEqual({"Lukaku": 29, "Werner": 26}, self.team.members)
        team_2 = Team("Liverpool")
        team_2.add_member(Firmino=30, Salah=29, Henderson=31)
        self.assertEqual({"Firmino": 30, "Salah": 29, "Henderson": 31}, team_2.members)
        self.assertFalse(self.team > team_2)

    def test_len_method(self):
        self.team.add_member(Lukaku=29, Werner=26)
        self.assertEqual(2, len(self.team))

    def test_add_method(self):
        self.team.add_member(Lukaku=29, Werner=26)
        self.assertEqual({"Lukaku": 29, "Werner": 26}, self.team.members)
        team_2 = Team("Liverpool")
        team_2.add_member(Firmino=30, Salah=29, Henderson=31)
        self.assertEqual({"Firmino": 30, "Salah": 29, "Henderson": 31}, team_2.members)
        new_team = self.team + team_2
        self.assertEqual("ChelseaLiverpool", new_team.name)
        self.assertEqual({"Lukaku": 29, "Werner": 26, "Firmino": 30, "Salah": 29, "Henderson": 31}, new_team.members)
        self.assertTrue(isinstance(new_team, Team))

    def test_str_representation(self):
        team = Team("Test")
        team.add_member(A=29, Q=26, B=42, D=26)
        expected_result = "Team name: Test\n" \
                          "Member: B - 42-years old\n" \
                          "Member: A - 29-years old\n" \
                          "Member: D - 26-years old\n" \
                          "Member: Q - 26-years old"
        self.assertEqual(expected_result, str(team))


if __name__ == '__main__':
    main()
