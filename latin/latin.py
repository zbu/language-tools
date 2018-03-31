import discord
from discord.ext import commands
try: # check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False
import aiohttp

class lingtools:
    """Ling Tools"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="latin", pass_context=True)
    async def _latin(self, ctx):
        """Translates from English to Latin"""
        
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
    @_latin.command()
    async def normal(self, word):
        #Your code will go here
        url = "http://archives.nd.edu/cgi-bin/wordz.pl?english=" + word #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            text = soupObject.find('pre').get_text()
            text2 = text.split(',')[0]
            await self.bot.say(text2)
        except:
            await self.bot.say("Word doesn't exist.")
    @_latin.command()
    async def reverse(self, word):
        #Your code will go here
        url = "http://http://archives.nd.edu/cgi-bin/wordz.pl?keyword=" + word #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            text = soupObject.find('pre').get_text()
            text2 = text.split(']')[1]
            text3 = text2.split(',')[0]
            await self.bot.say(text3)
        except:
            await self.bot.say("Word doesn't exist.")
def setup(bot):
    bot.add_cog(lingtools(bot))