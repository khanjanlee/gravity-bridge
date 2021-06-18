

url = "https://discord.com/api/webhooks/855345877279703051/PMbAVWOohJrJreAUOtgNyFWGjYUCWoXUY5Uryw2tv5y2UXmEM4CxVyTHVJwsUCKHZ4iM"
from datetime import datetime
from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url=url, content=f'Etherum  gravity node image built successfully at {str(datetime.now())}')
response = webhook.execute()