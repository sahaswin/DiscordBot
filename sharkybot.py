import discord
from discord.ext import commands
from discord.utils import get
import os

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def ado(ctx):
    await ctx.send('Ay yako? \nOkkoma commands one nan **.udaw** kiyala gahapan')

@client.command()
async def pingeka(ctx):
    await ctx.send(f'Ping eka {round(client.latency * 1000)}ms bn')

@client.command()
async def makapan(ctx , amount = 5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'messages {amount}k makuwa')

@client.command()
async def udaw(ctx):
    embed = discord.Embed(
        title= "Okkoma commands tika",
        description= "bot negger ge commands tika xD\n",
        colour= discord.Colour.blue()
    )

    embed.set_footer(text="Marenna baya nathi ayage bota")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/696760865810022430/735999274583588874/profile-lillia.249a49.png')
    embed.set_author(name="SharkyBot")
    embed.set_image(url="https://cdn.discordapp.com/attachments/696760865810022430/735999274583588874/profile-lillia.249a49.png")

    embed.add_field(name="ado", value="karala balapan", inline=False)
    embed.add_field(name="pingeka", value="ping eka check karanna", inline=True)
    embed.add_field(name="makapan", value="messages delete karanna\n(example --> makapan 10)", inline=True)

    await ctx.send(embed=embed)






client.run(os.environ['token'])