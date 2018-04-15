import discord
from discord.ext import commands

defined = {'the': 'autrev', 'me': 'till', 'hello': 'auztlav', 'goodbye': 'nurvænt', 'and': 'vvil', 'i': 'ñuvely', 'we': 'ñuveli', 'you': 'ñuvemn', 'you (plural)': 'ñuvenm', 'you (pl)': 'ñuvenm', 'he': 'ñuvert', 'she': 'ñuvert', 'it': 'ñuvert', 'they': 'ñuvetr', 'everyone': 'ñuve', 'there': 'žoreal', 'their': 'žoremv', "they're": 'ñuvetržo', 'home': 'heiyuma', 'language': 'lindua', 'good': 'ǵqius', 'bad': 'byutzzi', 'happy': 'ǵquzo', 'sad': 'byuzo', 'excited': 'ǵquli', 'ecstatic': 'ǵquli', 'angry': 'byuli', 'homosexual': 'yzzer', 'gay': 'yzzer', 'heterosexual': 'zzasd', 'straight': 'zzasd'}

class lingtools:
    """Ling Tools"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hilindua(self, word):
        """Translates from English to Hilindua"""

        #Your code will go here
        try:
            await self.bot.say(defined[word.lower()])
        except:
            await self.bot.say("Word not indexed.")

def setup(bot):
    bot.add_cog(lingtools(bot))