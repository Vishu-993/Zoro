import time
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

CMD = ["/"]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    # Calculate the elapsed time since the start
    current_time = time.time()
    elapsed_time = current_time - start_time

    # Convert elapsed_time to a human-readable format
    elapsed_time_formatted = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

    ping_value = await ping(_, message)

    # Create the inline keyboard with two buttons
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🔁 Follow 🔁", url="https://t.me/CinemaVenoOfficial"),
                InlineKeyboardButton("🦋 Support Channel 🦋", url="https://t.me/HexaSupportOfficial")
            ]
        ]
    )

    await message.reply_photo(
        photo="https://i.imgur.com/L0woBZF.jpeg",
        caption=f"┌─❖\n"
                f"│「 𝗛𝗶 👋 」\n"
                "└┬❖\n"
                 f"│✑ 𝙃𝙚𝙡𝙡𝙤, 🈂️{message.from_user.mention}\n"
                 f"│✑ 𝙈𝙮𝙨𝙚𝙡𝙛 📍 <a href=https://t.me/Zoro_Renamer_bot>ʐօʀօ</a>\n"
                 f"│✑ A bot developed by <a href=https://t.me/CinemaVenoOfficial>ᶜᵛᵒ</a>\n"
                 f"│✑ 𝙑𝙚𝙧𝙨𝙞𝙤𝙣: ♻️{get_bot_version()}\n"
                 f"│✑ 𝘽𝙤𝙩 𝙍𝙪𝙣𝙩𝙞𝙢𝙚: 🛰️{elapsed_time_formatted}\n"
                 "└───────────────┈ ⳹",
        reply_markup=keyboard
    )

def get_bot_version():
    # Replace with the code to fetch the bot version from wherever it's stored
    return "1.0.0"
    
    
# Start time of the bot
start_time = time.time()

# Function to get the bot runtime
def get_bot_runtime():
    current_time = time.time()
    elapsed_time = current_time - start_time
    return elapsed_time

# Example usage
runtime = get_bot_runtime()
print(f"Bot has been running for {runtime:.2f} seconds.")


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("Pinging....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pɪɴɢ\n{time_taken_s:.3f} ms")
    return time_taken_s
