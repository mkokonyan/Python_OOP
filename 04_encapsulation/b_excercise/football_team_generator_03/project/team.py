class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player):
        searched_player = [p for p in self.__players if player == p.name]
        if not searched_player:
            return f"Player {player} not found"
        self.__players.remove(searched_player[0])
        return searched_player[0]

