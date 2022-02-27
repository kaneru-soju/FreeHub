# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 11:14:10 2022

@author: mithr
"""

import discord
import asyncio

from discord import client
from discord.ext import commands

import FreebieInfo
import scraper
import validators

from config import token


class freehub_bot(discord.Client):
    def __init__(self):
        super().__init__()
        self.channel = None
        self.pings = False
        self.ebook_role = None
        self.freebie_role = None
        self.game_role = None
        self.sticker_role = None

    async def on_ready(self):

        print("FreeHub started")

    async def on_message(self, message: discord.Message):
        # if "!role" in message.content:
        #     role = message.content[6:]
        #     self.addrole(ctx=, role)
        if "!ping" in message.content:
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

    # @client.command()
    # @commands.has_role("Admin")
    # def addrole(ctx, role_name):
    #     user = ctx.message.author
    #     role = discord.utils.get(user.server.roles, name=role_name)
    #     await client.add_roles(user, role)



    async def post_freebie(self, data: FreebieInfo):
        if self.pings:
            await self.channel.send(f"<@{self.ping_role}> Here's a freebie! \n {data.__str__()}")
        else:
            if data.get_information() is None:
                info = "n/a"
            else:
                info = data.get_information().capitalize()
            sr = data.get_subreddit().lower()
            if sr == "freeebooks":
                await self.channel.send("<@&947339276977336390>")
            elif sr == "freegamefindings":
                await self.channel.send("<@&947339509899591760>")
            elif sr == "freestickers":
                await self.channel.send("<@&947339308967276605>")
            elif sr == "freebies":
                await self.channel.send("<@&947339496138108929>")

            cut_title = data.get_title()[0:255]
            embedVar = discord.Embed(title=cut_title, url=data.get_link(), description=info,
                                     color=discord.Color.green())
            embedVar.add_field(name="Subreddit", value=data.get_subreddit())
            embedVar.add_field(name="Upvote Ratio", value=str((float(data.get_upvote()) * 100))[0:2] + "%")
            if validators.url(data.get_image()):
                embedVar.set_thumbnail(url=data.get_image())
            else:
                if sr == "freeebooks":
                    embedVar.set_thumbnail(url="https://raw.githubusercontent.com/kaneru-soju/FreeHub/main/book.jpg")
                elif sr == "freegamefindings":
                    embedVar.set_thumbnail(url="https://github.com/kaneru-soju/FreeHub/blob/main/game.png?raw=true")
                elif sr == "freestickers":
                    embedVar.set_thumbnail(url="https://github.com/kaneru-soju/FreeHub/blob/main/sticker.png?raw=true")
                elif sr == "freebies":
                    embedVar.set_thumbnail(url="https://github.com/kaneru-soju/FreeHub/blob/main/freebie.png?raw=true")
            await self.channel.send(embed=embedVar)


client = freehub_bot()
client.run(token)
