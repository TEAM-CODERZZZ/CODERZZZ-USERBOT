""" © MOON """

from .config import *
from .database import *
from .core import *
from pyrogram import Client 
from RiZoeLX.functions import * # make_list
import time, os, sys


print("🥀 𝗗𝗲𝗽𝗹𝗼𝘆𝗶𝗻𝗴 𝗧𝗼 𝗖𝗼𝗱𝗲𝗿𝘇 𝗕𝗼𝘁𝘀🥀")

#__version__ = "v0.5"
"""start time"""
start_time  = time.time()

try:
   OWNER_ID = int(OWNER_ID)
except ValueError:
   raise Exception("Your OWNER_ID variable is not a valid integer.")

"""Sudo Users"""
sudoser = []
if SUDO_USERS:
  sudoser = make_list(OWNER_ID, SUDO_USERS)
else:
  sudoser.append(OWNER_ID)

AUTO_REACT = []
if auto_re:
   AUTO_REACT = make_list(-1001244090544, auto_re)
else:
   AUTO_REACT.append(-1001244090544)

EMOJI_LIST = ['❤️', '✨', '🔥', '🥰', '💫', '💯', '🌟', '😁', '💥']
