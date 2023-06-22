import math
import time


class ProgressBar:
    def __init__(self, total, width=40):
        self.total = total
        self.width = width

    def update(self, progress):
        filled_length = math.ceil(self.width * progress / self.total)
        empty_length = self.width - filled_length
        bar = '█' * filled_length + '░' * empty_length
        percentage = round(progress / self.total * 100, 2)
        progress_bar = f'[{bar}] {percentage}%'
        return progress_bar


async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start,
    cancel_button=False
):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = ProgressBar(total)
        progress_bar = progress.update(current)

        tmp = "╭━━━━❰ PROGRESS BAR ❱━➣\n" + \
              f"┣⪼ 🗂️ : {humanbytes(current)} | {humanbytes(total)}\n" + \
              f"┣⪼ ⏳️ : {round(percentage, 2)}%\n" + \
              f"┣⪼ 🚀 : {humanbytes(speed)}/s\n" + \
              f"┣⪼ ⏱️ : {elapsed_time} / {estimated_total_time}\n" + \
              f"┣⪼ {progress_bar}\n"

        if cancel_button:
            tmp += "┣⪼ ❌ Cancel"
        else:
            tmp += "┣⪼ ⏹️ Cancel"

        try:
            await message.edit(
                text="{}\n{}".format(ud_type, tmp)
            )
        except:
            pass


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
          ((str(milliseconds) + "ms, ") if
