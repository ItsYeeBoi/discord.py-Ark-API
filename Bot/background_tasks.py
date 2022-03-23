from datetime import datetime
import json
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
                    data["etags"][0]["official_server"] = r.headers["ETag"]
                    total_official_servers = text.count("AllowDownloadItems")
                    official_servers_smalls = text.count("XboxSmallTribes")
                    official_servers = total_official_servers - official_servers_smalls
                    official_servers_pvp = text.count("NewXboxPVP")
                    official_servers_pve = text.count("NewXboxPVE")
                    official_servers_legacy = text.count('"XboxPVE"')
                    official_servers_arkpocalypse = text.count("XboxArkpocalypse")
                    official_servers_hardcore = text.count("NewXboxHardcorePVP")
                    total_official_servers_pvp = text.count('"SessionIsPve":0')
                    total_official_servers_pve = text.count('"SessionIsPve":1')
                    data["servers"][0]["official_servers"] = official_servers
                    data["servers"][0]["official_servers_pvp"] = official_servers_pvp
                    data["servers"][0]["official_servers_pve"] = official_servers_pve
                    data["servers"][0]["official_servers_smalls"] = official_servers_smalls
                    data["servers"][0]["official_servers_legacy"] = official_servers_legacy
                    data["servers"][0]["official_servers_arkpocalypse"] = official_servers_arkpocalypse
                    data["servers"][0]["official_servers_hardcore"] = official_servers_hardcore
                    data["servers"][0]["total_official_servers_pvp"] = total_official_servers_pvp
                    data["servers"][0]["total_official_servers_pve"] = total_official_servers_pve
                    data["servers"][0]["total_official_servers"] = total_official_servers
                    total_official_players = 0
                    total_official_pvp_players = 0
                    total_official_pve_players = 0
                    official_servers_pvp_players = 0
                    official_servers_pve_players = 0
                    official_servers_legacy_players = 0
                    official_servers_smalls_players = 0
                    official_servers_arkpocalypse_players = 0
                    official_servers_hardcore_players = 0
                    for players in await r.json():
                        total_official_players += players["NumPlayers"]
                        if players["ClusterId"] == "XboxSmallTribes":
                            official_servers_smalls_players += players["NumPlayers"]
                        if players["ClusterId"] == "XboxPVE":
                            official_servers_legacy_players += players["NumPlayers"]
                        if players["ClusterId"] == "NewXboxPVP":
                            official_servers_pvp_players += players["NumPlayers"]
                        if players["ClusterId"] == "NewXboxPVE":
                            official_servers_pve_players += players["NumPlayers"]
                        if players["SessionIsPve"] == 0:
                            total_official_pvp_players += players["NumPlayers"]
                        if players["SessionIsPve"] == 1:
                            total_official_pve_players += players["NumPlayers"]
                        if players["ClusterId"] == "XboxArkpocalypse":
                            official_servers_arkpocalypse_players += players["NumPlayers"]
                        if players["ClusterId"] == "NewXboxHardcorePVP":
                            official_servers_hardcore_players += players["NumPlayers"]
                    official_servers_players = total_official_players - official_servers_smalls_players
                    data["players"][0]["official_servers_players"] = official_servers_players
                    data["players"][0]["official_servers_pvp_players"] = official_servers_pvp_players
                    data["players"][0]["official_servers_pve_players"] = official_servers_pve_players
                    data["players"][0]["official_servers_smalls_players"] = official_servers_smalls_players
                    data["players"][0]["official_servers_legacy_players"] = official_servers_legacy_players
                    data["players"][0]["official_servers_arkpocalypse_players"] = official_servers_arkpocalypse_players
                    data["players"][0]["official_servers_hardcore_players"] = official_servers_hardcore_players
                    data["players"][0]["total_official_pvp_players"] = total_official_pvp_players
                    data["players"][0]["total_official_pve_players"] = total_official_pve_players
                    data["players"][0]["total_official_players"] = total_official_players
                    with open(filename, "w+") as file:
                        file.write(json.dumps(data, indent=4))
                    print(f"Official Server Updated - {datetime.utcnow()}")
                else:
                    print(f"Official Servers Had A Problem, Status Code = {r.status} - {datetime.utcnow()}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")
        try:
            async with session.get("http://arkdedicated.com/xbox/cache/unofficialserverlist.json") as r:
                if r.status == 200:
                    with open(filename, "r") as file:
                        data = json.load(file)
                    text = await r.text()
                    data["etags"][0]["unofficial_server"] = r.headers["ETag"]
                    total_unofficial_servers = text.count("AllowDownloadItems")
                    unofficial_servers_pvp = text.count('"SessionIsPve":0')
                    unofficial_servers_pve = text.count('"SessionIsPve":1')
                    data["servers"][0]["unofficial_servers_pvp"] = unofficial_servers_pvp
                    data["servers"][0]["unofficial_servers_pve"] = unofficial_servers_pve
                    data["servers"][0]["total_unofficial_servers"] = total_unofficial_servers
                    total_unofficial_players = 0
                    unofficial_servers_pvp_players = 0
                    unofficial_servers_pve_players = 0
                    for players in await r.json():
                        total_unofficial_players += players["NumPlayers"]
                        if players["SessionIsPve"] == 0:
                            unofficial_servers_pvp_players += players["NumPlayers"]
                        if players["SessionIsPve"] == 1:
                            unofficial_servers_pve_players += players["NumPlayers"]
                    data["players"][0]["unofficial_servers_pvp_players"] = unofficial_servers_pvp_players
                    data["players"][0]["unofficial_servers_pve_players"] = unofficial_servers_pve_players
                    data["players"][0]["total_unofficial_players"] = total_unofficial_players
                    with open(filename, "w+") as file:
                        file.write(json.dumps(data, indent=4))
                    print(f"Unofficial Server Updated - {datetime.utcnow()}")
                else:
                    print(f"Unofficial Servers Had A Problem, Status Code = {r.status} - {datetime.utcnow()}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                data["bans"][0]["total_bans"] = pc_bans + xbox_bans + ps4_bans
                data["servers"][0]["total_servers"] = total_official_servers + total_unofficial_servers
                data["players"][0]["total_players"] = total_official_players + total_unofficial_players
            with open(filename, "w+") as file:
                file.write(json.dumps(data, indent=4))
                print(f"Total Servers, Players And Bans Updated - {datetime.utcnow()}")
        except Exception as error:
            print(f"There Was An Error: {type(error).__name__} - {datetime.utcnow()}")