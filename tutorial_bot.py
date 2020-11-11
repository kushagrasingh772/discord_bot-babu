from __future__ import unicode_literals
import discord
import os
from discord.ext import commands,tasks
import time
import random
from itertools import cycle
import json
import youtube_dl
from random import choice
import asyncio
from discord.utils import get
import shutil
from os import system
from discord import FFmpegPCMAudio
import praw
import asyncio
import speech_recognition as sr
import pyttsx3


# pylint: disable=E1101
client= commands.Bot(command_prefix=".")
status= cycle(['Fucking',f"on {len(client.guilds)} servers",'Sleeping','With your heart','PoonamPandeyvideos'])
#On_Ready
@client.event
async def on_ready():
    print("Babu is ready!")
    print('Logged in as {0} ({0.id})'.format(client.user))
    print('------')
    change_status.start()


@client.command(help='To load a cog')
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@client.command(help='To unload a cog')
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


#Error
@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("Command not found!")
    elif isinstance(error,commands.MissingPermissions):
        await ctx.send("You do not have the permission to do so!")
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Please enter all the arguments")
        await ctx.message.delete()


#Member_Join
@client.event
async def on_member_join(ctx,member):
    await ctx.send(f'{member} has joined the server!')

#Mute
@client.command(help='Mute someone who has been naughty lil fellow')
@commands.has_permissions(kick_members=True)
async def mute(ctx, member:discord.Member):
    guild=ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            await ctx.send("{} has {} has been muted".format(member.mention,ctx.author.mention))
            return 

            overwrite =discord.PermissionOverwrite(send_messages=False)
            newRole= await guild.create_role(name="Muted")

            for channel in guild.text_channels:
                await channel.set_permissions(newRole,overwrite=overwrite)

            await member.add_roles(newRole)
            await ctx.send("{} has {} has been muted".format(member.mention,ctx.author.mention))


#Unmute
@client.command(help='Unmute someone who has been muted')
async def unmute(ctx, member:discord.Member):
    guild=ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send("{} has {} has been unmuted".format(member.mention,ctx.author.mention))
            return 


#Member_Remove
@client.event
async def on_member_remove(ctx,member):
    await ctx.send(f'{member} has left the server!')

    
#Delete_message
@client.command(help="To clear messages")
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)
    await  ctx.send(f'Deleted {amount} messages!!')

#Kick
@client.command(help="Kick a member, also give a reason if you wanna kick ")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member,*,reason="No reason provided"):
    await member.send(f"You have been kicked from {ctx.guild} ,because: "+reason)
    await member.kick(reason=reason)

#Ban
@client.command(help="Ban a member, give a reason too")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member,*,reason="No reason provided"):
    await ctx.send(member.name+f"You have been banned from {ctx.guild} ,because: "+reason)
    await member.ban(reason=reason)

#Unban
@client.command(help="To unban a member")
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator=member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.users
        if (user.name,user.discriminator)==(member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return


#Who_Is_Function
@client.command(help="Revealing one's info",aliases=['users','info'])
async def whois(ctx, member: discord.Member):
    embed= discord.Embed(title=member.name,description=member.mention,color=discord.Colour.green())
    embed.add_field(name="ID",value=member.id,inline=True)
    embed.set_thumbnail(url= member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name} ")
    await ctx.send(embed=embed)

#Credits
@client.command(help='Display the name of developer of the bot')
async def credits(ctx):
    await ctx.send('Hindu launda Perkymaster!!!!!')
    
#Looping_Activity
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status =discord.Status.idle,activity=discord.Game(next(status)))
 
#Say
@client.command(help="Make Babu say anything you want")
async def say(ctx,*,msg):
    await ctx.message.delete()
    await ctx.send("{}".format(msg))

client.run('YOUR TOKEN')
