#nerd

import discord
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import Pymoe
import simplejson as json
import requests as rq
from champs import champs
import os
import image_links





api = os.environ['RIOT_KEY']
wu_key='c8034bd5f8c70795'



An=Pymoe.Anilist()


startup_extensions = ('Music')
bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print('Bot has now been loaded')

class Main_Commands() :
    def __init__(self, bot):
     self.bot = bot


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(':ping_pong: Ping=30ms')

@bot.command(pass_context=True)
async def profile(ctx, user: discord.Member):
    await bot.say("```User's name is: {}".format(user.name)+"\n\nUser's ID is: {}".format(user.id)+"\n\nUser joined at: {}```".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say('RIP {}'.format(user.name))
    await bot.kick(user)
    print ('{} has been kicked from the server'.format(user.name))

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await bot.say('Well cant rejoin now nerd({})'.format(user.name))
    await bot.ban(user)
    print ('OOF {} has been banned'.format(user.name))


@bot.command(pass_context=True)
async def howtoplay(ctx):
    embed = discord.Embed(title='Rules', description='Dont u dare abuse', color=0x00ff00)
    embed.set_footer(text='Tag Fiery(vansh) or Akshat if u want to play anything with us')
    await bot.say(embed=embed)

if __name__== '__main__':
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = ' {}: {}'.format(type(e).__name__, e)
            print('Failed to load extensions {}\n{}'.format(extension, exc))    

    

bot.run(os.environ['BOT_TOKEN'])
     
