import discord
import json
import os.path
import asyncio
import random

client = discord.Client()

 

@client.event
async def on_ready():
    print(client.user.name)
    print("===================")


@client.event
async def on_message(message):
    user_id = message.author.id

    author_level = get_level(user_id)
    author_xp = get_xp(user_id)

    if author_level == 0 and author_xp >= 100:
        set_level(user_id, 1)
        await client.send_message(message.channel, "You are at Level 1")

    if author_level == 1 and author_xp >= 500:
        set_level(user_id, 2)
        await client.send_message(message.channel, "You are at Level 2")
    if author_level == 2 and author_xp >= 1200:
        set_level(user_id, 3)
        await client.send_message(message.channel, "You are at Level 3")
    if author_level == 3 and author_xp >= 2000:
        set_level(user_id, 4)
        await client.send_message(message.channel, "You are at Level 4")
        lvl_role = None
        for role in message.server.roles:
             if role.name == "Regulars":
                lvl_role = role

        await client.add_roles(message.author, lvl_role)

    if message.content.lower().startswith('d!xp'):
        await client.send_message(message.channel, "**You have** `{}` **XP!**".format(get_xp(message.author.id)))

    if message.content.lower().startswith('d!lvl'):
        level = get_level(user_id)
        await client.send_message(message.channel, "**Your Level is:** {}".format(level))

    user_add_xp(message.author.id, 1)


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


def set_level(user_id: int, level: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        users[user_id]["level"] = level
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_level(user_id: int):
    if os.path.isfile('users.json'):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            return users[user_id]['level']
        except KeyError:
            return 0
     

client.run(os.getenv('Token'))
