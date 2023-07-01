import time
import os
import telegram

BOT_TOKEN = int(os.environ.get("TOKEN", ""))
GROUP_CHAT_ID = int(os.environ.get("GROUP_ID", ""))

def bot_restarted():
    print("⚡ Bot Restarted ⚡")
    start_time = time.time()
    # Your bot's initialization or startup code here
    # ...
    # ...

    end_time = time.time()
    runtime = end_time - start_time
    print(f"🥂 Runtime: {runtime:.2f} seconds")

    time.sleep(10)  # Add a 10-second delay before sending the message

    bot = telegram.Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=GROUP_CHAT_ID, text=f"⚡ Bot Restarted ⚡\n🥂 Runtime: {runtime:.2f} seconds")

def main():
    bot_restarted()
    # Add any additional startup code here
    # ...
    # ...

    # Rest of your bot's logic
    # ...

if __name__ == '__main__':
    main()
