import discord
import requests
import json
client=discord.Client()

'''

Add a out command and then end the process and do the end part of adding the data to the main game 

'''
def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + '\t- ' + json_data[0]['a']
    return quote
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) 

@client.event
async def on_message(message):
    if (message.author == client.user):
        return
    if message.content.startswith('$inspire'):
        quote=get_quote()
        await message.channel.send(quote)    
    if message.content.startswith('$hello'):

        await message.channel.send('I am up and running, oh hey there.')
    
    if message.content.startswith('IN'):
        obj=users()
    if message.content.startswith('BYE' or 'bye'):
        await message.channel.send('see ya !')    
    if message.content.startswith('tell me a joke'):
        await message.channel.send('Teeth one: Do you like my jokes ? \n teeth two: yes but they are cracking me up.')    
client.run('ODMxODY0MjI1MjczNzQxMzU0.YHbb7g.hB1Vaw8Tyy3IiSwaV6Zw2zlgFE8')        

                                # Dynamic user creation
database=[]

class users():
    def __init__(self,user_name):
        self.name=user_name
        self.counter=1