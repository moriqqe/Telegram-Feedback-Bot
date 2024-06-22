# Telegram-Feedback-Bot

This bot is used for collecting feedback on mechanics, design, or bug reports from users. It's built with Python using the aiogram framework to interact with the Telegram API.

## Project Structure:
- `bot.py`: The main bot file, contains the logic for message handling.
- `config.py`: Configuration file, includes the API token and channel ID.
- `messages.py`: Definitions of messages used by the bot.
- `requirements.txt`: List of dependencies to be installed.

## Installation and Setup:

### Creating a Virtual Environment:

To isolate the project dependencies from system libraries, it is recommended to use a virtual environment. Create and activate a virtual environment using the following commands:

```bash
python3.10 -m venv venv
source venv/bin/activate  # For Unix/Linux
.\venv\Scripts\activate   # For Windows

Installing Dependencies:
Install the dependencies listed in requirements.txt using pip:
pip install -r requirements.txt

Configuring Settings:
In the config.py file, you need to specify the following parameters:

API_TOKEN: The bot token obtained from BotFather in Telegram.
CHANNEL_ID: The ID of a Telegram channel where feedback messages will be sent.

Example config.py file:
API_TOKEN = 'your_token_here'
CHANNEL_ID = 'your_channel_id_here'

You should obtain these values from @BotFather for the token and from your Telegram channel settings for the ID.

Running the Bot:
After configuring the settings and installing dependencies, the bot is ready to run. Start the bot with this command:

Bot Operation:
Once launched, the bot waits for the /start command from a user, then offers to choose the type of feedback and sends the corresponding message based on the user's choice. Feedback is automatically sent to the configured Telegram channel.

Important Note:
Ensure that the bot has permissions to send messages in the specified channel.
