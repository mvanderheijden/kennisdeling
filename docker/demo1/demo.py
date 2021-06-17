import time

while True:
    print("Hello world")
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        exit(1)
