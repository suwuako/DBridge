import discord
import json

from datetime import datetime
from discord.ext import commands


class elevated(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.now()
        self.secret = json.load(open("config/secret.json"))

        print("elevated_commands loaded")

    @commands.command()
    async def add(self, message):
        if message.author.id not in self.secret["sudoers"]:
            print(f"{message.author} is not in the sudoers file")
            return

        content = message.message.content

        # Remove ;add from the message.message.content


        print(message.message.content)


def setup(bot):
    bot.add_cog(elevated(bot))