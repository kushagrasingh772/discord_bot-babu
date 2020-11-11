import discord
from discord.ext import commands


client=commands.Bot(command_prefix='.')
class Example(commands.Cog):

    def __init__(self,client):
        self.client=client
    
    @commands.command()
    async def cogs(self,ctx):
        print("Cogs connected.")
        await ctx.send('Cogs working fine!')

def setup(client):
    client.add_cog(Example(client))