
from . import *

if DATABASE_URL:
   from .database import users_db
   print("🥀 𝐃𝐄𝐏𝐋𝐎𝐘𝐈𝐍𝐆 𝐓𝐎 ⚡️ 𝐌𝐎𝐎𝐍 𝐁𝐎𝐓𝐒 🥀")
   for x in sudoser:
      users_db.addsudo(x)
     
if __name__ == "__main__":
    Run_SpamX()
