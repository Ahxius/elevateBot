from discord.ext import commands
import discord


class links(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='youtube', hidden=True, aliases=['yt'])
    async def youtube(self, context):
        embed = discord.Embed(title='Our YouTube', description="[www.youtube.com/channel/"
                                                               "UC1yKPtZ7HOzThgAGFfJd4dg](https://www.youtube.com/"
                                                               "channel/UC1yKPtZ7HOzThgAGFfJd4dg)")
        await context.send(embed=embed)

    @commands.command(name='instagram', hidden=True, aliases=['ig', 'insta'])
    async def instagram(self, context):
        embed = discord.Embed(title='Our Instagram', description="[www.instagram.com/elevatewc]"
                                                                 "(https://www.instagram.com/elevatewc)")
        await context.send(embed=embed)

    @commands.command(name='email', hidden=True)
    async def email(self, context):
        embed = discord.Embed(title='Our Email:', description="elevate@willowcreek.org")
        await context.send(embed=embed)


def setup(client):
    client.add_cog(links(client))
