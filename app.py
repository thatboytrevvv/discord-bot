import os
import requests

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]


def send_morning_message():
    message = "@everyone Good morning! ☀️ Let's have a nice and productive week & make a bunch of money 💲 so we can spend it all on SKINS!"

    payload = {"content": message}

    response = requests.post(
        WEBHOOK_URL, json=payload, headers={"Content-Type": "application/json"}
    )

    if response.status_code == 204 or response.status_code == 200:
        print("Successfully sent good morning message")
    else:
        print("Failed to send good morning message")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
        exit(1)


if __name__ == "__main__":
    send_morning_message()
