from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import *
import asyncio

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
        caption = find(int(message.chat.id))[1]
        if caption:
            msg = await message.reply_text(
                f"Your custom caption is:\n\n`{caption}`",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Delete Caption", callback_data="delete_caption")]
                ])
            )
        else:
            msg = await message.reply_text(
                "**Give me a caption to set.\n\nExample: `/set_caption {filename}\n\n💾 Size: {filesize}\n\n⏰ Duration: {duration}`**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("View Caption", callback_data="view_caption")]
                ])
            )
        await asyncio.sleep(5)  # Wait for 5 seconds
        await message.delete()
        await msg.delete()

@Client.on_message(filters.private & filters.command('delete_caption'))
async def delete_caption(client, message):
    caption = find(int(message.chat.id))[1]
    if not caption:
        await message.reply_text("**🫠 You don't have any custom caption 🫠**")
        return
    delcaption(int(message.chat.id))
    await message.reply_text("**😶‍🌫️ Your caption successfully deleted ✅**")
    await asyncio.sleep(5)  # Wait for 5 seconds
    await message.delete()

@Client.on_message(filters.private & filters.command('view_caption'))
async def view_caption(client, message):
    caption = find(int(message.chat.id))[1]
    if caption:
        msg = await message.reply_text(
            f"<b><u>Your Caption:</b></u>\n\n`{caption}`",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Delete Caption", callback_data="delete_caption")]
            ])
        )
        await asyncio.sleep(5)  # Wait for 5 seconds
        await message.delete()
        await msg.delete()
    else:
        await message.reply_text("**You don't have any custom caption**")
        await asyncio.sleep(5)  # Wait for 5 seconds
        await message.delete()

@Client.on_message()
async def handle_message(client, message):
    await asyncio.sleep(5)  # Wait for 5 seconds
    await message.delete()

@Client.on_callback_query()
async def handle_callbacks(client, callback_query):
    if callback_query.data == "delete_caption":
        await delete_caption(client, callback_query)
    elif callback_query.data == "view_caption":
        await view_caption(client, callback_query)
    await asyncio.sleep(5)  # Wait for 5 seconds
    await callback_query.message.delete()

async def main():
    # Create your Pyrogram client and start it
    client = Client("session_name")
    await client.start()
    await client.run()

if __name__ == '__main__':
    asyncio.run(main())
