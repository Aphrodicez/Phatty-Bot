import os

import discord
from discord import channel
from discord import client
from discord import embeds
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.tasks import loop
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from PIL import Image, ImageFilter
from io import BytesIO

import schedule
import datetime
import bisect
import timetable
import Function

#Variables
client = discord.Client()
bot = commands.Bot(command_prefix = 'o/')
#bot.remove_command('help')
channel_id = 882332578454056960
channel_id_link_meet = 882332578454056960
channel_id_bot_test = 904992063710457856

test_run = False

# Bot Online
@bot.event
async def on_ready():
    #channel = discord.utils.get(bot.get_all_channels(), name = "link-meet")
    global channel_id
    if test_run:
        channel_id = channel_id_bot_test
    channel = bot.get_channel(channel_id)
    print('We have logged in as {0.user}'.format(bot))
    OnlineText = discord.Embed(title = "Phatty Bot is now online!", color = 0x8FB3CA)
    await channel.send(embed = OnlineText)

#Text-Chat
@bot.event
async def on_message(message):
    text = message.content
    ch = message.channel
    if text.lower() == 'smurf':
        await ch.send(Function.smurf)
    await bot.process_commands(message) # To use Prefix Commands

#commands

# echo
@bot.command()
async def echo(ctx, *args):
    message_args = " ".join(args)
    await ctx.send(message_args)

#ping
@bot.command()
async def ping(ctx):
    print(datetime.datetime.now())
    await ctx.send(f'Bot Latency is {round(bot.latency * 1000)} ms')
#
@bot.command()
async def ban(ctx,member:discord.Member=None):
    if not member:
        member = ctx.author
    spg = Image.open("E:\GitHub\Phatty_BOT\Phatty_BOT\ssban.png")
    asset = member.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((237,237))
    spg.paste(pfp, (139,135))
    spg.save('banned.png')
    await ctx.send(file = discord.File('banned.png'))

# Show today's timetable
@bot.command()
async def ttb(ctx):
    await ctx.send(embed = timetable.ttb(day_in_week, today_timetable))

@bot.command()
async def thissubject(ctx):
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.hour * 60 + current_datetime.minute
    upper_bound = bisect.bisect_right(time_list, current_time, lo = 0, hi = len(time_list))
    embed = subject_list[min(upper_bound - 1, len(time_list) - 1)]
    await ctx.send(embed = embed)

@bot.command()
async def nextsubject(ctx):
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.hour * 60 + current_datetime.minute
    upper_bound = bisect.bisect_right(time_list, current_time, lo = 0, hi = len(time_list))
    embed = subject_list[min(upper_bound - 1 + 1, len(time_list) - 1)]
    embed.title = "Next Subject : "
    await ctx.send(embed = embed)

# Schedule

# Show Subject
async def showsubject(Embed_Subject):
    linkmeet = bot.get_channel(882332578454056960)
    await linkmeet.send(embed = Embed_Subject)

# Print Subjects List
time_list = []
subject_list = []
today_timetable = []

alarmclass = AsyncIOScheduler()
day_in_week = datetime.datetime.today().weekday()
cnt = 0
current_time = 8 * 60 + 15
idx = 0

for subject_name in timetable.subject_string[day_in_week]:    
    time_list.append(current_time + 5)
    next_time = current_time + timetable.Subject_Dictionary[subject_name][3]
    if subject_name == "Get a life":
        next_subject = "Get a fucking life, please"
    else:
        next_subject = timetable.Subject_Dictionary[timetable.subject_string[day_in_week][idx + 1]][0]
    Embed_Subject = timetable.subject(subject_name, current_time + 5, next_time + 5, next_subject)
    subject_list.append(Embed_Subject)
    if subject_name == "Get a life":
        break
    today_timetable.append((subject_name, current_time + 5))
    alarmclass.add_job(showsubject, CronTrigger(day_of_week = day_in_week, hour = current_time // 60, minute = current_time % 60), args = [Embed_Subject])
    current_time = next_time
    idx += 1

alarmclass.start()

#show_list_subject.start()

token = "?"
bot.run(token)

'''
@loop(count = 1)
async def show_list_subject():
    channel = bot.get_channel(channel_id)
    for embed in subject_list:
        await channel.send(embed = embed)

@show_list_subject.before_loop
async def before_send_links():
    await bot.wait_until_ready()  # Wait until bot is ready.
'''