import discord
import asyncio
from datetime import datetime
import pytz
import os

TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = 1491178939983331459

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_morning_message():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    tz = pytz.timezone("America/New_York")

    while not client.is_closed():
        now = datetime.now(tz)
        if now.weekday() == 0 and now.hour == 9 and now.minute == 0:
            await channel.send("@everyone Good morning! ☀️ Let's have a nice and productive week & make a bunch of money 💲 so we can spend it all on SKINS!")
            await asyncio.sleep(60)
        await asyncio.sleep(30)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    client.loop.create_task(send_morning_message())

client.run(TOKEN)
