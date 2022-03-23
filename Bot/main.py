from datetime import datetime
import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
from background_tasks import get_data

load_dotenv()
token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")

description = """Multipurpose Bot Used To Search Through Arks API's"""

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, description=description, intents=intents)

for filename in os.listdir("./Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")
        print(f"Cogs.{filename[:-3]} Loaded")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(datetime.utcnow())
    print('------')
    await bot.wait_until_ready()
    while not bot.is_closed():
        while True:
            await get_data()
            await asyncio.sleep(30)

bot.run(token)