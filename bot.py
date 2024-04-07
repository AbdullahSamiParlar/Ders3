import discord
from bot_logic import gen_pass
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/şifreoluştur-'):
        a = message.content.replace("/şifreoluştur-", "")
        await message.channel.send(gen_pass(int(a)))
    else:
        return

client.run("TOKEN")
