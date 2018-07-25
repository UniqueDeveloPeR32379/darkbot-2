import discord
import json
import os.path

client = discord.Client()

 

@client.event
async def on_ready():
    print(client.user.name)
    print("===================")


@client.event
async def on_message(message):

    if message.content.lower().startswith('.test'):
        await client.send_message(message.channel, "Test")

    if message.content.lower().startswith('.xp'):
        await client.send_message(message.channel, "You have `{}` XP!".format(get_xp(message.author.id)))

    user_add_xp(message.author.id, 2)


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
