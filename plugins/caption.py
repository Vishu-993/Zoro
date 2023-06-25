from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import *
import asyncio

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
        caption = find(int(message.chat.id))[1]
        if caption:
            msg = await message.reply_text(f"Your custom caption is:\n\n`{caption}`",
                                           reply_markup=InlineKeyboardMarkup([
                                               [InlineKeyboardButton("Edit Caption", callback_data="edit_caption")],
                                               [InlineKeyboardButton("Delete Caption", callback_data="delete_caption")],
                                           ]))
            await asyncio.sleep(20)
            await msg.delete()
        else:
            await message.reply_text("**Give me a caption to set.\n\nExample: `/set_caption {filename}\n\n💾 Size: {filesize}\n\n⏰ Duration: {duration}`**")
        await message.delete()
        return
    
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("**🙂 Your caption successfully added ✅**")
    await message.delete()

@Client.on_message(filters.private & filters.command('delete_caption'))
async def delete_caption(client, message):
    caption = find(int(message.chat.id))[1]
    if not caption:
        msg = await message.reply_text("**🫠 You don't have any custom caption 🫠**")
    else:
        delcaption(int(message.chat.id))
        msg = await message.reply_text("**😶‍🌫️ Your caption successfully deleted ✅**")
    await asyncio.sleep(20)
    await msg.delete()
    await message.delete()

@Client.on_message(filters.private & filters.command('view_caption'))
async def view_caption(client, message):
    caption = find(int(message.chat.id))[1]
    if caption:
        msg = await message.reply_text(f"<b><u>Your Caption:</b></u>\n\n`{caption}`")
    else:
        msg = await message.reply_text("**You don't have any custom caption**")
    await asyncio.sleep(20)
    await msg.delete()
    await message.delete()

@Client.on_callback_query()
async def handle_callbacks(client, callback_query):
    if callback_query.data == "edit_caption":
        await edit_caption(client, callback_query)
    elif callback_query.data == "delete_caption":
        await delete_caption(client, callback_query)

async def edit_caption(client, callback_query):
    chat_id = callback_query.message.chat.id
    caption = find(int(chat_id))[1]
    if caption:
        msg = await client.send_message(chat_id, f"Your current caption is:\n\n`{caption}`\n\nSend me the new caption.")
    else:
        msg = await client.send_message(chat_id, "You don't have any custom caption. Send me the new caption.")
    await asyncio.sleep(20)
    await msg.delete()

async def delete_caption(client, callback_query):
    chat_id = callback_query.message.chat.id
    caption = find(int(chat_id))[1]
    if caption:
        delcaption(int(chat_id))
        msg = await client.send_message(chat_id, "**😶‍🌫️ Your caption successfully deleted ✅**")
    else:
        msg = await client.send_message(chat_id, "**🫠 You don't have any custom caption to delete 🫠**")
    await asyncio.sleep(20)
    await msg.delete()

app = Client("caption_bot")

if __name__ == "__main__":
    app
