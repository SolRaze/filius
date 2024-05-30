
# Imports

import discord
from discord.ext import commands
import random

class minigame(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  player1 = ""
  player2 = ""
  turn = ""
  gameover = True

  board = []


  @commands.group(name = 'chess', aliases=['c'], invoke_without_command = True)
  async def chess(self, ctx):
  
    await ctx.send("To challange a player type /chess challange @USERNAME")


  

  @checks.has_started()
  @commands.guild_only()
  @commands.max_concurrency(1, commands.BucketType.user)
  @chess.command(name = 'challange')
  async def reactionduel(self, ctx, user: discord.User, amount=10):
      if amount < 0:
          return await ctx.send("Nice Try")

      if user == ctx.author:
          return await ctx.send("You can not play yourself.")





  @chess.command(name = "a")
  async def a(self, ctx, *, p1 : discord.Member, p2 : discord.Member):
    global player1
    global player2
    global turn
    global gameover

    if gameover:
      global board
      board = [
        [":wbR:", ":bbN:", ":wbB:", ":bbQ:", ":wbK:", ":bbB:", ":wbN:", ":bbR:"],
        [":bbP:", ":wbP:", ":bbP:", ":wbP:", ":bbP:", ":wbP:", ":bbP:", ":wbP:"],
        [":wS:", ":bS:", ":wS:", ":bS:", ":wS:", ":bS:", ":wS:", ":bS:"],
        [":bS:", ":wS:", ":bS:", ":wS:", ":bS:", ":wS:", ":bS:", ":wS:"],
        [":wS:", ":bS:", ":wS:", ":bS:", ":wS:", ":bS:", ":wS:", ":bS:"],
        [":bS:", ":wS:", ":bS:", ":wS:", ":bS:", ":wS:", ":bS:", ":wS:"],
        [ ":wwP:", ":bwP:", ":wwP:", ":bwP:", ":wwP:", ":bwP:", ":wwP:", ":bwP:"],
        [":bwR:", ":wwN:", ":bwB:", ":wwQ:", ":bwK:", ":wwB:", ":bwN:", ":wwR:"],
      ]
      turn = ""
      gameover = False

      player1 = p1
      player2 = p2

      # Print the board

      await ctx.send(board)

      # Determine who goes first
      num = random.randint(1, 2)
      if num == 1:
        turn = player1
        await ctx.send("It is <@" + str(player1.id) + "> turn.")
      elif num == 2:
        turn = player2
        await ctx.send("It is <@" + str(player2.id) + "> turn.")

    else:
      await ctx.send("A game is alredy in progress")

  

    
def setup(bot):
  bot.add_cog(minigame(bot))
