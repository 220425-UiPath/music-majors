import os
import airium
import asyncio
import multiprocessing
import subprocess
from discord.ext import commands

bot = commands.Bot(command_prefix='!!')
bot.remove_command('help')

globalCooldown = False

@bot.event
async def on_ready():
    print('[BardBot] Connected to Discord.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f'{message.author}: {message.content}')

    await bot.process_commands(message)

@bot.command()
async def help(ctx):
    await ctx.send('Available commands:\n!!play <YouTube URL or search string>\n!!pause\n!!resume\n!!skip\n!!volume <Volume level between 0-100>')

@bot.command()
async def play(ctx, *, arg):
    global globalCooldown
    if not globalCooldown:
        globalCooldown = True
        await ctx.send('Received play command.')
        output_html('play', arg)
        await asyncio.sleep(2.5)
        output_html('', '')
        await asyncio.sleep(2.5)
        globalCooldown = False

def output_html(command, arg):
    doc = airium.Airium()
    queueFile = open(f'{os.getcwd()}\CommandQueue.html', 'w+b')
    doc('<!DOCTYPE html>')
    with doc.html():
        with doc.head():
            doc.title('BardBot Command Queue')
            doc.script(src='https://livejs.com/live.js')
        with doc.body():
            with doc.p(id='command'):
                doc(command)
            with doc.p(id='arg'):
                doc(arg)
    queueFile.write(bytes(doc))
    queueFile.close()

def run_local_webserver():
    print('[BardBot] Starting local webserver.')
    output_html('', '')
    subprocess.call('py -m http.server --bind localhost 8888')

def run_discord_bot():
    print('[BardBot] Starting Discord connection.')
    bot.run('OTgyMzUyNzI0Nzk0NDM3NjQy.GpGcuZ.euQh0O52q3p5px7aw0bstYk5VuHXrpVARY1blM')

def run_parallel(*functions):
    processes = []
    for function in functions:
        process = multiprocessing.Process(target=function)
        process.start()
        processes.append(process)
    for process in processes:
        process.join()

if __name__ == '__main__':
    try:
        multiprocessing.freeze_support()
        run_parallel(run_local_webserver, run_discord_bot)
    finally:
        output_html('', '')