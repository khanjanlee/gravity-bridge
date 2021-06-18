
from datetime import datetime
import os
from discord_webhook import DiscordWebhook, DiscordEmbed


url = os.environ["WEB_URL"]
webhook = DiscordWebhook(url=url)

OS = os.environ["RUNNER_OS"]
NAME = os.environ["GITHUB_RUN_ID"]
COMMIT = os.environ["GITHUB_SHA"]
ID = os.environ["GITHUB_JOB"]
EVENT = os.environ["GITHUB_EVENT_NAME"]
AUTHOR = os.environ["GITHUB_ACTOR"]

embed = DiscordEmbed(title=' <:ether:855358106342129664> Gravity Ethereum Node ', description=f'```yaml\nAction : {ID} \nStatus: Successfully build\nEvent : {EVENT}\nCommit : {NAME}\nCommit Hash : {COMMIT}\nOperating System: {OS}\nTime : {str(datetime.now())}```', color='03b2f8')
embed.set_thumbnail(url="https://raw.githubusercontent.com/onomyprotocol/gravity-bridge/main/gravity-bridge.svg")
embed.set_author(name=AUTHOR, url='https://github.com/khanjanlee/gravity-bridge', icon_url='https://media.glassdoor.com/sqll/343398/leewayhertz-squarelogo-1425384496934.png')
embed.add_embed_field(name="**DockerHub**" , value="<:docker:855356086772039680> ** [gravity_eth_image1](https://hub.docker.com/r/leeway302/gravity_eth_image1) **")
embed.add_embed_field(name="**Github**" , value="<:github:855356087494770688> ** [khanjanlee/gravity-bridge](https://github.com/khanjanlee/gravity-bridge) **")
webhook.add_embed(embed)

response = webhook.execute()