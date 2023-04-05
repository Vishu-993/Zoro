import math
import time


async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start
):

    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = get_progress_bar(percentage)

        tmp = "╭━━━━❰ PROGRESS BAR ❱━➣\n" + \
              f"┣⪼ 🗂️ : {humanbytes(current)} | {humanbytes(total)}\n" + \
              f"┣⪼ ⏳️ : {round(percentage, 2)}%\n" + \
              f"┣⪼ 🚀 : {humanbytes(speed)}/s\n" + \
              f"┣⪼ ⏱️ : {estimated_total_time}\n" + \
              f"╰━━━━━━━━━━━━━━━➣ {progress}"

        try:
            await message.edit(
                text="{}\n {}".format(
                    ud_type,
                    tmp
                )
            )
        except:
            pass


def get_progress_bar(percentage: float) -> str:
    filled = math.floor(percentage / 5)
    empty = 20 - filled
    return "[{0}{1}]".format(
            ''.join(["●" for i in range(filled)]),
            ''.join(["○" for i in range(empty)])
        )


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]
