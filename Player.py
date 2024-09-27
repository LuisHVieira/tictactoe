from discord.ext import commands

class Player (commands.Converter):
    async def convert(self, ctx, argument):
        p1 = ctx.author.name

        p2 = ctx.message.raw_mentions
    

        return p1, p2
