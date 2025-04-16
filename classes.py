import asyncio
import random

class Game:
    def __init__(self):
        self.players = []
    def add_player(self,player):
        self.players.append(player)
    def remove_player(self,player):
        if player in self.players:
            self.players.remove(player)
    def get_all_players(self):
        return self.players


class Player:
    Players = []
    def __init__(self,name,client):
        self.name = name
        self.client = client
