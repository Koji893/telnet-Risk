import classes
from gamelogic import game
print(id(game))
'''                                                                                                                                    
def [command](player, *args):                                                                                                          
    return {                                                                                                                           
        "scope": "",                                                                                                                
        "message": ""                                                                      
    }                                                                                                                                  
'''
def get_players(player):
     players = [p.name for p in game.players]     
     print(players)
     print(game.players)
     return "\n".join(players)

def whoami(player):
    return player.name
def clear(player):
   return "\033[2J\033[H"
