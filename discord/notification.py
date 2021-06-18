

url = "https://discord.com/api/webhooks/855349363277692969/8upsNV_Hr74JuLmdfH6MOBzY8y5BUISXoa7jdkUiNYQ3Z9XmhBqIRkQP3sGp4Pmi7-UL"
from datetime import datetime

from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url=url)


embed = DiscordEmbed(title=' <:ether:855358106342129664> Gravity Ethereum Node ', description=f'```yaml\nSuccessfully build and pushed to Docker Hub at time {str(datetime.now())}```', color='03b2f8')
embed.set_thumbnail(url="https://raw.githubusercontent.com/onomyprotocol/gravity-bridge/main/gravity-bridge.svg")
embed.set_author(name='Khanjan', url='https://github.com/khanjanlee/gravity-bridge', icon_url='https://media.glassdoor.com/sqll/343398/leewayhertz-squarelogo-1425384496934.png')
embed.add_embed_field(name="**DockerHub**" , value="<:docker:855356086772039680> ** [gravity_eth_image1](https://hub.docker.com/r/leeway302/gravity_eth_image1) **")
embed.add_embed_field(name="**Github**" , value="<:github:855356087494770688> ** [khanjanlee/gravity-bridge](https://github.com/khanjanlee/gravity-bridge) **")
webhook.add_embed(embed)

response = webhook.execute()