import discord
from discord.ext import commands
from congress import Congress
from token import token


TOKEN = "token"

bot = commands.Bot(command_prefix='>')  

@bot.event
async def on_ready():
        print(f"Bot is up & ready")


bot.add_cog(Congress(bot))
bot.run(TOKEN)






