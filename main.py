import requests
import json
with open('IP.txt', 'r') as f:
    ips = [line.strip() for line in f]

for ip in ips:
    api_url = f"https://api.mcsrvstat.us/2/{ip}"
    
    response = requests.get(api_url)
    server_info = json.loads(response.content)
    
    status = "Online" if server_info.get("online", False) else "Offline"
    version = server_info.get("version", "N/A")
    motd = server_info.get("motd", {}).get("clean", "N/A")
    players_online = server_info.get("players", {}).get("online", "N/A")
    output_str = f"{ip}/{status}/{version}/{motd}/{players_online}"
    
    with open('Stats.txt', 'a',encoding="utf-8") as f:
        f.write(output_str + "\n") 
