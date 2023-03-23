import time


def countdown(unix_timestamp):
    target_unix_timestamp = unix_timestamp
    current_unix_timestamp = int(time.time())

    while current_unix_timestamp < target_unix_timestamp:
        print(target_unix_timestamp - current_unix_timestamp)
        time.sleep(1)
        current_unix_timestamp = int(time.time())

    print("Happy New Year!")


countdown(1679539560)
