from player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player:Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"


    def kick_player(self, player_name: str):
        if player_name not in [p.name for p in self.players]:
            return f"Player {player_name} is not in the guild."
        removed_player = list(filter(lambda p: p.name == player_name, self.players))[0]
        removed_player.guild = "Unaffiliated"
        self.players.remove(removed_player)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for p in self.players:
            result += f"{p.player_info()}\n"

        return result

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
