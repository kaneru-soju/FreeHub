# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 11:14:10 2022

@author: mithr
"""

import discord
import asyncio
import FreebieInfo

from config import token


class freehub_bot(discord.Client):
    def __init__(self):
        super().__init__()
        self.channel = None
        self.pings = False
        self.ping_role = None

    async def on_ready(self):
        print("FreeHub started")

    async def on_message(self, message: discord.Message):
        if "!role" in message.content:
            self.ping_role = message.content[6:]
            await message.channel.send("Kaneru is so hot role")
        elif "!ping" in message.content:
            self.pings = not self.pings
            await message.channel.send("Kaneru is so hot ping")
        elif "!channel" in message.content:
            self.channel = message.channel
            await message.channel.send("Kaneru is so hot channel")

    async def post_freebie(self, data: FreebieInfo):
        if self.pings:
            await self.channel.send(f"<@{self.ping_role}> Here's a freebie! \n {data.__str__()}")
        else:
            await self.channel.send(f"Here's a freebie! \n {data.__str__()}")


client = freehub_bot()
client.run(token)
