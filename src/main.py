import requests
import discord
import json
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

prefix = config['General']['prefix']
token = config['General']['token']

intents = discord.Intents.default()
intents.messages = True
intents.members = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print("Storm Development Bot Is Online")
    print(f"Prefix: {bot.command_prefix}")
    print(f"Members: {len(bot.users)}")

@bot.command()
async def history(ctx, member: discord.Member):
    try:
        r = requests.get(f"https://stormss.cc/api/history/{member.id}")
        r.raise_for_status()
        data = r.json()
        
        if data:
            embed = discord.Embed(title=f"History for {member.name}")
            for key, value in data.items():
                embed.add_field(name=key, value=value, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No history found for this member.")
    except:
        await ctx.send(f"Failed to fetch history for {member.id}.")

@bot.command()
async def results(ctx, pin: str):
    try:
        r = requests.get(f"https://stormss.cc/api/results/{pin}")
        r.raise_for_status()
        data = r.json()
        
        if data:
            embed = discord.Embed(title=f"Results for {pin}")
            for key, value in data.items():
                embed.add_field(name=key, value=value, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No results found for this PIN.")
    except:
        await ctx.send(f"Failed to fetch results for {pin}.")


if __name__ == "__main__":
    bot.run(token)