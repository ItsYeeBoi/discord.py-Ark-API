import json
import os
from datetime import datetime
from math import floor
from time import time

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
prefix = os.getenv("PREFIX")

class General(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.filename = "data.json"

    @commands.command(brief=f"Usage: {prefix}info | Displays Information On All PS4 And Xbox Servers", description=f"Usage: {prefix}info")
    async def info(self, ctx):
        print(f"Message from {ctx.message.author}: {ctx.message.content} - {datetime.utcnow()}")
        start_time = time()
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                info_embed = discord.Embed(title=f"{self.client.user.name} | Ark: Survival Evolved Statistics `[{round(time() - start_time, 2)}s]`", color=discord.Color.random(), timestamp=datetime.utcnow())
                info_embed.set_footer(text=f"Requested By {ctx.message.author}")
                # Bans
                info_embed.add_field(name="<:online_status:947493937680101428> Global Bans",
                                    value=f'**PC Banned Players:** `{data["bans"][0]["pc_bans"]}`\n'
                                        f'**Xbox Banned Players:** `{data["bans"][0]["xbox_bans"]}`\n'
                                        f'**PS4 Banned Players:** `{data["bans"][0]["ps4_bans"]}`\n'
                                        f'**Total Banned Players:** `{data["bans"][0]["total_bans"]}`', 
                                    inline=False)
                # Xbox Servers
                info_embed.add_field(name="<:online_status:947493937680101428> Xbox Servers",
                                value=f'**Official Servers:** `{data["servers"][0]["xbox_official_servers"]}`\n'
                                    f'**Official Servers PVP:** `{data["servers"][0]["xbox_official_servers_pvp"]}`\n'
                                    f'**Official Servers PVE:** `{data["servers"][0]["xbox_official_servers_pve"]}`\n'
                                    f'**Official Smalls Servers:** `{data["servers"][0]["xbox_official_servers_smalls"]}`\n'
                                    f'**Official Legacy Servers:** `{data["servers"][0]["xbox_official_servers_legacy"]}`\n'
                                    f'**Official Arkpocalypse Servers:** `{data["servers"][0]["xbox_official_servers_arkpocalypse"]}`\n'
                                    f'**Official Hardcore Servers:** `{data["servers"][0]["xbox_official_servers_hardcore"]}`\n'
                                    f'**Total Official Servers PVP:** `{data["servers"][0]["xbox_total_official_servers_pvp"]}`\n'
                                    f'**Total Official Servers PVE:** `{data["servers"][0]["xbox_total_official_servers_pve"]}`\n'
                                    f'**Total Official Servers** `{data["servers"][0]["xbox_total_official_servers"]}`\n'
                                    f'**Unofficial Servers PVP:** `{data["servers"][0]["xbox_unofficial_servers_pvp"]}`\n'
                                    f'**Unofficial Servers PVE:** `{data["servers"][0]["xbox_unofficial_servers_pve"]}`\n'
                                    f'**Total Unofficial Servers:** `{data["servers"][0]["xbox_total_unofficial_servers"]}`\n'
                                    f'**Total Servers:** `{data["servers"][0]["xbox_total_servers"]}`',
                                inline=True)
                # PS4 Servers
                info_embed.add_field(name="<:online_status:947493937680101428> PS4 Servers",
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
                                inline=True)
                info_embed.add_field(name="\u200b", value="\u200b", inline=False)
                # Xbox Players
                info_embed.add_field(name="<:online_status:947493937680101428> Xbox Players",
                                value=f'**Official Players:** `{data["players"][0]["xbox_official_servers_players"]}`\n'
                                    f'**Official PVP Players:** `{data["players"][0]["xbox_official_servers_pvp_players"]}`\n'
                                    f'**Official PVE Players:** `{data["players"][0]["xbox_official_servers_pve_players"]}`\n'
                                    f'**Official Smalls Players:** `{data["players"][0]["xbox_official_servers_smalls_players"]}`\n'
                                    f'**Official Legacy Players:** `{data["players"][0]["xbox_official_servers_legacy_players"]}`\n'
                                    f'**Official Arkpocalypse Players:** `{data["players"][0]["xbox_official_servers_arkpocalypse_players"]}`\n'
                                    f'**Official Hardcore Players:** `{data["players"][0]["xbox_official_servers_hardcore_players"]}`\n'
                                    f'**Total Official PVP Players:** `{data["players"][0]["xbox_total_official_pvp_players"]}`\n'
                                    f'**Total Official PVE Players:** `{data["players"][0]["xbox_total_official_pve_players"]}`\n'
                                    f'**Total Official Players:** `{data["players"][0]["xbox_total_official_players"]}`\n'
                                    f'**Unofficial PVP Players:** `{data["players"][0]["xbox_unofficial_servers_pvp_players"]}`\n'
                                    f'**Unofficial PVE Players:** `{data["players"][0]["xbox_unofficial_servers_pve_players"]}`\n'
                                    f'**Total Unofficial Players:** `{data["players"][0]["xbox_total_unofficial_players"]}`\n'
                                    f'**Total Players:** `{data["players"][0]["xbox_total_players"]}`',
                                inline=True)
                # PS4 Players
                info_embed.add_field(name="<:online_status:947493937680101428> PS4 Players",
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
                                inline=True)
                await ctx.send(embed=info_embed)
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")

    @commands.command(aliases=["tekgenerator", "generator"], brief=f"Usage: {prefix}tekgen | Calculates How Long A Tek Generator Will Last", description=f"Usage: {prefix}tekgen")
    async def tekgen(self, ctx, arg1, arg2):
        print(f"Message from {ctx.message.author}: {ctx.message.content} - {datetime.utcnow()}")
        radius = float(arg1)
        element_usage = abs(1+(radius-1)*0.33)
        element_hourly = round(element_usage/18, 2)
        element_total = int(arg2)
        hourlyrate = abs(18/element_usage)
        will_last = abs((element_total)*hourlyrate)*1
        secondstotal = abs(will_last*3600)
        days = floor(secondstotal/(3600*24))
        hours = int(secondstotal/3600)%24
        minutes = int((secondstotal%3600)/60)
        seconds = int(secondstotal%60)

        element_usage = round(element_usage, 2)
        element_hourly = round(element_hourly, 2)
        radius = round(radius, 2)
        if element_hourly.is_integer() == True:
            element_hourly = int(element_hourly)
        if element_usage.is_integer() == True:
            element_usage = int(element_usage)
        if radius.is_integer() == True:
            radius = int(radius)
        start_time = time()
        tekgen_embed = discord.Embed(title=f"{self.client.user.name} `[{round(time() - start_time, 2)}s]`", color=discord.Color.random(), timestamp=datetime.utcnow())
        tekgen_embed.set_footer(text=f"Requested By {ctx.message.author}")
        tekgen_embed.add_field(name="<:tek_gen:959825868748890142> Tek Generator Calculator", value=f"**Element:** `{element_total}`\n**Radius:** `{radius}`", inline=False)
        tekgen_embed.add_field(name="__RunTime:__", value=f"**Days:** `{days:02}`\n**Hours:** `{hours:02}`\n**Minutes:** `{minutes:02}`\n**Seconds:** `{seconds:02}`", inline=False)
        tekgen_embed.add_field(name="__Usage:__", value=f"**Element Used Every Hour:** `{element_hourly}`\n**Element Used Every 18 Hours:** `{element_usage}`", inline=False)
        await ctx.send(embed=tekgen_embed)
        
    @commands.command(aliases=["tekforcefield", "tekforcef", "forcefield"], brief=f"Usage: {prefix}tekforce | Calculates How Long A Tek Forcefield Will Last", description=f"Usage: {prefix}tekforce")
    async def tekforce(self, ctx, arg1, arg2):
        print(f"Message from {ctx.message.author}: {ctx.message.content} - {datetime.utcnow()}")
        radius = float(arg1)
        element_total = int(arg2)
        element_24hours = radius*24
        will_last = abs((element_total)/radius)*1
        seconds_total = abs(will_last*3600)
        days = floor(seconds_total/(3600*24))
        hours = int(seconds_total/3600)%24
        minutes = int((seconds_total%3600)/60)
        seconds = int(seconds_total%60)

        element_24hours = round(element_24hours, 2)
        radius = round(radius, 2)
        if element_24hours.is_integer() == True:
            element_24hours = int(element_24hours)
        if radius.is_integer() == True:
            radius = int(radius)
        start_time = time()
        tekforce_embed = discord.Embed(title=f"{self.client.user.name} `[{round(time() - start_time, 2)}s]`", color=discord.Color.random(), timestamp=datetime.utcnow())
        tekforce_embed.set_footer(text=f"Requested By {ctx.message.author}")
        tekforce_embed.add_field(name="<:tek_forcef:959825876206387220> Tek Forcefield Calculator", value=f"**Element:** `{element_total}`\n**Radius:** `{radius}`", inline=False)
        tekforce_embed.add_field(name="__RunTime:__", value=f"**Days:** `{days:02}`\n**Hours:** `{hours:02}`\n**Minutes:** `{minutes:02}`\n**Seconds:** `{seconds:02}`", inline=False)
        tekforce_embed.add_field(name="__Usage:__", value=f"**Element Used Every Hour:** `{radius}`\n**Element Used Every 24 Hours:** `{element_24hours}`", inline=False)
        await ctx.send(embed=tekforce_embed)

def setup(client):
    client.add_cog(General(client))