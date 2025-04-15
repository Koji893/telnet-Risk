import asyncio
import inspect
from server import Server
import commands
from classes import *
game = Game()
print(id(game))
#This dict comprehension generates the command dictionary from the command.py file
command_dict = {
    name: func
    for name, func in inspect.getmembers(commands, inspect.isfunction)
    }
async def command(data,player):
    cmd, *args = data.strip().split()
    if cmd in command_dict:
        return command_dict[cmd](player,*args) +"\n"
    else:
        return "That command is invalid\n"
async def commandProcessor(data,player,all_players):
    result = await command(data,player)
    if isinstance(result,dict):
        scope = result.get("scope","player")
        message= result.get("message","")
        if scope =="all":
            for p in all_players:
                await p.client.send(message)
        elif scope == "target":
            target_name = result.get("target")
            for p in all_players:
                if p.name == target_name:
                    await p.client.send(message)
                    break
        else:
            await player.client.send(result)
    else:
        await player.client.send(result)
                

async def handle_client(client):
    await client.send("welcome to risk\n")
    await client.send("What is your name? ")
    name = await client.receive()
    client.userdata['name'] = name
    await client.send(f"Hello, {name}!\n")
    player = Player(name,client)
    game.add_player(player)
    print([p.name for p in game.players])
    while True:
        await client.send("> ")
        data = await client.receive()
        if not data:
            break
        if data.lower() in ('quit', 'exit'):      
            break
        await commandProcessor(data,player,game.players)
    print(f"{name} disconnected.")

async def main():
    server = Server('0.0.0.0', 1234, handle_client)
    await server.start()

    
if __name__ == '__main__':
    asyncio.run(main())

