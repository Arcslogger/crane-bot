import discord
import json
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

with open('run.json') as f:
  token = json.load(f)

@client.event
async def on_ready():
    print('Hello world!')
    
@client.command(aliases=['latency', 'ping'])
async def check(ctx):
    embed = discord.Embed(title='Pong!', colour=discord.Colour.blue())    
    embed.add_field(name=f'⌛', value=f'{round(client.latency * 1000)}ms')
    await ctx.send(embed=embed)

@client.command(aliases=['carry deck crane'])
async def carry(ctx):
    embed = discord.Embed(title='Carry Deck Crane!', colour=discord.Colour.blue())    
    embed.set_image(url='https://cdn.discordapp.com/attachments/708483689780346974/761001550076182538/construction-carry-deck-crane.png')
    await ctx.send(embed=embed)

@client.command(aliases=['floating crane'])
async def floating(ctx):
    embed = discord.Embed(title='Floating Crane!', colour=discord.Colour.blue())    
    embed.set_image(url='https://cdn.discordapp.com/attachments/708483689780346974/761001599001952266/construction-floating-crane.png')
    await ctx.send(embed=embed)

@client.command(aliases=['rough terrain crane'])
async def rough(ctx):
    embed = discord.Embed(title='Rough Terrain Crane!', colour=discord.Colour.blue())    
    embed.set_image(url='https://cdn.discordapp.com/attachments/708483689780346974/761001621463236648/construction-rough-terrain-crane.png')
    await ctx.send(embed=embed)

@client.command(aliases=['truck crane'])
async def truck(ctx):
    embed = discord.Embed(title='Truck-Mounted Crane!', colour=discord.Colour.blue())    
    embed.set_image(url='https://cdn.discordapp.com/attachments/708483689780346974/761001636436508682/construction-truck-mounted-crane.png')
    await ctx.send(embed=embed)


client.run(token['token']) 