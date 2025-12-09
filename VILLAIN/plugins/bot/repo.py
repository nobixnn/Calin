from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VILLAIN import app
from config import BOT_USERNAME
from VILLAIN.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**Cʟᴏɴɪғʏ** - Tʜᴇ Uʟᴛɪᴍᴀᴛᴇ Tᴇʟᴇɢʀᴀᴍ Mᴜsɪᴄ Sᴏʟᴜᴛɪᴏɴ ᴡɪᴛʜ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇs.

┏━━━━━━━━━━━━━━━━━⧫
┠ ◆ **𝐅ʀᴇᴇ 𝐏ʀᴏᴍᴏᴛɪᴏɴ:** [Click Here](https://t.me/LINK_KI_HAWELII)  
┠ ◆ **𝐃ᴇᴠᴇʟᴏᴘᴇʀ:** [༐DEV](https://t.me/lNobil)
┠ ◆ **ʀᴇʟᴇᴀsᴇᴅ ʙʏ:** [𝐁ᴏᴛ 𝐗 𝐌ᴇᴅɪᴀ](https://t.me/BotXMedia)
┗━━━━━━━━━━━━━━━━━⧫

__𝐁ᴏᴛ 𝐗 𝐌ᴇᴅɪᴀ__
"""





@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
                InlineKeyboardButton("𝐃ᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/lNobil"),
                InlineKeyboardButton("𝐁ᴏᴛ 𝐗 𝐌ᴇᴅɪᴀ", url="https://t.me/BotXMedia")
        ],
       
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://i.ibb.co/gFm6VW52/source-code.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/aditya88402/Heistsnetwork/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://t.me/BotXMedia) |
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
