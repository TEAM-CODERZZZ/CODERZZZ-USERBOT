
from . import *

if DATABASE_URL:
   from .database import users_db
   print("💦𝘿𝙀𝙋𝙇𝙊𝙔𝙄𝙉𝙂 𝙏𝙊 ⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️ 𝘽𝙊𝙏 🛑")
   for x in sudoser:
      users_db.addsudo(x)
     
if __name__ == "__main__":
    Run_SpamX()
