import os
import discord

from datetime import datetime
from discord.ext import commands

class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.now()
        print("basic_commands loaded")

    @commands.command()
    async def ping(self, message):
        then = datetime.now()

        message = await message.send("<a:fox_ears:944222338243780640> Pong!")
        latency = datetime.now() - then
        await message.edit(content=f"<a:fox_ears:944222338243780640> Pong!\n"
                                   f"[latency: {latency}] ")

        edit_latency = datetime.now() - then
        await message.edit(content=f"<a:fox_ears:944222338243780640> Pong!\n"
                                   f"[latency: {latency} (ms)] \n"
                                   f"[edit latency: {edit_latency}] (ms)")

    @commands.command()
    async def run(self, message):
        output = os.popen("ls")

        while output.readline():
            print(output.readline)

def setup(bot):
    bot.add_cog(basic(bot))