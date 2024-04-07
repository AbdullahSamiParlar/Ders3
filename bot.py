import discord
from bot_logic import gen_pass

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/merhaba'):
        await message.channel.send("Selam!")
    if message.content.startswith('/şifreoluştur-'):
        a = message.content.replace("/şifreoluştur-", "")
        await message.channel.send(gen_pass(int(a)))
    elif message.content.startswith('/bye'):
        await message.channel.send("See you later!")
    else:
        return

client.run("TOKEN")
