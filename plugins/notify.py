import os
import datetime
import random
import time
import asyncio
from pyrogram import Client

# Generating a random restart time between 2 and 16 minutes, and 0 to 59 seconds
restart_time_minutes = random.randint(2, 16)
restart_time_seconds = random.randint(0, 59)
restart_time = datetime.timedelta(minutes=restart_time_minutes, seconds=restart_time_seconds)

# Telegram bot setup
bot_token = os.environ.get("TOKEN", "")
support_group_id = int(os.environ.get("GROUP_ID", ""))

# Restart flag
is_restarted = True

# Create an instance of the bot
bot = Client("my_bot", bot_token=bot_token)

# Sending the restart message to the support group
async def send_restart_message():
    restart_message = "⚡ Bot Restarted ⚡\n"
    restart_message += f"🥂 Time Taken: {restart_time_minutes} Minutes {restart_time_seconds} Seconds"

    await bot.send_message(chat_id=support_group_id, text=restart_message)

# Delay before sending the restart message
time.sleep(5)  # Adjust the delay as needed

# Check restart flag and send message
async def main():
    if is_restarted:
        await bot.start()
        await send_restart_message()
        await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
