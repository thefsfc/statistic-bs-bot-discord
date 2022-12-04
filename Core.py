import discord
from discord.ext import commands
global token
token = "brawl.api.token"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="Brawl Stats"))
	print("Bot Ready To Work!")

@bot.command()
async def test(ctx, arg):
    client = brawlstats.Client(token)
    player=client.get_profile(arg)
    cups=player.trophies
    hight=player.highest_trophies
    expl=player.exp_level
    expp=player.exp_points
    tvtv=player.x3vs3_victories
    tv=player.team_victories
    sv=player.solo_victories
    dv=player.duo_victories
    cn=player.club.name
    all = "Username & Tag: " + str(player) + "\n" + "Trophies: " + str(cups) + "\n" + "Max Trophies: " + str(hight) + "\n" + "EXP LvL: " + str(expl) + "\n" + "EXP Points: " + str(expp) + "\n" + "3 VS 3 Wins: " + str(tvtv) + "\n" + "Team Wins: " + str(tv) + "\n" + "Solo Wins: " + str(sv) + "\n" + "Duo Wins:" + str(dv) + "\n" + "Player Club Name: " + str(cn)
    await ctx.reply(all)

bot.run("your.bot.token")
