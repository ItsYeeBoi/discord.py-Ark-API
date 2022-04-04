import json
from datetime import datetime

import aiohttp

async def get_data():
    filename = "data.json"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get("http://arkdedicated.com/banlist.txt") as r:
                if r.status == 200:
                    with open(filename, "r") as file:
                        data = json.load(file)
                    text = await r.text()
                    pc_bans = text.count("\n") + 1
                    data["etags"][0]["pc_banlist"] = r.headers["ETag"]
                    data["bans"][0]["pc_bans"] = pc_bans
                    with open(filename, "w+") as file:
                        file.write(json.dumps(data, indent=4))
                    print(f"PC Banlist Updated - {datetime.utcnow()}")
                else:
                    print(f"PC Banlist Had A Problem, Status Code = {r.status} - {datetime.utcnow()}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")
        try:
            async with session.get("http://arkdedicated.com/xboxbanlist.txt") as r:
                if r.status == 200:
                    with open(filename, "r") as file:
                        data = json.load(file)
                    text = await r.text()
                    xbox_bans = text.count("\n") + 1
                    data["etags"][0]["xbox_banlist"] = r.headers["ETag"]
                    data["bans"][0]["xbox_bans"] = xbox_bans
                    with open(filename, "w+") as file:
                        file.write(json.dumps(data, indent=4))
                    print(f"Xbox Banlist Updated - {datetime.utcnow()}")
                else:
                    print(f"Xbox Banlist Had A Problem, Status Code = {r.status} - {datetime.utcnow()}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")
        try:
            async with session.get("http://arkdedicated.com/ps4banlist.txt") as r:
                if r.status == 200:
                    with open(filename, "r") as file:
                        data = json.load(file)
                    text = await r.text()
                    ps4_bans = text.count("\n") + 1
                    data["etags"][0]["ps4_banlist"] = r.headers["ETag"]
                    data["bans"][0]["ps4_bans"] = ps4_bans
                    with open(filename, "w+") as file:
                        file.write(json.dumps(data, indent=4))
                    print(f"PS4 Banlist Updated - {datetime.utcnow()}")
                else:
                    print(f"PS4 Banlist Had A Problem, Status Code = {r.status} - {datetime.utcnow()}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")
        try:
            async with session.get("http://arkdedicated.com/xbox/cache/officialserverlist.json") as r:
                if r.status == 200:
                    with open(filename, "r") as file:
                        data = json.load(file)
                    text = await r.text()
                    data["etags"][0]["xbox_official_server"] = r.headers["ETag"]
                    xbox_total_official_servers = text.count("AllowDownloadItems")
                    xbox_official_servers_smalls = text.count("XboxSmallTribes")
                    xbox_official_servers = xbox_total_official_servers - xbox_official_servers_smalls
                    xbox_official_servers_pvp = text.count("NewXboxPVP")
                    xbox_official_servers_pve = text.count("NewXboxPVE")
                    xbox_official_servers_legacy = text.count('"XboxPVE"')
                    xbox_official_servers_arkpocalypse = text.count("XboxArkpocalypse")
                    xbox_official_servers_hardcore = text.count("NewXboxHardcorePVP")
                    xbox_total_official_servers_pvp = text.count('"SessionIsPve":0')
                    xbox_total_official_servers_pve = text.count('"SessionIsPve":1')
                    data["servers"][0]["xbox_official_servers"] = xbox_official_servers
                    data["servers"][0]["xbox_official_servers_pvp"] = xbox_official_servers_pvp
                    data["servers"][0]["xbox_official_servers_pve"] = xbox_official_servers_pve
                    data["servers"][0]["xbox_official_servers_smalls"] = xbox_official_servers_smalls
                    data["servers"][0]["xbox_official_servers_legacy"] = xbox_official_servers_legacy
                    data["servers"][0]["xbox_official_servers_arkpocalypse"] = xbox_official_servers_arkpocalypse
                    data["servers"][0]["xbox_official_servers_hardcore"] = xbox_official_servers_hardcore
                    data["servers"][0]["xbox_total_official_servers_pvp"] = xbox_total_official_servers_pvp
                    data["servers"][0]["xbox_total_official_servers_pve"] = xbox_total_official_servers_pve
                    data["servers"][0]["xbox_total_official_servers"] = xbox_total_official_servers
                    xbox_total_official_players = 0
                    xbox_total_official_pvp_players = 0
                    xbox_total_official_pve_players = 0
                    xbox_official_servers_pvp_players = 0
                    xbox_official_servers_pve_players = 0
                    xbox_official_servers_legacy_players = 0
                    xbox_official_servers_smalls_players = 0
                    xbox_official_servers_arkpocalypse_players = 0
                    xbox_official_servers_hardcore_players = 0
                    for players in await r.json():
                        xbox_total_official_players += players["NumPlayers"]
                        if players["ClusterId"] == "XboxSmallTribes":
                            xbox_official_servers_smalls_players += players["NumPlayers"]
                        if players["ClusterId"] == "XboxPVE":
                            xbox_official_servers_legacy_players += players["NumPlayers"]
                        if players["ClusterId"] == "NewXboxPVP":
                            xbox_official_servers_pvp_players += players["NumPlayers"]
                        if players["ClusterId"] == "NewXboxPVE":
                            xbox_official_servers_pve_players += players["NumPlayers"]
                        if players["SessionIsPve"] == 0:
                            xbox_total_official_pvp_players += players["NumPlayers"]
                        if players["SessionIsPve"] == 1:
                            xbox_total_official_pve_players += players["NumPlayers"]
                        if players["ClusterId"] == "XboxArkpocalypse":
                            xbox_official_servers_arkpocalypse_players += players["NumPlayers"]
                        if players["ClusterId"] == "NewXboxHardcorePVP":
                            xbox_official_servers_hardcore_players += players["NumPlayers"]
                    xbox_official_servers_players = xbox_total_official_players - xbox_official_servers_smalls_players
                    data["players"][0]["xbox_official_servers_players"] = xbox_official_servers_players
                    data["players"][0]["xbox_official_servers_pvp_players"] = xbox_official_servers_pvp_players
                    data["players"][0]["xbox_official_servers_pve_players"] = xbox_official_servers_pve_players
                    data["players"][0]["xbox_official_servers_smalls_players"] = xbox_official_servers_smalls_players
                    data["players"][0]["xbox_official_servers_legacy_players"] = xbox_official_servers_legacy_players
                    data["players"][0]["xbox_official_servers_arkpocalypse_players"] = xbox_official_servers_arkpocalypse_players
                    data["players"][0]["xbox_official_servers_hardcore_players"] = xbox_official_servers_hardcore_players
                    data["players"][0]["xbox_total_official_pvp_players"] = xbox_total_official_pvp_players
                    data["players"][0]["xbox_total_official_pve_players"] = xbox_total_official_pve_players
                    data["players"][0]["xbox_total_official_players"] = xbox_total_official_players
                    with open(filename, "w+") as file:
                        file.write(json.dumps(data, indent=4))
                    print(f"Xbox Official Server Updated - {datetime.utcnow()}")
                else:
                    print(f"Xbox Official Servers Had A Problem, Status Code = {r.status} - {datetime.utcnow()}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")
        try:
            async with session.get("http://arkdedicated.com/sotfps4/cache/officialserverlist.json") as r:
                if r.status == 200:
                    with open(filename, "r") as file:
                        data = json.load(file)
                    text = await r.text()
                    data["etags"][0]["ps4_official_server"] = r.headers["ETag"]
                    ps4_total_official_servers = text.count("AllowDownloadItems")
                    ps4_official_servers_smalls = text.count("PS4SmallTribesCrossArkCluster")
                    ps4_official_servers = ps4_total_official_servers - ps4_official_servers_smalls
                    ps4_official_servers_pvp = text.count("NewPS4PVPCrossArkCluster")
                    ps4_official_servers_pve = text.count("NewPS4PVECrossArkCluster")
                    ps4_official_servers_legacy = text.count('"PS4PVECrossArkCluster"')
                    ps4_official_servers_arkpocalypse = text.count("PS4ArkpocalypseCrossArkCluster")
                    ps4_official_servers_hardcore = text.count("NewPS4HardcorePVPCrossArkCluster")
                    ps4_total_official_servers_pvp = text.count('"SessionIsPve":0')
                    ps4_total_official_servers_pve = text.count('"SessionIsPve":1')
                    data["servers"][1]["ps4_official_servers"] = ps4_official_servers
                    data["servers"][1]["ps4_official_servers_pvp"] = ps4_official_servers_pvp
                    data["servers"][1]["ps4_official_servers_pve"] = ps4_official_servers_pve
                    data["servers"][1]["ps4_official_servers_smalls"] = ps4_official_servers_smalls
                    data["servers"][1]["ps4_official_servers_legacy"] = ps4_official_servers_legacy
                    data["servers"][1]["ps4_official_servers_arkpocalypse"] = ps4_official_servers_arkpocalypse
                    data["servers"][1]["ps4_official_servers_hardcore"] = ps4_official_servers_hardcore
                    data["servers"][1]["ps4_total_official_servers_pvp"] = ps4_total_official_servers_pvp
                    data["servers"][1]["ps4_total_official_servers_pve"] = ps4_total_official_servers_pve
                    data["servers"][1]["ps4_total_official_servers"] = ps4_total_official_servers
                    ps4_total_official_players = 0
                    ps4_total_official_pvp_players = 0
                    ps4_total_official_pve_players = 0
                    ps4_official_servers_pvp_players = 0
                    ps4_official_servers_pve_players = 0
                    ps4_official_servers_legacy_players = 0
                    ps4_official_servers_smalls_players = 0
                    ps4_official_servers_arkpocalypse_players = 0
                    ps4_official_servers_hardcore_players = 0
                    for players in await r.json():
                        ps4_total_official_players += players["NumPlayers"]
                        if players["ClusterId"] == "PS4SmallTribesCrossArkCluster":
                            ps4_official_servers_smalls_players += players["NumPlayers"]
                        if players["ClusterId"] == "PS4PVECrossArkCluster":
                            ps4_official_servers_legacy_players += players["NumPlayers"]
                        if players["ClusterId"] == "NewPS4PVPCrossArkCluster":
                            ps4_official_servers_pvp_players += players["NumPlayers"]
                        if players["ClusterId"] == "NewPS4PVECrossArkCluster":
                            ps4_official_servers_pve_players += players["NumPlayers"]
                        if players["SessionIsPve"] == 0:
                            ps4_total_official_pvp_players += players["NumPlayers"]
                        if players["SessionIsPve"] == 1:
                            ps4_total_official_pve_players += players["NumPlayers"]
                        if players["ClusterId"] == "PS4ArkpocalypseCrossArkCluster":
                            ps4_official_servers_arkpocalypse_players += players["NumPlayers"]
                        if players["ClusterId"] == "NewPS4HardcorePVPCrossArkCluster":
                            ps4_official_servers_hardcore_players += players["NumPlayers"]
                    official_servers_players = ps4_total_official_players - ps4_official_servers_smalls_players
                    data["players"][1]["ps4_official_servers_players"] = official_servers_players
                    data["players"][1]["ps4_official_servers_pvp_players"] = ps4_official_servers_pvp_players
                    data["players"][1]["ps4_official_servers_pve_players"] = ps4_official_servers_pve_players
                    data["players"][1]["ps4_official_servers_smalls_players"] = ps4_official_servers_smalls_players
                    data["players"][1]["ps4_official_servers_legacy_players"] = ps4_official_servers_legacy_players
                    data["players"][1]["ps4_official_servers_arkpocalypse_players"] = ps4_official_servers_arkpocalypse_players
                    data["players"][1]["ps4_official_servers_hardcore_players"] = ps4_official_servers_hardcore_players
                    data["players"][1]["ps4_total_official_pvp_players"] = ps4_total_official_pvp_players
                    data["players"][1]["ps4_total_official_pve_players"] = ps4_total_official_pve_players
                    data["players"][1]["ps4_total_official_players"] = ps4_total_official_players
                    with open(filename, "w+") as file:
                        file.write(json.dumps(data, indent=4))
                    print(f"PS4 Official Server Updated - {datetime.utcnow()}")
                else:
                    print(f"PS4 Official Servers Had A Problem, Status Code = {r.status} - {datetime.utcnow()}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")
        try:
            async with session.get("http://arkdedicated.com/xbox/cache/unofficialserverlist.json") as r:
                if r.status == 200:
                    with open(filename, "r") as file:
                        data = json.load(file)
                    text = await r.text()
                    data["etags"][0]["xbox_unofficial_server"] = r.headers["ETag"]
                    xbox_total_unofficial_servers = text.count("AllowDownloadItems")
                    xbox_unofficial_servers_pvp = text.count('"SessionIsPve":0')
                    xbox_unofficial_servers_pve = text.count('"SessionIsPve":1')
                    data["servers"][0]["xbox_unofficial_servers_pvp"] = xbox_unofficial_servers_pvp
                    data["servers"][0]["xbox_unofficial_servers_pve"] = xbox_unofficial_servers_pve
                    data["servers"][0]["xbox_total_unofficial_servers"] = xbox_total_unofficial_servers
                    xbox_total_unofficial_players = 0
                    xbox_unofficial_servers_pvp_players = 0
                    xbox_unofficial_servers_pve_players = 0
                    for players in await r.json():
                        xbox_total_unofficial_players += players["NumPlayers"]
                        if players["SessionIsPve"] == 0:
                            xbox_unofficial_servers_pvp_players += players["NumPlayers"]
                        if players["SessionIsPve"] == 1:
                            xbox_unofficial_servers_pve_players += players["NumPlayers"]
                    data["players"][0]["xbox_unofficial_servers_pvp_players"] = xbox_unofficial_servers_pvp_players
                    data["players"][0]["xbox_unofficial_servers_pve_players"] = xbox_unofficial_servers_pve_players
                    data["players"][0]["xbox_total_unofficial_players"] = xbox_total_unofficial_players
                    with open(filename, "w+") as file:
                        file.write(json.dumps(data, indent=4))
                    print(f"Xbox Unofficial Server Updated - {datetime.utcnow()}")
                else:
                    print(f"Xbox Unofficial Servers Had A Problem, Status Code = {r.status} - {datetime.utcnow()}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")
        try:
            async with session.get("http://arkdedicated.com/ps4/cache/unofficialserverlist.json") as r:
                if r.status == 200:
                    with open(filename, "r") as file:
                        data = json.load(file)
                    text = await r.text()
                    data["etags"][0]["ps4_unofficial_server"] = r.headers["ETag"]
                    ps4_total_unofficial_servers = text.count("AllowDownloadItems")
                    ps4_unofficial_servers_pvp = text.count('"SessionIsPve":0')
                    ps4_unofficial_servers_pve = text.count('"SessionIsPve":1')
                    data["servers"][1]["ps4_unofficial_servers_pvp"] = ps4_unofficial_servers_pvp
                    data["servers"][1]["ps4_unofficial_servers_pve"] = ps4_unofficial_servers_pve
                    data["servers"][1]["ps4_total_unofficial_servers"] = ps4_total_unofficial_servers
                    ps4_total_unofficial_players = 0
                    ps4_unofficial_servers_pvp_players = 0
                    ps4_unofficial_servers_pve_players = 0
                    for players in await r.json():
                        ps4_total_unofficial_players += players["NumPlayers"]
                        if players["SessionIsPve"] == 0:
                            ps4_unofficial_servers_pvp_players += players["NumPlayers"]
                        if players["SessionIsPve"] == 1:
                            ps4_unofficial_servers_pve_players += players["NumPlayers"]
                    data["players"][1]["ps4_unofficial_servers_pvp_players"] = ps4_unofficial_servers_pvp_players
                    data["players"][1]["ps4_unofficial_servers_pve_players"] = ps4_unofficial_servers_pve_players
                    data["players"][1]["ps4_total_unofficial_players"] = ps4_total_unofficial_players
                    with open(filename, "w+") as file:
                        file.write(json.dumps(data, indent=4))
                    print(f"PS4 Unofficial Server Updated - {datetime.utcnow()}")
                else:
                    print(f"PS4 Unofficial Servers Had A Problem, Status Code = {r.status} - {datetime.utcnow()}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                data["bans"][0]["total_bans"] = pc_bans + xbox_bans + ps4_bans
                data["servers"][0]["xbox_total_servers"] = xbox_total_official_servers + xbox_total_unofficial_servers
                data["players"][0]["xbox_total_players"] = xbox_total_official_players + xbox_total_unofficial_players

                data["servers"][1]["ps4_total_servers"] = ps4_total_official_servers + ps4_total_unofficial_servers
                data["players"][1]["ps4_total_players"] = ps4_total_official_players + ps4_total_unofficial_players
            with open(filename, "w+") as file:
                file.write(json.dumps(data, indent=4))
                print(f"Total Servers, Players And Bans Updated - {datetime.utcnow()}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")