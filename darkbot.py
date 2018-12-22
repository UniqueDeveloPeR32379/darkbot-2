import discord
from discord.ext import commands
import os
import random
import json
import asyncio
import time

client = commands.Bot(description="MultiVerse Official Bot", command_prefix=commands.when_mentioned_or("mv!"), pm_help = True)
client.remove_command('help')

    
#show when it connects to discord
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)

@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "🇻":
        role = discord.utils.get(reaction.message.server.roles, name="Verified")
        await client.add_roles(user, role)
	
@client.event
async def on_reaction_remove(reaction, user):
    verifychannel = "★verify-for-chatting★"
    for channel in user.server.channels:
      if channel.name != verifychannel:
          return
      if str(reaction.emoji) == "🇻":
          role = discord.utils.get(user.server.roles, name="Verified")
          await client.remove_roles(user, role)
        
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setreactionverify(ctx):
    author = ctx.message.author
    server = ctx.message.server
    everyone_perms = discord.PermissionOverwrite(send_messages=False,read_messages=True)
    everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
    await client.create_channel(server, '★verify-for-chatting★',everyone)
    for channel in author.server.channels:
        if channel.name == '★verify-for-chatting★':
            react_message = await client.send_message(channel, 'React with 🇻 to Verify | Sometimes it not works so you can also use mv!verify anywhere(Where you can send messages)')
            reaction = '🇻'
            await client.add_reaction(react_message, reaction)
  
@client.command(pass_context=True)
async def remind(ctx, time=None, *,remind=None):
    time =int(time)
    time = time * 60
    output = time/60
    await client.say("I will remind {} after {} minutes for {}".format(ctx.message.author.name, output, remind))
    await asyncio.sleep(time)
    await client.say("Reminder: {} by {}".format(remind, ctx.message.author.mention))
    await client.send_message(ctx.message.author, "Reminder: {}".format(remind))


client.run(os.getenv('Token'))
