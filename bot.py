# creation of a discord bot to learn more python
import discord
from discord.ext import commands
import os
import response
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger('Discord')


async def send_message(message, user_message, is_private):
    try:
        ans = response.newresponse(user_message)
        await message.author.send(ans) if is_private else await message.channel.send(ans)
    except Exception as e:
        print(f'error inside Exception {e}')
    # starts the discord bot


# bot.run(discord_token)

def start_bot():
    # client = discord.Client()
    discord_token = os.getenv('API_KEY')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print('shite ready')

    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return

        username = str(msg.author)
        channel = str(msg.channel)
        user_content = str(msg.content)
        print(f'{username} said :  "{user_content}" in {channel}')
        if user_content[0] == '?':
            user_content = user_content[1:]
            await send_message(msg, user_content, is_private=True)
        else:
            await send_message(msg, user_content, is_private=False)

    client.run(discord_token)
