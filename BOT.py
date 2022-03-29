import discord
from discord.ext import commands, tasks
import random
import requests
import json
import praw
from PIL import Image

token="ODY3NDM5MjY5MjQ0MTc0MzY2.YPhHxg.i36LPDQJGXTWXDmZNyVhnw1WseA"
client_id='tGSwoGuBtGVHjlmY6er2mg'
secret_key='DUFLTAyrS7Tfi_BHn4ZlcREdlI1XsA'

client= commands.Bot(command_prefix='!')
try:
    @client.command()
    async def hello(ctx):
        await ctx.send('Hello to you !')
    @client.command()
    async def inspire(ctx):
        response = requests.get('https://zenquotes.io/api/random').json()
        await ctx.send(response[0]['q']+'-'+response[0]['a'])
        
    @client.command()
    async def meme(ctx):
        response = requests.get('https://meme-api.herokuapp.com/gimme').json()
        embed=discord.Embed(color=discord.Colour.random())
        embed.set_image(url=response['url'])
        
        await ctx.send(f'{response["title"]}\n',embed=embed)
    @client.command()
    async def ud(ctx,*,search):
        data = requests.get(f'https://api.urbandictionary.com/v0/define?term={search}').json()        
        print(data["list"][0]["definition"])
        main=data["list"][0]["definition"]
        main=main.replace("[","")
        main=main.replace("]","")

        embed =discord.Embed(color=0x2bc7ff,title=f'{search}',description=f'{main.capitalize()}')

        await ctx.send(embed=embed)


    @client.command()
    async def trivia(ctx):
        '''
            Type     
            Question 

        '''    
        data = requests.get(f'https://opentdb.com/api.php?amount=10&type=boolean').json()        
        print(data["results"][0]["question"])
        main=data["results"][0]["question"]
        def check(m):
            return m.author.id==ctx.author.id

        embed =discord.Embed(color=0x2bc7ff,title=f'{data["results"][0]["category"]}',description=f'{data["results"][0]["question"]}')
        await ctx.send(embed=embed)
        answer=await client.wait_for('message',check=data["results"][0]["correct_answer"])
        print(answer)
        print(data["results"][0]["correct_answer"])
        if(answer==data["results"][0]["correct_answer"]):
            await ctx.send("correct answer.")
        else:
            await ctx.send("Incorrect answer.")

    @client.command()
    async def userinfo(ctx,member: discord.Member=None):
        member= ctx.author if not member else member
        embed =discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

        embed.set_author(name=f"User Info: -{member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)

        embed.add_field(name="Username:",value=member.display_name)
        embed.add_field(name="Created at:",value=member.created_at.strftime("%a,%d %B %Y,%I:%M %p UTC"))
        embed.add_field(name="Joined at:",value=member.joined_at.strftime("%a,%d %B %Y,%I:%M %p UTC"))

        embed.add_field(name="ID",value=member.id)
        embed.add_field(name="BOT?",value=member.bot)

        await ctx.send(embed=embed)  

    @client.command()    
    async def manual(ctx):
        embed =discord.Embed(colour=10070709, timestamp=ctx.message.created_at)

        embed.set_footer(text=f"DM the @CMYIC#5575 for assistance")

        embed.add_field(name="!Userinfo:",value="get the entire userinfo")
        embed.add_field(name=f"$inspire:",value="inspire yourself by sayings from the best authors")
        embed.add_field(name=f"!meme:",value="Call it to have some fun")
        
        embed.add_field(name=f"!kick:",value="Kick a user off the server")
        embed.add_field(name=f"!ban",value="Ban a user from the server")
        embed.add_field(name=f"!ask:",value="Ask a question to the Bot")

        embed.add_field(name=f"!help:",value="To get a list of all the commands")
        
        await ctx.send(embed=embed)

    @client.command()
    #@commands.has_permissions(ban_members=True)
    async def ban(ctx,member: discord.Member,*,reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'```User {member} has been banned.```')

    @client.command()
    #@commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None):
            await member.kick(reason=reason)
            await ctx.send(f'```User {member} has been kicked.```')

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
    print(e)    import discord
from discord.ext import commands, tasks
import random
import requests
import json
import praw
from PIL import Image

token="ODY3NDM5MjY5MjQ0MTc0MzY2.YPhHxg.i36LPDQJGXTWXDmZNyVhnw1WseA"
client_id='tGSwoGuBtGVHjlmY6er2mg'
secret_key='DUFLTAyrS7Tfi_BHn4ZlcREdlI1XsA'

client= commands.Bot(command_prefix='!')
try:
    @client.command()
    async def hello(ctx):
        await ctx.send('Hello to you !')
    @client.command()
    async def inspire(ctx):
        response = requests.get('https://zenquotes.io/api/random').json()
        await ctx.send(response[0]['q']+'-'+response[0]['a'])
        
    @client.command()
    async def meme(ctx):
        response = requests.get('https://meme-api.herokuapp.com/gimme').json()
        embed=discord.Embed(color=discord.Colour.random())
        embed.set_image(url=response['url'])
        
        await ctx.send(f'{response["title"]}\n',embed=embed)
    @client.command()
    async def ud(ctx,*,search):
        data = requests.get(f'https://api.urbandictionary.com/v0/define?term={search}').json()        
        print(data["list"][0]["definition"])
        main=data["list"][0]["definition"]
        main=main.replace("[","")
        main=main.replace("]","")

        embed =discord.Embed(color=0x2bc7ff,title=f'{search}',description=f'{main.capitalize()}')

        await ctx.send(embed=embed)


    @client.command()
    async def trivia(ctx):
        '''
            Type     
            Question 

        '''    
        data = requests.get(f'https://opentdb.com/api.php?amount=10&type=boolean').json()        
        print(data["results"][0]["question"])
        main=data["results"][0]["question"]
        def check(m):
            return m.author.id==ctx.author.id

        embed =discord.Embed(color=0x2bc7ff,title=f'{data["results"][0]["category"]}',description=f'{data["results"][0]["question"]}')
        await ctx.send(embed=embed)
        answer=await client.wait_for('message',check=data["results"][0]["correct_answer"])
        print(answer)
        print(data["results"][0]["correct_answer"])
        if(answer==data["results"][0]["correct_answer"]):
            await ctx.send("correct answer.")
        else:
            await ctx.send("Incorrect answer.")

    @client.command()
    async def userinfo(ctx,member: discord.Member=None):
        member= ctx.author if not member else member
        embed =discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

        embed.set_author(name=f"User Info: -{member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)

        embed.add_field(name="Username:",value=member.display_name)
        embed.add_field(name="Created at:",value=member.created_at.strftime("%a,%d %B %Y,%I:%M %p UTC"))
        embed.add_field(name="Joined at:",value=member.joined_at.strftime("%a,%d %B %Y,%I:%M %p UTC"))

        embed.add_field(name="ID",value=member.id)
        embed.add_field(name="BOT?",value=member.bot)

        await ctx.send(embed=embed)  

    @client.command()    
    async def manual(ctx):
        embed =discord.Embed(colour=10070709, timestamp=ctx.message.created_at)

        embed.set_footer(text=f"DM the @CMYIC#5575 for assistance")

        embed.add_field(name="!Userinfo:",value="get the entire userinfo")
        embed.add_field(name=f"$inspire:",value="inspire yourself by sayings from the best authors")
        embed.add_field(name=f"!meme:",value="Call it to have some fun")
        
        embed.add_field(name=f"!kick:",value="Kick a user off the server")
        embed.add_field(name=f"!ban",value="Ban a user from the server")
        embed.add_field(name=f"!ask:",value="Ask a question to the Bot")

        embed.add_field(name=f"!help:",value="To get a list of all the commands")
        
        await ctx.send(embed=embed)

    @client.command()
    #@commands.has_permissions(ban_members=True)
    async def ban(ctx,member: discord.Member,*,reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'```User {member} has been banned.```')

    @client.command()
    #@commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None):
            await member.kick(reason=reason)
            await ctx.send(f'```User {member} has been kicked.```')

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
