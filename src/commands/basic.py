import os
import json
import discord
import src.lib as lib

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
    async def list(self, message):
        commands = json.load(open("config/commands.json"))

        await message.message.reply(json.dumps(commands, indent=4, sort_keys=True))

    @commands.command()
    async def run(self, message):
        global arguments
        commands = json.load(open("config/commands.json"))
        await message.message.reply(f"Here is a list of all user commands: ```{json.dumps(commands, indent=4, sort_keys=True)}```")
        command = await lib.respond(message, "Enter command name you would like to exec: (timeout 60s)", self.bot)
        command = command.content

        async def run_as_async(run, arguments):
            # Remove literal string "{args}" so command wont run {args} + arguments
            run = commands[command].replace("{args}", "")
            return os.popen(f"{run} {arguments.content}")

        if command in commands:
            if "{args}" in commands[command]:
                arguments = await lib.respond(message, "Enter argument you would like to pass)", self.bot)

            output = await run_as_async(commands[command], arguments)
            await message.send(f"```{output.read()}```")

        else:
            await message.send(f"{command} is not in commands.json.")

def setup(bot):
    bot.add_cog(basic(bot))