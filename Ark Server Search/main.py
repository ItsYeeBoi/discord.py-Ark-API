from datetime import datetime
import aiohttp
import discord
from discord.ext import commands
import json
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")

description = """Search For Any Xbox Dedicated Server Using The Command xd"""

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(datetime.utcnow())
    print('------')

@bot.command(brief="Usage: <Server Name> | Searches For A Xbox Dedicated Server", description="Usage: .xd <Server Name>")
async def xd(ctx, *args):
    print("Message from {0.author}: {0.content} - {1}".format(ctx.message, datetime.utcnow()))
    getting_data = discord.Embed(title=f"{bot.user.name} | Retrieving Data", color=discord.Color.random(), timestamp=datetime.utcnow())
    getting_data.set_footer(text=f"Requested By {ctx.message.author}")
    getting_data.add_field(name="Getting The Data...", value="This Message Will Update Once We Have The Data", inline=False)
    embed = await ctx.send(embed=getting_data)
    while True:
        try:
            timeout = aiohttp.ClientTimeout(total=30)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get("http://arkdedicated.com/xbox/cache/unofficialserverlist.json") as r:
                    if r.status == 200:
                        servers_players = 0
                        total_players = 0
                        counter = 0
                        str_args = " ".join(args)
                        args_lower = str_args.lower()
                        args_upper = str_args.upper()
                        args_capital = str_args.capitalize()
                        args_title = str_args.title()
                        server_search_embed = discord.Embed(title=f"<:xbox:951998441624592454> {bot.user.name} | Ark Server Search For {str_args} | Found {counter} Servers", color=discord.Color.random(), timestamp=datetime.utcnow())
                        for players in await r.json():
                            await asyncio.sleep(0)
                            if str_args in players["Name"] or args_lower in players["Name"] or args_upper in players["Name"] or args_capital in players["Name"] or args_title in players["Name"]:
                                total_players += players["NumPlayers"]
                                servers_players = players["NumPlayers"]
                                counter += 1
                                server_search_embed.title = f"<:xbox:951998441624592454> {bot.user.name} | Ark Server Search For {str_args} | Found {counter} Servers"
                                server_search_embed.set_footer(text=f"Requested By {ctx.message.author} - Total Players: {total_players}")
                                server_search_embed.add_field(name="<:online_status:947493937680101428> {}: {}".format(counter, players["Name"]), value="```Map: {}, Players: {}```".format(players["MapName"], servers_players), inline=False)
                        await embed.edit(embed=server_search_embed)
                        print(f"Embed Has Been Edited - {datetime.utcnow()}")

                        filename="data.json"
                        with open(filename, "r") as file:
                            file_data = json.load(file)
                            data2 = {"server_name":f"{args_lower}",
                                    "total_servers": counter,
                                    "total_players": total_players
                                    }
                            file_data["etags"][0]["unofficial_server"] = r.headers["ETag"]

                            total_searches = file_data["searches"][0]["total_searches"]
                            file_data["searches"][0]["total_searches"] = total_searches + 1
                            total_servers_found = file_data["searches"][0]["total_servers_found"]
                            file_data["searches"][0]["total_servers_found"] = total_servers_found + counter
                            total_players_found = file_data["searches"][0]["total_players_found"]
                            file_data["searches"][0]["total_players_found"] = total_players_found + total_players
                            for data in file_data["servers_and_players"]:
                                if args_lower == data["server_name"]:
                                    print(f"Data Already Exists: {args_lower}, Updating Players And Server Count. - {datetime.utcnow()}")
                                    data["total_servers"] = counter
                                    data["total_players"] = total_players
                                    break
                            if args_lower != data["server_name"]:
                                print(f"Data Doesnt Exist: {args_lower}, Adding Data. - {datetime.utcnow()}")
                                file_data["servers_and_players"].append(data2)
                            file = open(filename, "w+")
                            file.write(json.dumps(file_data, indent=4))
                            file.close()
                        break
                    else:
                        print(f"There Was A Problem Requesting The Data, Status Code: {r.status}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")

bot.run(token)
