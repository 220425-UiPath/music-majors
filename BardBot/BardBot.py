import airium
import discord
import multiprocessing
import subprocess

bot = discord.Client()

@bot.event
async def on_ready():
    print('[BardBot] Connected to Discord.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    messageContents = message.content
    print(f'{message.author}: {messageContents}')

    if messageContents.startswith('!!'):
        process_command(messageContents)

def process_command(command):
    commandParts = command.split(' ', 1)
    match commandParts[0]:
        case '!!play':
            output_html('play', commandParts[1])
        case '!!pause':
            output_html('pause', '')
        case '!!resume':
            output_html('resume', '')
        case '!!skip':
            output_html('skip', '')
        case '!!volume':
            output_html('volume', commandParts[1])

def output_html(command, arg):
    doc = airium.Airium()
    queueFile = open('CommandQueue.html', 'w+b')
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
    subprocess.call('python -m http.server --bind localhost 8888')

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
    run_parallel(run_local_webserver, run_discord_bot)