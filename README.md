# Discord Bot with YouTube Integration

The Discord Bot with YouTube Integration is a Python-based bot that allows you to automatically post the URL of the most recent video from a specified YouTube channel to a designated Discord channel. The bot periodically checks for new videos and notifies your Discord server members about the latest content updates.

## Features

- Automatically fetches the most recent video URL from a YouTube channel
- Posts the video URL in a designated Discord channel
- Periodically checks for new videos and posts updates

## Prerequisites

- Python 3.7 or higher
- `discord.py` library
- `google-api-python-client` library
- YouTube Data API key
- Discord bot token

## Installation

1. Clone the repository.
2. Install the required Python libraries.
3. Obtain the necessary credentials:
   - Create a new Discord bot and obtain the bot token. Add the bot to your Discord server.
   - Create a project in the Google Developers Console and enable the YouTube Data API. Obtain a YouTube Data API key.
4. Configuration:
   - Create a `.env` file in the project directory and add the required environment variables.
5. Run the bot.

Please refer to the project documentation or source code for more detailed information on installation and configuration.

## License

This project is licensed under the [MIT License](LICENSE).
