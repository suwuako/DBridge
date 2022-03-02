import asyncio
import discord
import json
import src.lib as lib

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

        commands = json.load(open("config/commands.json"))

        await message.send(f"Here is a dict all current commands: ```{json.dumps(commands, indent=4, sort_keys=True)}```")
        name = await lib.respond(message, "Enter command name: (60s timeout)", self.bot)
        await message.send("**[WARNING]** do NOT give commands {args} without knowing what the command does;"
                           " for instance, `cat` can be used for json/secret.json and leak the bot token")
        if name is None:
            return

        if name.content in commands:
            await message.send(f"{name} is already in commands.json")

        bash = await lib.respond(message, "Enter command: (timeout 60s)", self.bot)
        if bash is None:
            return

        commands[name.content] = bash.content
        lib.write_to_json("config/commands.json", commands)

        await message.send(f"Successfully added `{name.content}` to exec `{bash.content}`")

    @commands.command()
    async def remove(self, message):
        if message.author.id not in self.secret["sudoers"]:
            print(f"{message.author} is not in the sudoers file")
            return

        commands = json.load(open("config/commands.json"))

        await message.send(f"Here is a dict all current commands: ```{json.dumps(commands, indent=4, sort_keys=True)}```")
        name = await lib.respond(message, "Enter command name: (timeout 60s)", self.bot)
        if name is None or name.content not in commands:
            return

        del commands[name.content]
        lib.write_to_json("config/commands.json", commands)

        await message.send(f"Successfully removed `{name.content}`")

    @commands.command()
    async def python(self, message):
        if message.author.id not in self.secret["sudoers"]:
            print(f"{message.author} is not in the sudoers file")
            return

def setup(bot):
    bot.add_cog(elevated(bot))