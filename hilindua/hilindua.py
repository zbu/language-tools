import discord
from discord.ext import commands

defined = {'the': 'Autrev', 'me': 'Till', 'hello': 'Auztlav', 'goodbye': 'Nurvænt', 'and': 'Vvil', 'i': 'Ñuvely', 'we': 'Ñuveli', 'you': 'Ñuvemn', 'you (plural)': 'Ñuvenm', 'you (pl)': 'Ñuvenm', 'he': 'Ñuvert', 'she': 'Ñuvert', 'it': 'Ñuvert', 'they': 'Ñuvetr', 'everyone': 'Ñuve', 'there': 'Žoreal', 'their': 'Žoremv', "they're": 'Ñuvetržo', 'home': 'heiyuma', 'language': 'lindua'}

class lingtools:
    """Ling Tools"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hilindua(self, word):
        """Translates from English to Hilindua"""

        #Your code will go here
        try:
            await self.bot.say(defined[word])
        except:
            await self.bot.say("Word not indexed.")

def setup(bot):
    bot.add_cog(lingtools(bot))