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
        url = "http://www.spanishdict.com/translate/" + word #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            text = soupObject.find(class_='lang').get_text()
            await self.bot.say(text)
        except:
            await self.bot.say("Word not indexed.")

def setup(bot):
    bot.add_cog(lingtools(bot))