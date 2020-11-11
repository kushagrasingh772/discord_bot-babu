import discord
from discord.ext import commands
import random

client=commands.Bot(command_prefix='.')

class _8ball(commands.Cog):
    
    def __init__(self,client):
        self.client=client

    @commands.command(aliases=['8ball'],help='Ask any question to Babu')
    async def _8ball(self,ctx,*,question):
        responses=['Probably','I would not be so sure about that.','My answer is no.','Probably not','Of course!','Why not?','My answer is yes.','This is true, and it will stay like that.','Not even in a million years.','I mean, I do not see the point in saying no.','Why this question? The answer is a definitive no.','Yes please','I do not know.','Sources say no.','True that.','Dont ask me this.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(client):
    client.add_cog(_8ball(client))