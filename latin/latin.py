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

    @commands.command()
    async def latin(self, word):
        """Translates from English to Latin"""

        #Your code will go here
        url = "http://archives.nd.edu/cgi-bin/wordz.pl?english=" + word #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            text = soupObject.find('pre').get_text()
            text2 = text.split(' ')[0]
            if ',' in text2:
                text2 = text.split(',')[0]
            else:
                await self.bot.say(text2)
        except:
            await self.bot.say("Word doesn't exist.")

def setup(bot):
bot.add_cog(lingtools(bot))