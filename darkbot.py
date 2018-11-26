import discord
from discord.ext import commands
import os
import asyncio


client = commands.Bot(description="MultiVerse Official Bot", command_prefix="mv!", pm_help = True)
client.remove_command('help')


#show when it connects to discord
@client.event
async def on_ready():
    for channel in author.server.channels:
        if channel.name == '★verify-for-chatting★':
            role = discord.utils.get(user.server.roles, name="Verified")
        while True:
            reaction = await client.wait_for_reaction(emoji="🇻", message=message)
            await client.add_roles(reaction.message.author, role)
            print('Logged in as')
            print(client.user.name)
        
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
            react_message = await client.send_message(channel, 'React with 🇻 to Verify')
            reaction = '🇻'
            await client.add_reaction(react_message, reaction)
            reaction1 = await client.wait_for_reaction(emoji="🇻", message=react_messagw)
            await client.add_roles(reaction1.message.author, role)    
    
client.run(os.getenv('Token'))
