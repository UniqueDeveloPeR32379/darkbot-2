import discord
import json
import os.path
import asyncio
import random

client = discord.Client()
gamble_msg_stuff = {}
 

@client.event
async def on_ready():
    print(client.user.name)
    print("===================")


@client.event
@client.event
async def on_message(message):
    user_id = message.author.id
    author_xp = get_xp(user_id)

    if message.content.lower().startswith('d!gamble'):
        # !gamble 10
        try:
            value = abs(int(message.content.lower().replace('d!gamble', '').replace(' ', '')))

            if author_xp >= value:
                embed = discord.Embed(
                    title="Gamble Game:",
                    description="- 10% Chance = 🌓\n"
                                "- 45% Chance = 🌑\n"
                                "- 45% Chance = 🌕"
                )
                msg = await client.send_message(message.channel, embed=embed)
                await client.add_reaction(msg, "🌓")
                await client.add_reaction(msg, "🌑")
                await client.add_reaction(msg, "🌕")

                gamble_msg_stuff[user_id] = {"g_msg_id": msg.id, "g_user_id": user_id, "g_value": value}
            else:
                await client.send_message(message.author, "You didn't got xp!")
        except ValueError:
            await client.send_message(message.channel, "Use it like d!gamble 10")


def user_add_xp(user_id: int, xp: int):
    if os.path.isfile("users.json"):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['xp'] += xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['xp'] = xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['xp'] = xp
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_xp(user_id: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['xp']
    else:
        return 0

     

client.run(os.getenv('Token'))
