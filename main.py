import nextcord
from nextcord.ext import commands
import os

bot = commands.Bot(command_prefix="?", description="xmsbt")


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")

    await bot.change_presence(
        status=nextcord.Status.idle,
        activity=nextcord.Activity(
            name="ratio", type=nextcord.ActivityType.watching
        ),
    )

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print("loaded cog")
    else:
        if os.path.isfile(filename):
            print(f"Unable to load {filename[:-3]}")

bot.run(token)
