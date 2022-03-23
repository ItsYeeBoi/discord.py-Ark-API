import discord
from discord.ext import commands
from datetime import datetime
import json

class General(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def info(self, ctx):
        print("Message from {0.author}: {0.content} - {1}".format(ctx.message, datetime.utcnow()))
        try:
            filename = "Complete Bot\data.json"
            with open(filename, "r") as file:
                data = json.load(file)
                info_embed = discord.Embed(title=f"<:xbox:951998441624592454> {self.client.user.name} | Ark: Survival Evolved Statistics", color=discord.Color.random(), timestamp=datetime.utcnow())
                info_embed.set_footer(text=f"Requested By {ctx.message.author}")
                # Bans
                info_embed.add_field(name="<:online_status:947493937680101428> Global Bans",
                                    value="**PC Banned Players:** `{}`\n**Xbox Banned Players:** `{}`\n**PS4 Banned Players:** `{}`\n**Total Banned Players:** `{}`".format(
                                        data["bans"][0]["pc_bans"],
                                        data["bans"][0]["xbox_bans"],
                                        data["bans"][0]["ps4_bans"],
                                        data["bans"][0]["total_bans"]),
                                    inline=False)
                # Servers
                info_embed.add_field(name="<:online_status:947493937680101428> Servers",
                                value="**Official Servers:** `{}`\n**Official Servers PVP:** `{}`\n**Official Servers PVE:** `{}`\n**Official Smalls Servers:** `{}`\n**Official Legacy Servers:** `{}`\n**Official Arkpocalypse Servers:** `{}`\n**Official Hardcore Servers:** `{}`\n**Total Official Servers PVP:** `{}`\n**Total Official Servers PVE:** `{}`\n**Total Official Servers** `{}`\n**Unofficial Servers PVP:** `{}`\n**Unofficial Servers PVE:** `{}`\n**Total Unofficial Servers:** `{}`\n**Total Servers:** `{}`".format(
                                    data["servers"][0]["official_servers"],
                                    data["servers"][0]["official_servers_pvp"],
                                    data["servers"][0]["official_servers_pve"],
                                    data["servers"][0]["official_servers_smalls"],
                                    data["servers"][0]["official_servers_legacy"],
                                    data["servers"][0]["official_servers_arkpocalypse"],
                                    data["servers"][0]["official_servers_hardcore"],
                                    data["servers"][0]["total_official_servers_pvp"],
                                    data["servers"][0]["total_official_servers_pve"],
                                    data["servers"][0]["total_official_servers"],
                                    data["servers"][0]["unofficial_servers_pvp"],
                                    data["servers"][0]["unofficial_servers_pve"],
                                    data["servers"][0]["total_unofficial_servers"],
                                    data["servers"][0]["total_servers"]),
                                inline=False)
                # Players
                info_embed.add_field(name="<:online_status:947493937680101428> Players",
                                value="**Official Players:** `{}`\n**Official PVP Players:** `{}`\n**Official PVE Players:** `{}`\n**Official Smalls Players:** `{}`\n**Official Legacy Players:** `{}`\n**Official Arkpocalypse Players:** `{}`\n**Official Hardcore Players:** `{}`\n**Total Official PVP Players:** `{}`\n**Total Official PVE Players:** `{}`\n**Total Official Players:** `{}`\n**Unofficial PVP Players:** `{}`\n**Unofficial PVE Players:** `{}`\n**Total Unofficial Players:** `{}`\n**Total Players:** `{}`".format(
                                    data["players"][0]["official_servers_players"],
                                    data["players"][0]["official_servers_pvp_players"],
                                    data["players"][0]["official_servers_pve_players"],
                                    data["players"][0]["official_servers_smalls_players"],
                                    data["players"][0]["official_servers_legacy_players"],
                                    data["players"][0]["official_servers_arkpocalypse_players"],
                                    data["players"][0]["official_servers_hardcore_players"],
                                    data["players"][0]["total_official_pvp_players"],
                                    data["players"][0]["total_official_pve_players"],
                                    data["players"][0]["total_official_players"],
                                    data["players"][0]["unofficial_servers_pvp_players"],
                                    data["players"][0]["unofficial_servers_pve_players"],
                                    data["players"][0]["total_unofficial_players"],
                                    data["players"][0]["total_players"]),
                                inline=False)
                await ctx.send(embed=info_embed)
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")
    
def setup(client):
    client.add_cog(General(client))