from unittest import case
import discord

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'[BardBot] Connected to Discord.')
    queueFile = open('QueueItems.txt', 'w')
    queueFile.write('')
    queueFile.close()
    

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    messageContents = message.content
    print(f'{message.author}: {messageContents}')

    if messageContents.startswith('!!'):
        commandArgs = messageContents.split(' ', 1)
        process_command(commandArgs[0], commandArgs[1])

def process_command(command, args):
    match command:
        case '!!play':
            retries = 5
            while retries > 0:
                try:
                    queueFile = open('QueueItems.txt', 'a')
                    queueFile.write(f'{args}\n')
                    queueFile.close()
                    print('[BardBot] Song request added to queue.')
                except:
                    print(f'[BardBot] Problem encountered while adding request to queue. Retries left: {retries}')
                    retries -= 1
                    continue
                break
        

bot.run('OTgyMzUyNzI0Nzk0NDM3NjQy.GpGcuZ.euQh0O52q3p5px7aw0bstYk5VuHXrpVARY1blM')