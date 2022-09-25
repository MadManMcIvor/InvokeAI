import discord
from discord.ext import commands

import os
import sys
import time

#sys.path.append("c:\\Users\\mcivo\\Desktop\\Stable Diffusion CLI\\stable-diffusion\\ldm")
from ldm.generate import Generate

from bot_token import bot_token

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #test it's working w/ $hello
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$prompt'):
        await message.channel.send(f"Working on {message.author}'s very weird request")
       
        input = message.content[8::]
        gr = Generate()
        results = gr.prompt2image(prompt   = input,
                                outdir   = "./outputs/")

        image_path = ''
        for row in results:
            im   = row[0]
            seed = row[1]
            input_dashed = input.replace(' ','_')
            image_path = f'./outputs/img_samples/{input_dashed}-{seed}.png'
            im.save(image_path)

        await message.channel.send(f"Finished. Hmmmm... Exactly what I thought {input} would look like.", file=discord.File(image_path))
        time.sleep(1.0)


client.run(bot_token)