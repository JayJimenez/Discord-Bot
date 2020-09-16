import discord
from discord.ext import commands



sessionNumber = 1
totalYays = 0
totalNays = 0
author = None



class Congress(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    #Helper Functions-----------------------------------------------------------------------------------
    def init_congress(self):
        return
     
    #Commands-------------------------------------------------------------------------------------------
    @commands.command(name = "present-bill")
    async def present_bill(self,ctx, arg: commands.clean_content(use_nicknames=True, escape_markdown=True), arg2: commands.clean_content(use_nicknames=True, escape_markdown=True)):
        global author
        global totalNays
        global totalYays
        totalYays = 0
        totalNays = 0
        author = ctx.author
        embedVar = discord.Embed(title=f"Congress Session #{sessionNumber}", description = f"Our session will begin shortly. {ctx.author} has presented the following bill to the floor to be voted upon : ", color=0x00ff40)
        embedVar.set_thumbnail(url="https://lawrjb.com/wp-content/uploads/2019/12/2060-Law-Book.png")
        embedVar.add_field(name=f"{arg}", value=f"{arg2}", inline = False)

        await ctx.send(embed=embedVar)

    @commands.command(name="vote")
    async def voting(self,ctx, arg):

        if arg.lower() == 'y':
            global totalYays
            totalYays += 1  
            await ctx.message.delete()
            await ctx.send(f"{ctx.author}\'s vote has been tallied")
            
        elif arg.lower() == 'n':
            global totalNays
            totalNays += 1
            await ctx.message.delete()
            await ctx.send(f"{ctx.author}\'s vote has been tallied")
            
        elif arg.lower() == 'np':
            pass
        else:
            await ctx.send("Invalid Vote - Please insert Y for Yes, N for No.", delete_after=5)
                  
    @commands.command(name="tally")
    async def tally(self, ctx):
        embedVar = discord.Embed(title=f"Congress Session #{sessionNumber}", description = f"Total Votes for {author}\'s bill' :", color=0x00ff40)
        embedVar.add_field(name=f"Yays : {totalYays}", value=f"Nays : {totalNays}", inline = True)
        await ctx.send(embed=embedVar, delete_after=30)

    @commands.command(name="clear-tally")
    async def clear_tally(self, ctx):
        global totalNays
        global totalYays
        totalYays = 0
        totalNays = 0
        await ctx.send("Cleared tally", delete_after=2)
    
    #Error Handling-------------------------------------------------------------------------------------
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.CommandNotFound):
            embedVar = discord.Embed(title=f"Error : Command Not Found", description = f"This is an invalid command", color=0xff0000)
            embedVar.set_thumbnail(url="https://p1.hiclipart.com/preview/238/944/29/human-o2-grunge-dialog-error-icon-png-icon.jpg")

            await ctx.send(embed=embedVar, delete_after=30)
        
        
        if  isinstance(error, commands.MissingRequiredArgument):

            if ctx.command.qualified_name == "vote":
                embedVar = discord.Embed(title=f"Error : Argument(s) Missing", description = f"Please enter a valid argument with this command- either Y or N.", color=0xff0000)
                embedVar.set_thumbnail(url="https://p1.hiclipart.com/preview/238/944/29/human-o2-grunge-dialog-error-icon-png-icon.jpg")
                embedVar.add_field(name=f"Example Usage", value=f">vote Y", inline = False)
                await ctx.send(embed=embedVar, delete_after=30)

            elif ctx.command.qualified_name == "present-bill":
                embedVar = discord.Embed(title=f"Error : Argument(s) Missing", description = f"Please provide the two descriptors required for this command.", color=0xff0000)
                embedVar.set_thumbnail(url="https://p1.hiclipart.com/preview/238/944/29/human-o2-grunge-dialog-error-icon-png-icon.jpg")
                embedVar.add_field(name=f"Example Usage", value=f">present_bill \"This is the Bill Name\" \"This is the description of the bill\"", inline = False)
                await ctx.send(embed=embedVar, delete_after=30)

            else:
                pass



            




    
        


