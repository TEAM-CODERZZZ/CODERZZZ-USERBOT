
from . import *

if DATABASE_URL:
   from .database import users_db
   print("💞𝙎𝙐𝘾𝘾𝙀𝙎𝙎𝙁𝙐𝙇 💦𝘿𝙀𝙋𝙇𝙊𝙔𝙀𝘿 𝘽𝙔 𝘾𝙊𝘿𝙀𝙓 🛑")
   for x in sudoser:
      users_db.addsudo(x)
     
if __name__ == "__main__":
    Run_SpamX()
