import asyncio
import json
import os
import re
from datetime import datetime
from time import time

import aiohttp
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
prefix = os.getenv("PREFIX")

class PS4(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.filename = "data.json"

    @commands.command(aliases=["ps4info", "ps4i", "psinfo"], brief=f"Usage: {prefix}pinfo | Displays Information On All PS4 Servers", description=f"Usage: {prefix}pinfo")
    async def pinfo(self, ctx):
        print(f"Message from {ctx.message.author}: {ctx.message.content} - {datetime.utcnow()}")
        start_time = time()
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                info_embed = discord.Embed(title=f"<:ps4:960221903035965510> {self.client.user.name} | Ark: Survival Evolved PS4 Statistics `[{round(time() - start_time, 2)}s]`", color=discord.Color.random(), timestamp=datetime.utcnow())
                info_embed.set_footer(text=f"Requested By {ctx.message.author}")
                # Bans
                info_embed.add_field(name="<:online_status:947493937680101428> Global Bans",
                                    value=f'**PC Banned Players:** `{data["bans"][0]["pc_bans"]}`\n'
                                        f'**Xbox Banned Players:** `{data["bans"][0]["xbox_bans"]}`\n'
                                        f'**PS4 Banned Players:** `{data["bans"][0]["ps4_bans"]}`\n'
                                        f'**Total Banned Players:** `{data["bans"][0]["total_bans"]}`', 
                                    inline=False)
                # Servers
                info_embed.add_field(name="<:online_status:947493937680101428> Servers",
                                value=f'**Official Servers:** `{data["servers"][1]["ps4_official_servers"]}`\n'
                                    f'**Official Servers PVP:** `{data["servers"][1]["ps4_official_servers_pvp"]}`\n'
                                    f'**Official Servers PVE:** `{data["servers"][1]["ps4_official_servers_pve"]}`\n'
                                    f'**Official Smalls Servers:** `{data["servers"][1]["ps4_official_servers_smalls"]}`\n'
                                    f'**Official Legacy Servers:** `{data["servers"][1]["ps4_official_servers_legacy"]}`\n'
                                    f'**Official Arkpocalypse Servers:** `{data["servers"][1]["ps4_official_servers_arkpocalypse"]}`\n'
                                    f'**Official Hardcore Servers:** `{data["servers"][1]["ps4_official_servers_hardcore"]}`\n'
                                    f'**Total Official Servers PVP:** `{data["servers"][1]["ps4_total_official_servers_pvp"]}`\n'
                                    f'**Total Official Servers PVE:** `{data["servers"][1]["ps4_total_official_servers_pve"]}`\n'
                                    f'**Total Official Servers** `{data["servers"][1]["ps4_total_official_servers"]}`\n'
                                    f'**Unofficial Servers PVP:** `{data["servers"][1]["ps4_unofficial_servers_pvp"]}`\n'
                                    f'**Unofficial Servers PVE:** `{data["servers"][1]["ps4_unofficial_servers_pve"]}`\n'
                                    f'**Total Unofficial Servers:** `{data["servers"][1]["ps4_total_unofficial_servers"]}`\n'
                                    f'**Total Servers:** `{data["servers"][1]["ps4_total_servers"]}`',
                                inline=False)
                # Players
                info_embed.add_field(name="<:online_status:947493937680101428> Players",
                                value=f'**Official Players:** `{data["players"][1]["ps4_official_servers_players"]}`\n'
                                    f'**Official PVP Players:** `{data["players"][1]["ps4_official_servers_pvp_players"]}`\n'
                                    f'**Official PVE Players:** `{data["players"][1]["ps4_official_servers_pve_players"]}`\n'
                                    f'**Official Smalls Players:** `{data["players"][1]["ps4_official_servers_smalls_players"]}`\n'
                                    f'**Official Legacy Players:** `{data["players"][1]["ps4_official_servers_legacy_players"]}`\n'
                                    f'**Official Arkpocalypse Players:** `{data["players"][1]["ps4_official_servers_arkpocalypse_players"]}`\n'
                                    f'**Official Hardcore Players:** `{data["players"][1]["ps4_official_servers_hardcore_players"]}`\n'
                                    f'**Total Official PVP Players:** `{data["players"][1]["ps4_total_official_pvp_players"]}`\n'
                                    f'**Total Official PVE Players:** `{data["players"][1]["ps4_total_official_pve_players"]}`\n'
                                    f'**Total Official Players:** `{data["players"][1]["ps4_total_official_players"]}`\n'
                                    f'**Unofficial PVP Players:** `{data["players"][1]["ps4_unofficial_servers_pvp_players"]}`\n'
                                    f'**Unofficial PVE Players:** `{data["players"][1]["ps4_unofficial_servers_pve_players"]}`\n'
                                    f'**Total Unofficial Players:** `{data["players"][1]["ps4_total_unofficial_players"]}`\n'
                                    f'**Total Players:** `{data["players"][1]["ps4_total_players"]}`',
                                inline=False)
                await ctx.send(embed=info_embed)
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")

    @commands.command(brief=f"Usage: {prefix}po <Server Name> | Searches For A PS4 Official Server", description=f"Usage: {prefix}xo <Server Name>")
    async def po(self, ctx, args):
        print(f"Message from {ctx.message.author}: {ctx.message.content} - {datetime.utcnow()}")
        start_time = time()
        getting_data = discord.Embed(title=f"{self.client.user.name} | Retrieving Data", color=discord.Color.random(), timestamp=datetime.utcnow())
        getting_data.set_footer(text=f"Requested By {ctx.message.author}")
        getting_data.add_field(name="This Message Will Update Once We Have The Data", value="If This Message Doesnt Update Please Try Again", inline=False)
        embed = await ctx.send(embed=getting_data)
        try:
            timeout = aiohttp.ClientTimeout(total=30)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get("http://arkdedicated.com/sotfps4/cache/officialserverlist.json") as r:
                    if r.status == 200:
                        counter = 0
                        server_players = 0
                        server_name = ""
                        server_map = ""
                        server_daytime = 0
                        server_search_embed = discord.Embed(title=f"<:ps4:960221903035965510> {self.client.user.name} | Ark Search For: {args}", color=discord.Color.random(), timestamp=datetime.utcnow())
                        for players in await r.json():
                            if (args in players["Name"]
                            and "PS4Official" in players["Name"]
                            and "SmallTribes" not in players["Name"]
                            and "ARKpocalypse" not in players["Name"]
                            and "LEGACY" not in players["Name"]):
                                end_value = re.sub("[^\d\.()]", "", players["Name"])
                                end_result = re.sub("[\(\[].*?[\)\]]", "", end_value)
                                if end_result[1:] == args:
                                    server_players = players["NumPlayers"]
                                    server_name = players["Name"]
                                    server_map = players["MapName"]
                                    server_daytime = players["DayTime"]
                                    counter += 1
                                    server_search_embed.title = f"<:ps4:960221903035965510> {self.client.user.name} | Ark Search For: {args} `[{round(time() - start_time, 2)}s]`"
                                    server_search_embed.set_footer(text=f"Requested By {ctx.message.author}")
                                    server_search_embed.add_field(name=f'<:online_status:947493937680101428> Server Is Online', value="The Data Below Is Up To Date", inline=False)
                                    server_search_embed.add_field(name=f'**Server Name:**', value=f'```{server_name}```', inline=False)
                                    server_search_embed.add_field(name=f'**Players:**', value=f'```{server_players}/{players["MaxPlayers"]}```', inline=False)
                                    server_search_embed.add_field(name=f'**Map**', value=f'```{server_map}```', inline=False)
                                    server_search_embed.add_field(name=f'**Day**', value=f'```{server_daytime}```', inline=False)
                                    break
                        await embed.edit(embed=server_search_embed)
                        print(f"Embed Has Been Edited - {datetime.utcnow()}")

                        with open(self.filename, "r") as file:
                            file_data = json.load(file)
                            new_data = {
                                "server_name": server_name,
                                "user_search": args,
                                "map_name": server_map,
                                "day_time": server_daytime,
                                "total_players": server_players
                            }
                            file_data["etags"][0]["ps4_official_server"] = r.headers["ETag"]
                            total_searches = file_data["searches"][0]["total_searches"]
                            file_data["searches"][0]["total_searches"] = total_searches + 1
                            total_servers_found = file_data["searches"][0]["total_servers_found"]
                            file_data["searches"][0]["total_servers_found"] = total_servers_found + counter
                            total_players_found = file_data["searches"][0]["total_players_found"]
                            file_data["searches"][0]["total_players_found"] = total_players_found + server_players
                            for data in file_data["ps4_official_servers_and_players"]:
                                if args == data["user_search"]:
                                    print(f"Data Already Exists: {args}, Updating Players And Day. - {datetime.utcnow()}")
                                    data["day_time"] = players["DayTime"]
                                    data["total_players"] = server_players
                                    break
                            if args != data["user_search"]:
                                print(f"Data Doesnt Exist: {args}, Adding Data. - {datetime.utcnow()}")
                                file_data["ps4_official_servers_and_players"].append(new_data)
                            with open(self.filename, "w+") as file:
                                file.write(json.dumps(file_data, indent=4))
                    else:
                        error_embed = discord.Embed(title=f"{self.client.user.name} | ERROR", color=discord.Color.red(), timestamp=datetime.utcnow())
                        error_embed.set_footer(text=f"Requested By {ctx.message.author} - ERROR CODE: {r.status}")
                        error_embed.add_field(name="There Has Been An Error", value="Please Try Again")
                        await embed.edit(embed=error_embed)
                        print(f"There Was A Problem Requesting The Data, Status Code: {r.status}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")

    @commands.command(brief=f"Usage: {prefix}ps <Server Name> | Searches For A PS4 Official Smalls Server", description=f"Usage: {prefix}ps <Server Name>")
    async def ps(self, ctx, args):
        print(f"Message from {ctx.message.author}: {ctx.message.content} - {datetime.utcnow()}")
        start_time = time()
        getting_data = discord.Embed(title=f"{self.client.user.name} | Retrieving Data", color=discord.Color.random(), timestamp=datetime.utcnow())
        getting_data.set_footer(text=f"Requested By {ctx.message.author}")
        getting_data.add_field(name="This Message Will Update Once We Have The Data", value="If This Message Doesnt Update Please Try Again", inline=False)
        embed = await ctx.send(embed=getting_data)
        try:
            timeout = aiohttp.ClientTimeout(total=30)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get("http://arkdedicated.com/sotfps4/cache/officialserverlist.json") as r:
                    if r.status == 200:
                        counter = 0
                        server_players = 0
                        server_name = ""
                        server_map = ""
                        server_daytime = '""'
                        server_search_embed = discord.Embed(title=f"<:ps4:960221903035965510> {self.client.user.name} | Ark Search For: {args}", color=discord.Color.random(), timestamp=datetime.utcnow())
                        for players in await r.json():
                            if (args in players["Name"]
                            and "SmallTribes" in players["Name"]
                            and "PS4Official" in players["Name"]
                            and "ARKpocalypse" not in players["Name"]
                            and "LEGACY" not in players["Name"]):
                                end_value = " ".join(re.findall(args, players["Name"]))
                                if end_value == args:
                                    server_players = players["NumPlayers"]
                                    server_name = players["Name"]
                                    server_map = players["MapName"]
                                    server_daytime = players["DayTime"]
                                    counter += 1
                                    server_search_embed.title = f"<:ps4:960221903035965510> {self.client.user.name} | Ark Search For: {args} `[{round(time() - start_time, 2)}s]`"
                                    server_search_embed.set_footer(text=f"Requested By {ctx.message.author}")
                                    server_search_embed.add_field(name=f'<:online_status:947493937680101428> Server Is Online', value="The Data Below Is Up To Date", inline=False)
                                    server_search_embed.add_field(name=f'**Server Name:**', value=f'```{server_name}```', inline=False)
                                    server_search_embed.add_field(name=f'**Players:**', value=f'```{server_players}/{players["MaxPlayers"]}```', inline=False)
                                    server_search_embed.add_field(name=f'**Map**', value=f'```{server_map}```', inline=False)
                                    server_search_embed.add_field(name=f'**Day**', value=f'```{server_daytime}```', inline=False)
                                    break
                        await embed.edit(embed=server_search_embed)
                        print(f"Embed Has Been Edited - {datetime.utcnow()}")

                        with open(self.filename, "r") as file:
                            file_data = json.load(file)
                            new_data = {
                                "server_name": server_name,
                                "user_search": args,
                                "map_name": server_map,
                                "day_time": server_daytime,
                                "total_players": server_players
                            }
                            file_data["etags"][0]["ps4_official_server"] = r.headers["ETag"]
                            total_searches = file_data["searches"][0]["total_searches"]
                            file_data["searches"][0]["total_searches"] = total_searches + 1
                            total_servers_found = file_data["searches"][0]["total_servers_found"]
                            file_data["searches"][0]["total_servers_found"] = total_servers_found + counter
                            total_players_found = file_data["searches"][0]["total_players_found"]
                            file_data["searches"][0]["total_players_found"] = total_players_found + server_players
                            for data in file_data["ps4_smalls_servers_and_players"]:
                                if args == data["user_search"]:
                                    print(f"Data Already Exists: {args}, Updating Players And Day. - {datetime.utcnow()}")
                                    data["day_time"] = server_daytime
                                    data["total_players"] = server_players
                                    break
                            if args != data["user_search"]:
                                print(f"Data Doesnt Exist: {args}, Adding Data. - {datetime.utcnow()}")
                                file_data["ps4_smalls_servers_and_players"].append(new_data)
                            with open(self.filename, "w+") as file:
                                file.write(json.dumps(file_data, indent=4))
                    else:
                        error_embed = discord.Embed(title=f"{self.client.user.name} | ERROR", color=discord.Color.red(), timestamp=datetime.utcnow())
                        error_embed.set_footer(text=f"Requested By {ctx.message.author} - ERROR CODE: {r.status}")
                        error_embed.add_field(name="There Has Been An Error", value="Please Try Again")
                        await embed.edit(embed=error_embed)
                        print(f"There Was A Problem Requesting The Data, Status Code: {r.status}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")

    @commands.command(brief=f"Usage: {prefix}pd <Server Name> | Searches For A PS4 Dedicated Server", description=f"Usage: {prefix}pd <Server Name>")
    async def pd(self, ctx, *args):
        print(f"Message from {ctx.message.author}: {ctx.message.content} - {datetime.utcnow()}")
        start_time = time()
        getting_data = discord.Embed(title=f"{self.client.user.name} | Retrieving Data", color=discord.Color.random(), timestamp=datetime.utcnow())
        getting_data.set_footer(text=f"Requested By {ctx.message.author}")
        getting_data.add_field(name="This Message Will Update Once We Have The Data", value="If This Message Doesnt Update Please Try Again", inline=False)
        embed = await ctx.send(embed=getting_data)
        try:
            timeout = aiohttp.ClientTimeout(total=30)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get("http://arkdedicated.com/ps4/cache/unofficialserverlist.json") as r:
                    if r.status == 200:
                        servers_players = 0
                        total_players = 0
                        total_maxplayers = 0
                        counter = 0
                        str_args = " ".join(args)
                        args_lower = str_args.lower()
                        args_upper = str_args.upper()
                        args_capital = str_args.capitalize()
                        args_title = str_args.title()
                        server_search_embed = discord.Embed(title=f"<:ps4:960221903035965510> {self.client.user.name} | Ark Server Search For {str_args} | Found {counter} Servers", color=discord.Color.random(), timestamp=datetime.utcnow())
                        for players in await r.json():
                            await asyncio.sleep(0)
                            if (str_args in players["Name"]
                            or args_lower in players["Name"]
                            or args_upper in players["Name"]
                            or args_capital in players["Name"]
                            or args_title in players["Name"]):
                                total_players += players["NumPlayers"]
                                servers_players = players["NumPlayers"]
                                total_maxplayers += players["MaxPlayers"]
                                counter += 1
                                server_search_embed.title = f"<:ps4:960221903035965510> {self.client.user.name} | Ark Server Search For {str_args} | Found {counter} Servers `[{round(time() - start_time, 2)}s]`"
                                server_search_embed.set_footer(text=f"Requested By {ctx.message.author} - Total Players: {total_players}/{total_maxplayers}")
                                server_search_embed.add_field(name=f'<:online_status:947493937680101428> {counter}: {players["Name"]}', value=f'```Map: {players["MapName"]}, Players: {servers_players}/{players["MaxPlayers"]}```', inline=False)
                        await embed.edit(embed=server_search_embed)
                        print(f"Embed Has Been Edited - {datetime.utcnow()}")

                        with open(self.filename, "r") as file:
                            file_data = json.load(file)
                            new_data = {
                                    "server_name": args_lower,
                                    "total_servers": counter,
                                    "total_players": total_players
                            }
                            file_data["etags"][0]["ps4_unofficial_server"] = r.headers["ETag"]
                            total_searches = file_data["searches"][0]["total_searches"]
                            file_data["searches"][0]["total_searches"] = total_searches + 1
                            total_servers_found = file_data["searches"][0]["total_servers_found"]
                            file_data["searches"][0]["total_servers_found"] = total_servers_found + counter
                            total_players_found = file_data["searches"][0]["total_players_found"]
                            file_data["searches"][0]["total_players_found"] = total_players_found + total_players
                            for data in file_data["ps4_unofficial_servers_and_players"]:
                                if args_lower == data["server_name"]:
                                    print(f"Data Already Exists: {args_lower}, Updating Players And Server Count. - {datetime.utcnow()}")
                                    data["total_servers"] = counter
                                    data["total_players"] = total_players
                                    break
                            if args_lower != data["server_name"]:
                                print(f"Data Doesnt Exist: {args_lower}, Adding Data. - {datetime.utcnow()}")
                                file_data["ps4_unofficial_servers_and_players"].append(new_data)
                            with open(self.filename, "w+") as file:
                                file.write(json.dumps(file_data, indent=4))
                    else:
                        error_embed = discord.Embed(title=f"{self.client.user.name} | ERROR", color=discord.Color.red(), timestamp=datetime.utcnow())
                        error_embed.set_footer(text=f"Requested By {ctx.message.author} - ERROR CODE: {r.status}")
                        error_embed.add_field(name="There Has Been An Error", value="Please Try Again")
                        await embed.edit(embed=error_embed)
                        print(f"There Was A Problem Requesting The Data, Status Code: {r.status}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")

def setup(client):
    client.add_cog(PS4(client))