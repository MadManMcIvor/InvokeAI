import discord
from discord.ext import commands

import os
import sys
import time

#sys.path.append("c:\\Users\\mcivo\\Desktop\\Stable Diffusion CLI\\stable-diffusion\\ldm")
from ldm.generate import Generate

#make a directory "bot_token" and put your Bot's Token from Discord in as the variable bot_token
from bot_token import bot_token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# @bot.command()
# async def prompt(ctx, *arg):
#     '''
#     $prompt Write a prompt for Stable Diffusion to generate.
#     '''
#     await ctx.send(f"Working on {ctx.author}'s very weird request")

#     input = arg
#     gr = Generate()
#     results = gr.prompt2image(prompt   = input,
#                             outdir   = "./outputs/")

#     image_path = ''
#     for row in results:
#         im   = row[0]
#         seed = row[1]
#         input_dashed = input.replace(' ','_')
#         image_path = f'./outputs/img_samples/{input_dashed}-{seed}.png'
#         im.save(image_path)

#     await ctx.send(f"Finished. Hmmmm... Exactly what I thought {input} would look like.", file=discord.File(image_path))
#     time.sleep(1.0)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    #test it's working w/ $hello
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$prompt'):
        await message.channel.send(f"Working on {message.author}'s request")
       
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


bot.run(bot_token)