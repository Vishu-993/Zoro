from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import *

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Give me a caption to set.\n\nExample:- `/set_caption {filename}\n\n💾 Size: {filesize}\n\n⏰ Duration: {duration}`**")
       if caption:
       await message.reply_text(f"<b><u>𝘠𝘰𝘶𝘳 𝘊𝘢𝘱𝘵𝘪𝘰𝘯:</b></u>\n\n`{caption}`")
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("**🙂𝘠𝘰𝘶𝘳 𝘊𝘢𝘱𝘵𝘪𝘰𝘯 𝘴𝘶𝘤𝘤𝘦𝘴𝘴𝘧𝘶𝘭𝘭𝘺 𝘢𝘥𝘥𝘦𝘥 ✅**")

@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if not caption:
        await message.reply_text("**🫠 𝘠𝘰𝘶 𝘥𝘰𝘯𝘵 𝘩𝘢𝘷𝘦 𝘢𝘯𝘺 𝘤𝘶𝘴𝘵𝘰𝘮 𝘤𝘢𝘱𝘵𝘪𝘰𝘯 🫠**")
        return
    delcaption(int(message.chat.id))
    await message.reply_text("**😶‍🌫️𝘠𝘰𝘶𝘳 𝘤𝘢𝘱𝘵𝘪𝘰𝘯 𝘴𝘶𝘤𝘤𝘦𝘴𝘴𝘧𝘶𝘭𝘭𝘺 𝘥𝘦𝘭𝘦𝘵𝘦𝘥 ✅**")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if caption:
       await message.reply_text(f"<b><u>Your Caption:</b></u>\n\n`{caption}`")
    else:
       await message.reply_text("**You dont have any custom caption**")
          
