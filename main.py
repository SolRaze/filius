# Imports

from discord.ext import commands
import os
from keep_online import keep_online

# Bot setup

client = commands.Bot(command_prefix="/", help_command=None)

# Custom status for bot

statuses = []

# Checks if bot is ready


@client.event
async def on_ready():
    print("{0.user} is online".format(client))


# Keeps the bot running

keep_online()

# Cogs to organize commands collection

extensions = ['cogs.misc_command']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)

# Runs the bot

client.run(os.environ['TOKEN'])
