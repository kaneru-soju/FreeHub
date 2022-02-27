# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 11:14:10 2022

@author: mithr
"""

import discord
import asyncio
import FreebieInfo
import scraper
import validators

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
            await message.channel.send("Role was set!")
        elif "!ping" in message.content:
            self.pings = not self.pings
            if self.pings:
                await message.channel.send("Ping's are now enabled!")
            else:
                await message.channel.send("Ping's are now disabled!")
        elif "!channel" in message.content:
            self.channel = message.channel
            await message.channel.send("Kaneru is so hot channel")
        elif "!*" in message.content:
            self.channel = message.channel
            sr = "freebies+freegamefindings+freestickers+freeebooks"
            data_harvester = scraper.utils(self, sr)
            await data_harvester.start_sending_posts()

    async def post_freebie(self, data: FreebieInfo):
        if self.pings:
            await self.channel.send(f"<@{self.ping_role}> Here's a freebie! \n {data.__str__()}")
        else:

            embedVar = discord.Embed(title=data.get_title(), url=data.get_link(), description=data.get_information(),
                                  color=discord.Color.green())

            if validators.url(data.get_image()):
                embedVar.set_thumbnail(url=data.get_image())
            else:
                embedVar.set_thumbnail(url="book.jpg")

            await self.channel.send(embed=embedVar)


client = freehub_bot()
client.run(token)
