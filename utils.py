from datetime import datetime, timedelta
import random
import os


def get_timestamp_for_message_sending():
    day = int(os.getenv("EGE_DAY"))
    random_delta = int(os.getenv("RANDOM_PERIOD")) * 24 * 60 * 60

    now = datetime.now()

    target_date = datetime(2024, 5, day, 10, 0, 0)

    delta = target_date - now

    random_delta_seconds = random.randint(min(24*60*60, int(delta.total_seconds())),
                                          min(random_delta, int(delta.total_seconds())))
    # random_delta_seconds = random.randint(30, 35)

    wait_time = timedelta(seconds=random_delta_seconds)

    wait_to = now + wait_time

    return wait_to


def compute_remaining_time():
    day = int(os.getenv("EGE_DAY"))

    now = datetime.now()

    target_date = datetime(2024, 5, day, 10, 0, 0)

    delta = target_date - now

    total_days = delta.days

    total_hours = delta.total_seconds() // 3600

    weeks = total_days // 7
    days = total_days % 7

    remaining_hours = total_hours % 24

    return f"{weeks} НЕДЕЛЬ, {days} ДНЕЙ, {remaining_hours} ЧАСОВ."


def get_message(num: int) -> str:
    f = open("messages.txt", 'r', encoding='utf-8')
    messages = f.read().split("\n")
    f.close()
    return messages[num]


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    # compute_remaining_time()
    # print(get_timestamp_for_message_sending())
    print(get_message(100))