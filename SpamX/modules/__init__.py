from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "🍃𝗖𝗢𝗗𝗘𝗥𝗭𝗭𝗭🍃"
pic = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/50936a7037d6683910591.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "𝐒𝐏𝐀𝐌 - by 🍃𝗖𝗢𝗗𝗘𝗥𝗭𝗭𝗭🍃"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**[🍃𝗖𝗢𝗗𝗘𝗥𝗭𝗭𝗭🍃](https://t.me/Noob_Coderzzz)
◈ •━━━━━★✦♡✦★━━━━━• ◈ 
➪ **𝐌𝐀𝐒𝐓𝐄𝐑:**[🍃𝗖𝗢𝗗𝗘𝗥𝗭𝗭𝗭🍃](https://t.me/Noob_Coderzzz)
➪ **𝐏𝐘𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍:** `{platform.python_version()}`
➪ **🍃𝗖𝗢𝗗𝗘𝗥𝗭𝗭𝗭🍃 𝐕𝐄𝐑𝐒𝐈𝐎𝐍:** `{__version__}`
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
