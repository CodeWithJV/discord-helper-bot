import os
import discord
from discord import Intents
from dotenv import load_dotenv

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

if discord_token is None:
    print('Error: DISCORD_TOKEN environment variable is not set.')
    exit(1)

intents = Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True  # Enable messaging intent

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('Bot is ready to receive messages')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == 'hello':
        await message.channel.send('Hello, World!')

bot.run(discord_token)
