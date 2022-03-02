import discord
import json
import asyncio

async def respond(message, text, bot):
    def check(m: discord.Message):
        return m.author.id == message.author.id and m.channel.id == message.channel.id

    await message.message.reply(text)

    try:
        item = await bot.wait_for(event="message", check=check, timeout=60.0)

    except asyncio.TimeoutError:
        await message.send("timeout error")
        return None

    return item

def write_to_json(path, dict):
    with open(path, "w") as json_file:
        json.dump(dict, json_file, indent=4, sort_keys=True)