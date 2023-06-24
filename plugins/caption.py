from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import *

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**♻️ Custom Caption ♻️/n/nBy default all messages will be forwarded with its default captions
Instead of this, you can set a custom caption/n/nFilling options:
{name} : file name
{size} : file size
{caption} : default caption of messages`**")
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("**Your Caption successfully added ✅**")

@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if not caption:
        await message.reply_text("**You dont have any custom caption**")
        return
    delcaption(int(message.chat.id))
    await message.reply_text("**Your caption successfully deleted ✅**")
                                       
@Client.on_message(filters.private & filters.command('view_caption'))
async def see_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if caption:
       await message.reply_text(f"<b><u>Your Caption:</b></u>\n\n`{caption}`")
    else:
       await message.reply_text("**You dont have any custom caption**")
          
