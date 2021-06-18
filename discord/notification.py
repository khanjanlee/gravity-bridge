

url = "https://discord.com/api/webhooks/855345877279703051/PMbAVWOohJrJreAUOtgNyFWGjYUCWoXUY5Uryw2tv5y2UXmEM4CxVyTHVJwsUCKHZ4iM"
from datetime import datetime

from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='your webhook url')

# create embed object for webhook
# you can set the color as a decimal (color=242424) or hex (color='03b2f8') number
embed = DiscordEmbed(title='Gravity Ethereum Node ', description=f'Successfully build and pushed to [dockerhub](https://hub.docker.com/r/leeway302/gravity_eth_image1) at time {str(datetime.now())} ', color='03b2f8')

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()