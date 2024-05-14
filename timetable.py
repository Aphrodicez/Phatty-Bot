import os

import discord
from discord import channel
from discord import client
from discord import embeds
from discord.client import Client
from discord.embeds import Embed
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

time_subject = 40
time_break = 10

Subject_Dictionary = {
    # Get a life
    "Get a life" : [
        "Get a life",
        "",
        "Get a life, please",
        time_subject,
        "",
    ],
    # Free
    "Free Time" : [
        "Free Time",
        "",
        "",
        time_subject,
        "",
    ],
    # Break
    "Break" : [
        "Break",
        "",
        "สงสัยล่ะสิ ทำไมไม่ใครเข้ามีท",
        time_break,
        "",
    ],
    "Lunch" : [
        "Lunch",
        "",
        "Get a life, please",
        time_subject,
        "",
    ],
    # Subject
    "Advance" : [
        "Advance",
        "",
        "",
        time_subject,
        "",
    ],
    "Ratchadawan" : [
        "Math Ratchadawan",
        "https://classroom.google.com/c/MzQ5MTQ4NDQyNjYx",
        "https://meet.google.com/uuf-hyrz-qqy",
        time_subject,
        "",
    ],
    "Homeroom" : [
        "Homeroom",
        "",
        "https://meet.google.com/vum-xrpn-sav",
        time_subject,
        "",
    ],
    "Siriporn" : [
        "Math Siriporn",
        "https://classroom.google.com/c/MzM5ODkwMDY3OTA3",
        "https://meet.google.com/dev-ejws-soi",
        time_subject,
        "",
    ],
    "Thai" : [
        "Thai",
        "",
        "หัดเปิด LINE ดูบ้างนะ",
        time_subject,
        "",
    ],
    "Music" : [
        "Music",
        "https://classroom.google.com/c/NDE5NzI0NTg5MTc2",
        "https://meet.google.com/onc-nnzp-mjp",
        time_subject,
        "",
    ],
    "Social" : [
        "Social",
        "https://classroom.google.com/c/NDE5NzIwMzgwMTU5",
        "",
        time_subject,
        "",
    ],
    "Kritsadaporn" : [
        "Eng Kritsadaporn",
        "https://classroom.google.com/c/MzQ4NjI0MTI1NDky",
        "https://meet.google.com/mzo-zwvz-xwo",
        time_subject,
        "",
    ],
    "Poonnapa" : [
        "Eng Poonnapa",
        "https://classroom.google.com/c/MzUxMTgyNTc1NDQ0",
        "https://meet.google.com/vye-skkx-cgh",
        time_subject,
        "",
    ],

    "Kimberly" : [
        "Eng Kimberly",
        "https://classroom.google.com/c/MzUxMTgyNTc1NDQ0",
        "https://meet.google.com/vye-skkx-cgh",
        time_subject,
        "",
    ],
    "Richard" : [
        "Eng Richard",
        "https://classroom.google.com/c/MzQ5Nzc3MDk1ODY3",
        "https://meet.google.com/err-jpoq-ngx",
        time_subject,
        "",
    ],
    "Health" : [
        "Health",
        "",
        "หัดเปิด LINE ดูบ้างนะ",
        time_subject,
        "",
    ],
    "PE" : [
        "PE",
        "",
        "",
        time_subject,
        "",
    ],
    "Chemistry" : [
        "Chemistry",
        "https://classroom.google.com/c/MzUxMTk4MTgyNDIx",
        "https://meet.google.com/xjz-wvdd-can",
        time_subject,
        "",
    ],
    "Biology" : [
        "Biology",
        "https://classroom.google.com/c/MzUyNzI4OTU4MzQ3",
        "https://meet.google.com/lookup/f364sytfpk",
        time_subject,
        "",
    ],
    "Physics" : [
        "Physics",
        "https://classroom.google.com/c/MzQ5NzY3Mjk2NzM0",
        "ไอเหี้ยนี่เปลี่ยนทุกคาบ",
        time_subject,
        "",
    ],
    "Astronomy" : [
        "Astronomy",
        "https://classroom.google.com/c/MzQ3NDY3OTc5OTM4",
        "https://meet.google.com/abq-hrrc-waq",
        time_subject,
        "",
    ],
    "Wichuda" : [
        "Com Wichuda",
        "https://classroom.google.com/c/MzU3NjY0ODgwODgy",
        "https://meet.google.com/jsj-dsyy-kcx",
        time_subject,
        "",
    ],
    "Nongluck" : [
        "Com Nongluck",
        "https://classroom.google.com/c/NDE5NjQ4MjcwODU4",
        "https://meet.google.com/gky-fpdh-iyy",
        time_subject,
        "**Check In**\t:\t" + "https://forms.gle/BqsJfimYtF4n4WLV8",
    ],
    "Wattana" : [
        "Com Wattana",
        "https://classroom.google.com/c/MzUyNzM5MzU0MjM3",
        "https://meet.google.com/ipx-pqtn-scx",
        time_subject,
        "",
    ],
    "Guidedance" : [
        "Guidedance",
        "https://classroom.google.com/c/MzcwMjcwNDkwNDAw",
        "https://meet.google.com/krj-ptiy-obs",
        time_subject,
        "",
    ],
    "Cookery" : [
        "Cookery",
        "https://classroom.google.com/c/NDIwNDk2MTA3MTQ3",
        "https://meet.google.com/yzy-xozo-yrj",
        time_subject,
        "",
    ],
}

