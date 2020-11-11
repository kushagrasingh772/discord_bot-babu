import discord
from discord.ext import commands
import random
from random import randint
import praw

reddit = praw.Reddit(client_id="yOUR CLIENT ID",
client_secret="Your client secret",
username="Your-username",
password="password",
user_agent="useragent")


client=commands.Bot(command_prefix='.')
class Meme(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command(help='Meme dekh lo kisi bhi category ka',aliases=['m','maymay'])
    async def meme(self,ctx,subred="memes"):
        subreddit=reddit.subreddit(subred)
        all_subs=[]
        top=subreddit.top(limit= 50)
        for submission in top:
            all_subs.append(submission)

        random_sub= random.choice(all_subs)

        name=random_sub.title
        url =random_sub.url

        em=discord.Embed(title=name)

        em.set_image(url=url)

        await ctx.send(embed=em)

def setup(client):
    client.add_cog(Meme(client))