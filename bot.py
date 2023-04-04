#creation of a discord bot to learn more python
import discord
from  discord.ext import commands
import os
import responses 
from dotenv import load_dotenv
import logging
load_dotenv()

logger = logging.getLogger('Discord')

async def send_message(message, user_message, is_private): 
    try: 
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send()
    except Exception as e: 
        print(e) 
#starts the discord bot
#bot.run(discord_token)

def start_bot():
    client = discord.Client()
    discord_token = os.getenv('API_KEY')
    @client.event 
    async def on_ready(): 
       print('shite ready')

    client.run(discord_token)
