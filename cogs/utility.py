import discord
from discord.ext import commands
import random
import time

class Utility(commands.Cog):
    @commands.command(name = 'eval')
    async def evaluate(self, ctx, *, content):
        await ctx.reply(embed = discord.Embed(
            title = 'Evaluation',
            description = discord.utils.escape_markdown(str(eval(content, {
                'ctx': ctx,
                'discord': discord,
                'choose': random.choice,
                'random': random.randint,
                'timestamp': __import__('time').time,
                'shuffle': lambda x: random.sample(x, len(x))
            }, {i: None for i in (
                '__import__',
                'copyright',
                'credits',
                'license',
                'print',
                'input',
                'eval',
                'exec',
                'help',
                'exit',
                'quit',
                'open'
            )}))),
            color = 0xffe5ce
        ).set_footer(
            text = ctx.author.display_name,
            icon_url = ctx.author.display_avatar.url
        ))
    
    @commands.command()
    async def embed(self, ctx, title, *, description):
        embed = discord.Embed(
            title = title,
            description = description,
            color = 0xffe5ce
        )
        if ctx.message.attachments != []:
            embed.set_image(url = ctx.message.attachments[0].url)
        await ctx.send(embed = embed)

async def setup(bot):
    await bot.add_cog(Utility())