import discord
from discord.ext import commands
from congress import Congress



TOKEN = "NzUzMTI0OTg0NDk4NTUyODg0.X1hoTA.sPwcofaclgYczyT2n2l3dqW_Yik"




bot = commands.Bot(command_prefix='>')  

@bot.event
async def on_ready():
        print(f"Bot is up & ready")


bot.add_cog(Congress(bot))
bot.run(TOKEN)






