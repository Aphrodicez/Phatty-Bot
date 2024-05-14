import os

import discord
from discord import channel
from discord import client
from discord.client import Client
from discord.embeds import Embed
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

smurf = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fsmurfs.fandom.com%2Fwiki%2FGeneric_Smurf&psig=AOvVaw01RfXR9mNYkzIQKd9pk0Tt&ust=1715755475558000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCKCfza7FjIYDFQAAAAAdAAAAABAH"