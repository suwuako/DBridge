import json
import discord
import asyncio

from discord.ext import commands


class sshBot:
    def __init__(self):
        self.secret = json.load(open("config/secret.json"))

        @bot.event
        async def on_ready():
            print("init")
            await bot.change_presence(activity=discord.Streaming(name='127.0.0.1',
                                                                 url='https://www.youtube.com/watch?v=c6VhcpwFZJM'))

    def load_cogs(self):
        bot.load_extension("src.commands.basic")
        bot.load_extension("src.commands.elevated")

    def run(self):
        self.load_cogs()
        bot.run(self.secret["token"])


if __name__ == "__main__":
    bot = commands.Bot(command_prefix=';')
    bot.remove_command('help')

    sshBot = sshBot()
    sshBot.run()

