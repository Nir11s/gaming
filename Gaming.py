import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random 
import os

print ("hi bro")

prefix = "gaming "
status = "OFF"
Client = discord.Client()
client = commands.Bot(command_prefix = "gaming ")

@client.event
async def on_ready():
    print("Bot is online!")
    await client.change_presence(game=discord.Game(name="server: https://discord.gg/fZ3FcFP".format(len(client.servers))))

@client.event
async def on_message(message):
    global prefix
    global status
    if message.author.bot:
        return
    if not message.content.lower().startswith(prefix):
        return
    command = message.content.lower()[len(prefix)::]
    userID = message.author.id

    if (command == "help") or (command == ""):
        embed=discord.Embed(title="**__Gaming (server):__**", color=0xff545c)
        embed.add_field(name="**prefix:** " + prefix , value="This Bot is for a discord server\n \n **Help** - this help message\n **Partner** - only the bot developer can do this command", inline=False)
        embed.set_footer(text="Creator: Nir11s")
        embed.add_field(name="**▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬**", value="Gaming server: [Click me](https://discord.gg/fZ3FcFP)")

        await client.send_message(message.channel, embed=embed)
    #commands:
    
    if command == "status":
         await client.send_message(message.channel, "Command status is: ``"+status+"``")
    if command == "partner":
        if status == "ON":
            await client.send_message(message.channel, "<@%s> This command is already ``ON``" % (userID))
            return
        else:
            if userID == "279531199611928577":
                await client.send_message(message.channel, ":white_check_mark: I will send this message every 24h :smile:")
                await client.delete_message(message)
                while True:
                    embed=discord.Embed(title="**__Gaming (server):__**", color=0xff545c)
                    embed.add_field(name="**היי!** " , value="**אני מעוניין להזמין אתכם לשרת גיימינג** \n **מעוצב במיוחד לגיימרים!** \n ``יש קבלה לצוות השרת!``\n \n » סדר רולים מעוצב בצורת פרופיל של גיימר\n » טאגים לכולם\n » הגרלות\n » בוטים מצחיק\n » פקודות מסודרות\n » מוזיקה\n » כלאנים\n » תחרויות בין הכלאנים\n » אומנות\n ועוד!\n \n**את הראנקים אפשר להשיג לבד** \n **נשמח מאוד אם תצטרפו לקהילה**", inline=False)
                    embed.set_footer(text="Creator: Nir11s")
                    embed.add_field(name="**▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬**", value="Gaming server: [Click me](https://discord.gg/fZ3FcFP)")
                    await client.send_message(message.channel, embed=embed)
                    await client.send_message(message.channel, "**__Link:__**\n https://discord.gg/fZ3FcFP")
                    status = "ON"
                    time.sleep(86400)
                    return status
            else:
                await client.send_message(message.channel, "<@%s> You do not have the premmision" % (userID))
                return
                                
    if(command == "servers"):
       await client.send_message(message.channel, "I'm in ``{}`` servers!".format(len(client.servers)))

client.run(os.getenv("TOKEN"))
