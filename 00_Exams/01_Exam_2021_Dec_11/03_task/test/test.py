from unittest import TestCase, main

from project.team import Team


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("Chelsea")

    def test_init_creates_all_attributes(self):
        self.assertEqual("Chelsea", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            team = Team("Chelsea1")
            self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member(self):
        trigger = self.team.add_member(Lukaku=31, Werner=26, Kepa=24)
        self.assertEqual("Successfully added: Lukaku, Werner, Kepa", trigger)
        self.assertEqual({"Lukaku": 31, "Werner": 26, "Kepa": 24
                          }, self.team.members)
        trigger_2 = self.team.add_member(Lukaku=34)
        self.assertEqual({"Lukaku": 31, "Werner": 26, "Kepa": 24
                          }, self.team.members)
        self.assertEqual("Successfully added: ", trigger_2)

    def test_remove_member_not_existing_member(self):
        self.team.add_member(Lukaku=29, Werner=26)
        self.assertEqual({"Lukaku": 29, "Werner": 26,
                          }, self.team.members)
        self.assertEqual("Member with name Kante does not exist", self.team.remove_member("Kante"))
        self.assertEqual({"Lukaku": 29, "Werner": 26}, self.team.members)

    def test_remove_member_successfully(self):
        self.team.add_member(Lukaku=29, Werner=26)
        removed_member = self.team.remove_member("Lukaku")
        self.assertEqual("Member Lukaku removed", removed_member)
        self.assertEqual({"Werner": 26}, self.team.members)

    def test_greater_than_members_true_result(self):
        self.team.add_member(Lukaku=29, Werner=26)
        self.assertEqual({"Lukaku": 29, "Werner": 26}, self.team.members)
        team_2 = Team("Liverpool")
        team_2.add_member(Firmino=30)
        self.assertEqual({"Firmino": 30}, team_2.members)
        self.assertEqual(True, self.team > team_2)

    def test_greater_than_members_false_result(self):
        self.team.add_member(Lukaku=29, Werner=26)
        self.assertEqual({"Lukaku": 29, "Werner": 26}, self.team.members)
        team_2 = Team("Liverpool")
        team_2.add_member(Firmino=30, Salah=29, Henderson=31)
        self.assertEqual({"Firmino": 30, "Salah": 29, "Henderson": 31}, team_2.members)
        self.assertEqual(False, self.team > team_2)

    def test_len_method(self):
        self.team.add_member(Lukaku=29, Werner=26)
        self.assertEqual(2, len(self.team))

    def test_add_method(self):
        self.team.members = {"Lukaku": 29, "Werner": 26}
        self.assertEqual({"Lukaku": 29, "Werner": 26}, self.team.members)
        team_2 = Team("Liverpool")
        team_2.members = {"Firmino": 30, "Salah": 29, "Henderson": 31}
        self.assertEqual({"Firmino": 30, "Salah": 29, "Henderson": 31}, team_2.members)
        new_team = self.team + team_2
        self.assertEqual("ChelseaLiverpool", new_team.name)
        self.assertEqual({"Lukaku": 29, "Werner": 26, "Firmino": 30, "Salah": 29, "Henderson": 31}, new_team.members)


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
