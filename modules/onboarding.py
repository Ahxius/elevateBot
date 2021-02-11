from discord.ext import commands
import discord


class onboarding(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = self.client.get_guild(809193352925806653)
        category = guild.get_channel(809551833864732702)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            member: discord.PermissionOverwrite(read_messages=True)
        }
        channel = await guild.create_text_channel(member.id, overwrites=overwrites, category=category)
        embed = discord.Embed(title='Welcome to Elevate!', description="We're so glad to see you. Before you can enter "
                                                                       "the server, we have some housekeeping to do. "
                                                                       "First, click on the Google form below and "
                                                                       "fill it out with your parent or guardian.")
        embed.add_field(name="Google Form", value="foo", inline=True)
        embed.set_footer(text="Elevate 2021, Willow Creek Church's Junior High Ministry")
        await channel.send(embed=embed)
        sent_message = await channel.send(f"React below when you've submitted the Form!")
        await sent_message.add_reaction("\U00002705")

        def check(reaction, user):
            if reaction.message.id != sent_message.id or reaction.emoji != "✅" or user.id != member.id:
                return False
            return True

        await self.client.wait_for('reaction_add', check=check)
        await sent_message.delete()
        await channel.send('Awesome! Someone with the <@&809193466412269627> role will soon help you.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        server = self.client.get_guild(809193352925806653)
        channels = await server.fetch_channels()
        for channel in channels:
            if channel.name == str(member.id):
                channel_object = server.get_channel(channel.id)
                await channel_object.delete()
        return


def setup(client):
    client.add_cog(onboarding(client))
