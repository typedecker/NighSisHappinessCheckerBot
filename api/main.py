# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:58:08 2022

@author: DELL
"""

import nest_asyncio
nest_asyncio.apply()

import discord, os, traceback, asyncio

intents = discord.Intents(guilds = True, dm_messages = True, members = True, messages = True, guild_messages = True, invites = True, message_content = True)
client = discord.Client(chunk_guilds_at_startup = True, intents = intents)

async def tasks_loop() :
    # DO STUFF HERE, ONCE READY, THEN UNCOMMENT THE SECOND LINE OF ON_READY FUNC
    # https://stackoverflow.com/questions/64173987/how-to-make-the-bot-run-a-defined-function-at-a-specific-time-everyday-in-discor
    
    await client.wait_until_ready()
    
    while not client.is_closed():
        try :
            nigh = client.get_user(624596508070772750)
            if nigh.dm_channel == None :
                await nigh.create_dm()
            await nigh.dm_channel.send('Sisterrr are you happy?')
        except :
            print('Sissy Nigh could not be found :( T_T where did they go?')
        await asyncio.sleep(1800)
    return

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    client.loop.create_task(tasks_loop())
    
    game = discord.Game("Making sure that Nigh Sis is happy <3!")
    await client.change_presence(activity = game)
    return

@client.event
async def on_message(message):
    try :
        if message.author == client.user :
            return
        print(message.author)
        print(message.content)
        if message.author.id == 624596508070772750 and message.content.lower().__contains__('yes') :
            await message.channel.send("GOOD! Always stay happy <3! ilysmm sissy <3 ~ Adi")
        if message.author.id == 624596508070772750 and message.content.lower().__contains__('no') :
            adi = client.get_user(568446269610000385)
            if adi.dm_channel == None :
                await adi.create_dm()
            await adi.dm_channel.send('Adi!!! Nigh sis is not happy!!! Do somethinggg')
    except Exception as err :
        print('Some error occured in the message checker function', Exception, err)
        traceback.print_exc()
    return


client.run(os.environ['BOT_TOKEN'])
