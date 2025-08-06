# poll_loop.py

import schedule
import time
from main import main

def start_polling():
    print("🔁 Starting phishing scanner polling (every 1 minute)...")
    schedule.every(1).minutes.do(main)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("🛑 Polling stopped by user.")

if __name__ == "__main__":
    start_polling()
