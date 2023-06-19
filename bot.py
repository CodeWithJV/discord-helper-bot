import os
import discord
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
announcement_channel_id = os.getenv('ANNOUNCEMENT_CHANNEL_ID')
youtube_api_key = os.getenv('YOUTUBE_API_KEY')
youtube_channel_id = os.getenv('YOUTUBE_CHANNEL_ID')

if discord_token is None:
    print('Error: DISCORD_TOKEN environment variable is not set.')
    exit(1)

if announcement_channel_id is None:
    print('Error: ANNOUNCEMENT_CHANNEL_ID environment variable is not set.')
    exit(1)

if youtube_api_key is None:
    print('Error: YOUTUBE_API_KEY environment variable is not set.')
    exit(1)

if youtube_channel_id is None:
    print('Error: YOUTUBE_CHANNEL_ID environment variable is not set.')
    exit(1)

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('Bot is ready to receive messages')

    youtube = build('youtube', 'v3', developerKey=youtube_api_key)
    request = youtube.search().list(
        part='snippet',
        channelId=youtube_channel_id,
        maxResults=1,
        order='date',
        type='video'
    )
    response = request.execute()

    videos = response.get('items', [])
    if videos:
        video = videos[0]
        video_id = video['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'

        announcement_channel = bot.get_channel(int(announcement_channel_id))
        await announcement_channel.send(f'New video published: {video_url}')

bot.run(discord_token)
