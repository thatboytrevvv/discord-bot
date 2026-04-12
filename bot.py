import discord
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio
 
TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = 1491178939983331459
 
intents = discord.Intents.default()
client = discord.Client(intents=intents)
scheduler = AsyncIOScheduler(timezone="America/New_York")
 
async def send_morning_message():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("@everyone Good morning! ☀️ Let's have a nice and productive week & make a bunch of money 💲 so we can spend it all on SKINS!")
    else:
        print("Channel not found!")
 
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    scheduler.add_job(send_morning_message, CronTrigger(day_of_week="mon", hour=9, minute=0))
    scheduler.start()
 
client.run(TOKEN)
