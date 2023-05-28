import discord
from discord.ext import commands
import random
import os
print(os.listdir('nature'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def helpme(ctx):
     await ctx.send("Комманд немного, вот список:")
     await ctx.send("mudrost - даёт совет для помощи природе")
     await ctx.send("biomem - скидывает случайный мем о природе")
     await ctx.send("chacha - советую лично это проверить ;)")
     await ctx.send("перед каждой командой пиши $")
     await ctx.send("clear - удаляет последние 5 сообщений (кол-во сообщений можно регулировать, дописав число) пример: сlear 10")

@bot.command()
async def biomem(ctx):
    
    images = os.listdir('nature') 
    img_name = random.choice(images)
    
    with open(f'nature/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def chacha(ctx):
    with open('chacha/img1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def mudrost(ctx):
     await ctx.send("Я тебе советую")
     
     words_list = ["Сортировать мусор", "Не выбрасывать вещи в неположенных местах", "по возможности перейти на более чистый вид энергии", "Записаться в волонтёры для помощи природе"]
     
     random_word = random.choice(words_list)
     
     await ctx.send(random_word)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5): 
    await ctx.channel.purge(limit=amount)

bot.run("token")
