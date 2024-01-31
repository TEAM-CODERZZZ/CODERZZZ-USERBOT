from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "⚡️𝐌 𝐎 𝐎 𝐍⚡️"
pic = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/1e406d15905398d0210df.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "𝐌𝐎𝐎𝐍 𝐒𝐏𝐀𝐌 - by ⚡️𝐌 𝐎 𝐎 𝐍⚡️"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**[⚡️𝐌 𝐎 𝐎 𝐍⚡️](https://t.me/THE_GLACEON)
◈ •━━━━━★✦♡✦★━━━━━• ◈ 
➪ **𝐌𝐀𝐒𝐓𝐄𝐑:**[⚡️𝐌 𝐎 𝐎 𝐍⚡️](https://t.me/MOON_M_6)
➪ **𝐏𝐘𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍:** `{platform.python_version()}`
➪ **⚡️𝐌 𝐎 𝐎 𝐍⚡️ 𝐕𝐄𝐑𝐒𝐈𝐎𝐍:** `{__version__}`
➪ **𝐏𝐘𝐑𝐎 𝐕𝐄𝐑𝐒𝐈𝐎𝐍:** `{pyro_vr}`
◈ •━━━━━★✦♡✦★━━━━━• ◈
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