# Variables
subject_string = [["Ratchadawan", "Thai", "Break", "Astronomy", "Social", "Lunch", "Cookery", "Break", "Music", "Nongluck", "Nongluck", "Get a life"],
                  ["Biology", "Biology", "Break", "Physics", "Wattana", "Lunch", "Chemistry", "Break", "Thai", "Ratchadawan", "Get a life"], 
                  ["Homeroom", "Ratchadawan", "Break", "Kimberly", "Richard", "Lunch", "Social", "Break", "Siriporn", "Guidedance", "Wichuda", "Wichuda", "Get a life"],
                  ["Advance", "Advance", "Break", "Biology", "Health", "Lunch", "Siriporn", "Break", "Ratchadawan", "Poonnapa", "Get a life"],
                  ["Siriporn", "PE", "Break", "Physics", "Physics", "Lunch", "Free Time", "Break", "Kritsadaporn", "Chemistry", "Chemistry", "Get a life"],
                  [],
                  []]

weekday_string = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def to_24Hours(current_time):
    return str((current_time // 60)).zfill(2) + " : " + str((current_time % 60)).zfill(2)

def bold(string):
    return "\033[1m" + string + "\033[0m"

def subject(subject_name, subject_begin, subject_end, next_subject):
    subject_begin = str((subject_begin // 60)).zfill(2) + " : " + str((subject_begin % 60)).zfill(2)
    subject_end = str((subject_end // 60)).zfill(2) + " : " + str((subject_end % 60)).zfill(2)
    global EmbedText
    EmbedText = discord.Embed(title = "Current Subject : ")
    this_subject = Subject_Dictionary[subject_name]
    EmbedText.color = 0x8FB3CA
    EmbedText.add_field(name = this_subject[0], 
                        value = 
                                "**Subject Begin : **\t" + subject_begin + '\n' + 
                                "**Subject End   : **\t" + subject_end + '\n' + 
                                "**Next Subject\t:\t**" + next_subject +'\n' + 
                                "**Classroom**\t:\t" + this_subject[1] + '\n' + 
                                "**Meet**\t:\t" + this_subject[2] + '\n' +
                                this_subject[4])

    EmbedText.set_footer(text = "Phatty-BOT", icon_url = "https://cdn.discordapp.com/attachments/739066342019301457/905774545590431744/firewatch_minimalist_wallpaper_by_trueru18_dco2151-fullview.jpg")
    return EmbedText

def ttb(day_in_week, today_timetable):
    embed = discord.Embed(title = weekday_string[day_in_week] + " Subject : ")
    embed.color = 0x8FB3CA
    value = ""
    # embed.add_field(name = weekday_string[day_in_week], value = value)
    for (subject_name, current_time) in today_timetable:
        subject_begin = to_24Hours(current_time)
        subject_end = to_24Hours(current_time + 40)
        embed.add_field(name = subject_name + ' : \t', value = 
                        "**Subject Begin : **" + subject_begin + '\n' + 
                        "**Subject End   : **" + subject_end + '\n', inline = False)
        # value += subject_name + ' : \t'+ subject_begin + '\t' + subject_end + '\n'
    embed.set_footer(text = "Phatty-BOT", icon_url = "https://cdn.discordapp.com/attachments/739066342019301457/905774545590431744/firewatch_minimalist_wallpaper_by_trueru18_dco2151-fullview.jpg")
    return embed