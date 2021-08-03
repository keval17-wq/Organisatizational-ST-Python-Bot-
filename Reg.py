import discord
from discord.ext import commands, tasks
import random

token="ODY3NDM5MjY5MjQ0MTc0MzY2.YPhHxg.UMwy_3YGQsgtYnuC7Kx66Bv09DI"

client= commands.Bot(command_prefix='!')
try:
    @client.command()
    async def hello(ctx):
        await ctx.send('Hello to you !')

    @client.command()
    #@commands.has_permissions(ban_members=True)
    async def ban(ctx,member: discord.Member,*,reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been banned.')

    @client.command()
    #@commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None):
            await member.kick(reason=reason)
            await ctx.send(f'User {member} has been kicked.')

    @client.command(aliases=['askme','ques'])# Wherever there is command written, it is meant perform something when told so
    async def ask(ctx,*,question):
        
        l1=['R1','R2','R3','R4','R5']
        choose=random.randint(0,len(l1))
        
        await ctx.send(l1[choose])
    @client.event# in case events, it chooses to wait until the expected task happens. like on_ready 
    async def on_ready():
        print('We have logged in as {0.user}'.format(client)) 

    client.run(token)
except Exception as e:
    print(e)    