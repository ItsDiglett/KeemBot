import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from config import token2
import asyncio
import os

client = commands.Bot(command_prefix = '^')

#This gets your current working directory and loads the soundfiles
print(os.getcwd())
print(os.listdir('soundclips'))

#This tells you when the bot is online. 
@client.event
async def on_ready():
        print('It\'s alive!')

#Everything under here is racist
@client.command(pass_context=True)
async def keem(ctx):
            channel = ctx.message.author.voice.channel
            server = ctx.message.guild.voice_client
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('soundclips/keem.mp3'), after=lambda e: print('done', e))
            await asyncio.sleep(0.1)
            while vc.is_playing():
                    await asyncio.sleep(0.1)
            vc.stop()
            await vc.disconnect()

@client.command(pass_context=True)
async def pewd(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('soundclips/pewd.wav'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()

@client.command(pass_context=True)
async def spongebob(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('soundclips/spongebob.wav'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()

@client.command(pass_context=True)
async def alex(ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('soundclips/alex.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(0.1)
        while vc.is_playing():
                await asyncio.sleep(0.1)
        vc.stop()
        await vc.disconnect()

client.run(token2)
