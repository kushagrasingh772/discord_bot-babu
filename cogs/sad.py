import discord
from discord.ext import commands
import random
from random import randint

pp_size=["=>","==>","===>","=====>","=======>"]

client=commands.Bot(command_prefix='.')
class Sad(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command(help="Virtual boobies for sed boy")
    async def sad(self,ctx):
        await ctx.send("boobies for you sadboi (.)(.) \n be happy now XD")
    @commands.command(help="Your pp size")
    async def pp(self,ctx):
        pp_select=random.choice(pp_size)
        await ctx.send(f"Your size \n {pp_select}")
def setup(client):
    client.add_cog(Sad(client)) 