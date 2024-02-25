from datetime import datetime

import utils

wait_to = utils.get_timestamp_for_message_sending()
while True:
    if datetime.now() > wait_to:
        break

print("opa")
