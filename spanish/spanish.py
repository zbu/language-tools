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
    async def spanish(self, word):
        """Translates from English to Spanish"""

        #Your code will go here
        url = "https://www.wordreference.com/es/translation.asp?tranword=" + word #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            text = soupObject.find(class_='ToWrd').get_text()
            text2 = text.split(' ')[0]
            await self.bot.say(text2)
        except:
            await self.bot.say("Word not indexed.")

def setup(bot):
    bot.add_cog(lingtools(bot))