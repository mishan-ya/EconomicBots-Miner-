import discord
from discord.ext import commands 
import random
import time

client = commands.Bot(command_prefix='af', self_bot = True, intents=discord.Intents.default()) 
TOKEN = "" #здесь токен от аккаунта 

hours = 10800
minutes = 0
cycle = 0
activetime = time.localtime(time.time())
activehour = activetime.tm_hour

@client.event
async def on_ready():
    print('Напиши "afping" от лица аккаута в любой канал, чтобы проверить работу кода!') #not translated
    print('Напиши "afstart" чтобы начать авто-фарм.') #not translated


@client.command()
async def start(ctx):
    global hours,cycle,minutes,activetime,activehour
    print(time.ctime(time.time()), '- startup')
    time.sleep(3)
    for i in range(999):
        activetime = time.localtime(time.time())
        activehour = activetime.tm_hour
        if activehour >= 9 and activehour <= 22:
            await ctx.send("!work")
            print("1/4 type'ed")
            time.sleep(random.randint(3, 20))
            await ctx.send("!crime")
            print("2/4 type'ed")
            time.sleep(random.randint(3, 20))
            await ctx.send("!slut")
            print("3/4 type'ed")
            time.sleep(random.randint(3, 20))
            await ctx.send("!dep all")
            print("4/4 type'ed")
            cycle = cycle + 1
            minutes = random.randint(60, 600)
            print(time.ctime(time.time()), "- цикл:", cycle, "- следующий цикл через 2ч +", minutes, "секунд.") #not translated
            time.sleep(hours + minutes)
        elif activehour <= 8 or activehour >= 23:
            minutes = random.randint(60, 600)
            print(time.ctime(time.time()), "- время сна, следующая попытка цикла через 2ч +", minutes, "секунд.") #not translated
            time.sleep(hours + minutes)
	

@client.command()
async def ping(ctx):
    #print("Hi there!")
	await ctx.send(time.ctime(time.time()))

client.run(TOKEN, bot=False) 
