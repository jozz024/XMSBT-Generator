import nextcord
from nextcord import File
from nextcord.ext import commands
from nextcord.ext.commands import Cog, Context
import generate

class XMSBTGen(Cog):
    @commands.command(name= "xmsbt")
    async def convert_to_xmsbt(self, ctx: Context):
        og_msbt = generate.load_og_msbt(ctx.message.attachments[0].filename)
        print(og_msbt)
        with open("./" + ctx.message.attachments[0].filename, "wb") as file:
            file.write(await ctx.message.attachments[0].read())

        generate.modded_msbt_diff("./" + ctx.message.attachments[0].filename, og_msbt)
        await ctx.send(file=File("./" + ctx.message.attachments[0].filename.rstrip(".msbt") + ".xmsbt"))

def setup(bot):
    bot.add_cog(XMSBTGen(bot))