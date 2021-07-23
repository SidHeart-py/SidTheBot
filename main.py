import discord
import os
import requests
from jokeapi import Jokes  # Import the Jokes class
from server import keep_alive
import asyncio
from random import choice

my_discord_key = os.environ['DiscordKey']
my_tenorAPI_key = os.environ['tenorAPIkey']


client = discord.Client()


def get_gif_url(theme):
    url = f"https://g.tenor.com/v1/search?q={theme}&limit=10&key={my_tenorAPI_key}&media_filter=gif"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()["results"]
    a_gif = choice(choice(response)["media"])["gif"]["url"]
    return a_gif


def get_meaning_dictionary_api(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}"

    payload = {}
    headers = {}
    
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    output_list = list()

    try:

      for i in response:
          output_list.append(f'Word : {i["word"]}')
          for meanings in i['meanings']:
              output_list.append(' ' * 4 + f'Part of Speech : {meanings["partOfSpeech"]}')
              output_list.append(' ' * 4 + "Definitions")
              for definitions in meanings['definitions']:
                  output_list.append(' ' * 8 + f'definition :')
                  output_list.append(' ' * 12 + definitions["definition"])
                  if 'synonyms' in definitions.keys():
                      output_list.append(' ' * 8 + 'Synonym : ')
                      for synonym in definitions['synonyms']:
                          output_list.append(' ' * 12 + synonym)
                  if 'example' in definitions.keys():
                      output_list.append(' ' * 8 + f'Examples : {definitions["example"]}')
      return output_list
    except:
      return ['No result found']


def get_joke():
    j = Jokes()  # Initialise the class
    joke = j.get_joke()  # Retrieve a random joke
    if joke["type"] == "single":  # Print the joke
        return joke["type"], joke["joke"]
    else:
        return joke["type"], joke["setup"], joke["delivery"]


def get_quote():
    response = requests.get(
        'https://goquotes-api.herokuapp.com/api/v1/random?count=1')
    response = response.json()
    quote = response['quotes'][0]['text']
    author = response['quotes'][0]['author']
    return f'```\n{quote}\n -{author}\n```'


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower().strip()

    if msg == 'sid':
        await message.reply("Hi How are you!")
    elif msg.startswith('sid '):
        if msg == 'sid':
            await message.channel.send("Hi How are you!")
        else:
            command = msg.split('sid ', 1)[1]
            if command == 'help':
                help_message = "```\nI can:\n  entertain you with a joke just type 'sid joke',\n  inspire you with a quote just type 'sid quote'\n```"
                await message.channel.send(help_message)
            elif command == 'quote':
                await message.channel.send(get_quote())
            elif command == 'joke':
                joke = get_joke()
                if joke[0] == 'single':
                    await message.channel.send('```\n' + joke[1] + '\n```')
                elif joke[0] == 'twopart':
                    await message.channel.send('```\n' + joke[1] + '\n```')
                    await asyncio.sleep(5)
                    await message.channel.send('```\n' + joke[2] + '\n```')
            elif command.startswith('define '):
                word = command[6:].strip()
                definition = '\n'.join(get_meaning_dictionary_api(word))
                await message.channel.send('```\n' + definition + '\n```')
            elif command.startswith('gif '):
                try:
                    gif_url = get_gif_url(command[4:])
                    embed = discord.Embed()
                    embed.set_image(url=gif_url)
                    await message.channel.send(embed=embed)
                except :
                    await message.channel.send(f"What the hell is {command} ?")
            else:
              await message.channel.send(f"What the hell is {command} ?")


keep_alive()
client.run(my_discord_key)