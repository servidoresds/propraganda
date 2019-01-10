import random
import discord
import asyncio
import requests
import json
import time
import datetime
import safygiphy
import os

g = safygiphy.Giphy()
start_time = {"start_time1": time.time()}
color = 0xcf9be7


client = discord.Client()




@client.event
async def on_ready():
    print(client.user.name)
    print('Logged in as ---->', client.user)
    print('ID:', client.user.id)
    print("Servidores: {} Serves".format(str(len(client.servers))))


@client.event
async def on_member_join(member):
  embed1 = discord.Embed(colour=color)
  embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
  embed1 = discord.Embed(title="Lunna",color=color,description='**Seja bem-vindo ao Servidor! <@{}\n\nQuer conheçer meu suporte? 💖\nSegue o link!\nVenha fazer parte da nossa familia 💑\nLink logo abaixo 💌**', url="https://discord.gg/ZrJYwHV".format(member.id))
  await client.send_message(member,embed=embed1)

client.run(str(os.environ.get('TOKEN')))
