import asyncio
from server import Server
from classes import Player
impoort commands
async def handle_client(client):
    await client.send("welcome to risk\n")
    await client.send("What is your name? ")
    name = await client.receive()
    client.userdata['name'] = name
    await client.send(f"Hello, {name}!\n")
    player = Player(name,client)
    while True:
        await client.send("> ")
        data = await client.receive()
        if not data:
            break
        if data.lower() in ('quit', 'exit'):      
            break
        await client.send(f"You said: {data}\n")
    
    print(f"{name} disconnected.")

async def main():
    server = Server('0.0.0.0', 1234, handle_client)
    await server.start()

def get_players():
    return player.name()


    
if __name__ == '__main__':
    asyncio.run(main())

