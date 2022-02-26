# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 11:14:10 2022

@author: mithr
"""

import discord
import asyncio
from config import token

class freehub_bot(discord.Client):
    async def on_ready(self):
        print("FreeHub started")
        
        
client = freehub_bot()
client.run(token, bot=False)