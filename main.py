import asyncio
import toml
from functions import scraper

config = toml.load('config.toml')
print("config loaded")

SLACK_WEBHOOK_URL = config['slack']['webhook_url']

target_url = "https://searchengineland.com/library/ppc"

result = asyncio.get_event_loop().run_until_complete(scraper.openURL(target_url))
print(result)