
from . import *

if DATABASE_URL:
   from .database import users_db
   print("🥀 𝗗𝗲𝗽𝗹𝗼𝘆𝗶𝗻𝗴 𝗧𝗼 𝗖𝗼𝗱𝗲𝗿𝘇 𝗕𝗼𝘁𝘀🥀")
   for x in sudoser:
      users_db.addsudo(x)
     
if __name__ == "__main__":
    Run_SpamX()
