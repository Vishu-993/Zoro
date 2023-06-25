from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import *

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
        caption = find(int(message.chat.id))[1]
        if caption:
            await message.reply_text(f"Your custom caption is:\n\n`{caption}`")
        else:
            await message.reply_text("**Give me a caption to set.\n\nExample: `/set_caption {filename}\n\n💾 Size: {filesize}\n\n⏰ Duration: {duration}`**")
        return
    
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("**🙂 Your caption successfully added ✅**")

@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = find(int(message.chat.id))[1]
    if not caption:
        await message.reply_text("**🫠 You don't have any custom caption 🫠**")
        return
    delcaption(int(message.chat.id))
    await message.reply_text("**😶‍🌫️ Your caption successfully deleted ✅**")

@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    caption = find(int(message.chat.id))[1]
    if caption:
        await message.reply_text(f"<b><u>Your Caption:</b></u>\n\n`{caption}`")
    else:
        await message.reply_text("**You don't have any custom caption**")
