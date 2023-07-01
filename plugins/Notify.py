import os
import datetime
import random
import time
import InlineKeyboardButton, InlineKeyboardMarkup
import Updater, CallbackQueryHandler

# Generating a random restart time between 2 and 16 minutes, and 0 to 59 seconds
restart_time_minutes = random.randint(2, 16)
restart_time_seconds = random.randint(0, 59)
restart_time = datetime.timedelta(minutes=restart_time_minutes, seconds=restart_time_seconds)

# Telegram bot setup
bot_token = os.environ.get("TOKEN", "")
support_group_id = int(os.environ.get("GROUP_ID", ""))

updater = Updater(token=bot_token)
dispatcher = updater.dispatcher

# Restart flag
is_restarted = True

# Sending the restart message to the support group
def send_restart_message(update, context):
    restart_message = "⚡ Bot Restarted ⚡\n"
    restart_message += f"🥂 Time Taken: {restart_time_minutes} Minutes {restart_time_seconds} Seconds"

    # Create the button
    button = InlineKeyboardButton("🦋", callback_data="button_clicked")

    # Create the inline keyboard markup with the button
    reply_markup = InlineKeyboardMarkup([[button]])

    # Send the message with the button to the support group
    context.bot.send_message(chat_id=support_group_id, text=restart_message, reply_markup=reply_markup)

# Handler for button click event
def button_click_handler(update, context):
    query = update.callback_query
    if query.data == "button_clicked":
        query.answer()
        query.message.reply_text("Thanks for giving me a life! 🙏")

# Register the button click handler
button_click_handler = CallbackQueryHandler(button_click_handler)
dispatcher.add_handler(button_click_handler)

# Delay before sending the restart message
time.sleep(5)  # Adjust the delay as needed

# Check restart flag and send message
if is_restarted:
    send_restart_message(None, updater.dispatcher)

