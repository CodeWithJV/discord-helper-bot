import os
import discord
from googleapiclient.discovery import build
from dotenv import load_dotenv
from datetime import datetime, timedelta
import time

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

async def check_new_video():
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
        if not is_same_url(video_url):
            announcement_channel = bot.get_channel(int(announcement_channel_id))
            await announcement_channel.send(f'New video published: {video_url}')
            save_url(video_url)
        else:
            print("video matches")

def is_same_url(video_url):
    file_path = '.most-recent-url'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            last_url = file.read().strip()
        return last_url == video_url
    return False

def save_url(video_url):
    file_path = '.most-recent-url'
    with open(file_path, 'w') as file:
        file.write(video_url)

async def read_and_delete_first_post():
    with open('links.txt', 'r') as file:
        lines = file.readlines()
    post = ""
    delimiter_line = None
    for i, line in enumerate(lines, start=1): 
        if line.strip() == '---':
            delimiter_line = i
            break
        post += line
    channel = bot.get_channel(1107939793532362782)
    print(post)
    if post.strip():  # Ensure that the post is not empty
        await channel.send(post)
    with open('links.txt', 'w') as file:
        file.writelines(lines[delimiter_line:])  # Skip the '---' line at the end of the post

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
    while True:
        await check_new_video()
        await read_and_delete_first_post()
        # Wait for 10 seconds before checking again
        await discord.utils.sleep_until(datetime.now() + timedelta(seconds=10))

bot.run(discord_token)
