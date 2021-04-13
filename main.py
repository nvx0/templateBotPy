import discord
import json
from discord.ext import commands
token = "token"

bot = commands.Bot(command_prefix=when_mentioned_or="!")

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.idle, activity=discord.Game('cloud3.site'))
  print(f"<---------- Logged in! --------->")

@bot.command(aliases=['Hi'])
async def test(ctx):
await ctx.send("Hello")

bot.run(token)
