import asyncio
import random
class Game:
    def __init__(self,players):
        self.players = players 
class Player:
    def __init__(self,name,client):
        self.name = name
        self.client = client
