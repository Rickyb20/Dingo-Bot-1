import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import urllib.parse
import math
import time

load_dotenv()
TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")
STARTING_ACT = "the prefix " + PREFIX
HELP_COLOR = discord.Color.from_rgb(162, 246, 56)

bot = commands.Bot(command_prefix=PREFIX)
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=STARTING_ACT))
    print(f"{bot.user} has connected to Discord!")

@bot.command(aliases=["sell"])
async def sellback(ctx, *args):
    if len(args) == 2:
        try:
            num = int(args[0])
        except ValueError:
            await ctx.send("Please enter a valid non-zero, non-negative number.")
        else:
            if args[1].upper() == "AC":
                await ctx.send("**First 24 Hours:** " + str(math.ceil(num*0.9)) + " AC\n**After 24 Hours:** " + str(math.ceil(num*0.25)) + " AC")
            elif args[1].upper() == "GOLD":
                await ctx.send(str(math.ceil(num*0.25)) + " Gold")
            else:
                await ctx.send("Please indicate if the item is AC or Gold.")
    else:
        await ctx.send("Please use the syntax: " + PREFIX + "sellback <price> <AC/Gold>")

@bot.command()
async def char(ctx, *args):
    if len(args) > 0:
        await ctx.send("Link: http://www.aq.com/character.asp?id=" + urllib.parse.quote(" ".join(args)))
    else:
        await ctx.send("Please specify a name after " + PREFIX + "char")

@bot.command()
async def aq3dchar(ctx, *args):
    if len(args) > 0:
        await ctx.send("Link: https://game.aq3d.com/account/Character?id=" + urllib.parse.quote(" ".join(args)))
    else:
        await ctx.send("Please specify a name after " + PREFIX + "aq3dchar")

@bot.command()
async def wiki(ctx, *args):
    if len(args) > 0:
        await ctx.send("Wiki search: http://aqwwiki.wikidot.com/search:site/q/" + urllib.parse.quote(" ".join(args)))
    else:
        await ctx.send("Please specify what you want to search after " + PREFIX + "wiki")

@bot.command()
async def aq3dwiki(ctx, *args):
    if len(args) > 0:
        await ctx.send("Wiki search: http://aq-3d.wikidot.com/search:site/q/" + urllib.parse.quote(" ".join(args)))
    else:
        await ctx.send("Please specify what you want to search after " + PREFIX + "aq3dwiki")

@bot.command(aliases=["commands"])
async def help(ctx):
    embed = discord.Embed(title="Commands", description="These are my available commands. Woof.", color=HELP_COLOR)
    embed.set_author(name="Lt. Dingo", icon_url="https://i.imgur.com/udByUnW.png")
    embed.set_thumbnail(url="https://i.imgur.com/VjRmBoF.png")
    embed.add_field(name=PREFIX + "sellback X Y or " + PREFIX + "sell X Y", value="Returns the sellback value for price **X** in **Y** currency (AC or Gold).", inline=False)
    embed.add_field(name=PREFIX + "char PLAYER", value="Returns the character page for **PLAYER** in AQWorlds.", inline=False)
    embed.add_field(name=PREFIX + "aq3dchar PLAYER", value="Returns the character page for **PLAYER** in AQ3D.", inline=False)
    embed.add_field(name=PREFIX + "wiki", value="Searches the AQWWiki for your input.", inline=False)
    embed.add_field(name=PREFIX + "aq3dwiki", value="Searches the AQ3DWiki for your input.", inline=False)
    embed.add_field(name=PREFIX + "help or " + PREFIX + "commands", value="Returns this help box.", inline=False)
    embed.set_footer(text="That's all, folks. Woof out.")
    await ctx.send(embed=embed)

@bot.command()
async def activity(ctx, *args):
    if len(args) > 0:
        await bot.change_presence(activity=discord.Game(name=" ".join(args)))
        await ctx.send("Changed activity to " + " ".join(args))
    else:
        await ctx.send("Please specify an activity for the bot to do")

@bot.command()
async def close(ctx):
    await ctx.send("Logging out!")
    await bot.close()

bot.run(TOKEN)