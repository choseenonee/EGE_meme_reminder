import os
import random
from datetime import datetime

from telethon.sync import TelegramClient
from dotenv import load_dotenv

import utils

# TODO: docker, test if script sleeps even

load_dotenv()

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')

phone_number = os.getenv('PHONE_NUMBER')

receiver = os.getenv('RECEIVER')

client = TelegramClient('session_name', api_id, api_hash)
client.start(phone=phone_number)

# test message on startup
client.send_message(receiver, message="123")

while True:
    wait_to = utils.get_timestamp_for_message_sending()
    message = utils.get_message(random.randint(0, 100))
    print("waiting to ", wait_to, "with message:", message)
    while True:
        if datetime.now() > wait_to:
            break
    message = message.replace("[оставшееся время]", utils.compute_remaining_time())
    client.send_message(receiver, message=message)
