import discord
from discord.ext import commands
global token
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjE1ZGM5NmYzLWQ0NmUtNGRhYS05M2Y5LTU5Y2Q2YTRiMzU4MCIsImlhdCI6MTY2NzczMDIyNiwic3ViIjoiZGV2ZWxvcGVyL2IxYTNiMGE2LTMzOTItZjRjYS0yMWYwLWIzYzljYTY0NmFhZSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNzkuMTA1LjExNy4yMzUiXSwidHlwZSI6ImNsaWVudCJ9XX0.iEVrEQqRPOJl9H3IPsPwR9Kco4gUOSdol8H0Nu7-las35zj1PDKNBhrbJgm1aMmYEd8nEkpLR5m3_PlYBxCAvw"

intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
# Задаём префикс и интенты
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

bot.run("MTAzODcxNzg5NzQwMjQ5MDkxMQ.Grmm5a.W2kVWnROCyE95XazEPOjZUv2MNvIWfGbDguV9o")