import os
import requests
import sys
import traceback

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
GOOD_MORNING_MESSAGE = os.environ.get(
    "GOOD_MORNING_MESSAGE",
    "@everyone Good morning! ☀️ Let's have a nice and productive week & make a bunch of money 💲 so we can spend it all on SKINS!",
)


def send_morning_message():
    message = GOOD_MORNING_MESSAGE

    payload = {"content": message}

    response = requests.post(
        WEBHOOK_URL,
        json=payload,
        headers={"Content-Type": "application/json"},
        timeout=10,
    )

    if response.status_code == 204 or response.status_code == 200:
        print("Successfully sent good morning message")
        exit(0)
    else:
        print("Failed to send good morning message")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
        exit(1)


if __name__ == "__main__":
    try:
        send_morning_message()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        traceback.print_exc()
        exit(1)
