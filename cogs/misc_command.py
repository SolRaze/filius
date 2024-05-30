
# Imports

from discord.ext import commands


#

class misc_command(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='repeat', aliases=['r', 'rep'])

  async def repeat_command(self, ctx, *, arg):
    await ctx.send(arg)
  

    
    
def setup(bot):
  bot.add_cog(misc_command(bot))
