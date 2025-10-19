#     __    __
#  o-''))____\\
#  "--__/ * * * )
#  c_c__/-c____/
#
# 🛑 Do not read this script — the contents are forbidden.
# The answers lie not in the code, but in the clues you've been given.
# Resist the urge. Proceed as instructed by the ASCII Dogs. 👁️

import time
import urllib.request
import sys
import base64

# --- Password Protection ---
ENCODED_PASSWORD = b'Q1ZFLTIwMjUtNTc3NjA='

def download_reward():
    """Downloads the reward file after successful authentication."""
    reward_url = "https://raw.githubusercontent.com/ndouglas-cloudsmith/offsite-scripts/refs/heads/main/reward1.txt"
    save_as = "reward1.txt"
    try:
        print("\n📥 Downloading your reward file...")
        urllib.request.urlretrieve(reward_url, save_as)
        print(f"✅ Reward downloaded as '{save_as}'!")
    except Exception as e:
        print(f"❌ Failed to download the reward: {e}")

def password_protected():
    """Prompts the user for a password and checks it against the decoded version."""
    print("🚪 To access the first fragment, you need to provide the unfixed CVE ID associated with the newly-created pod")
    user_input = input("Password: ")

    DECODED_PASSWORD = base64.b64decode(ENCODED_PASSWORD).decode('utf-8')

    if user_input == DECODED_PASSWORD:
        print("✅ Access granted! You found the correct flag. Click next at the bottom right corner of the page to proceed.")
        time.sleep(1)
        download_reward()
    else:
        print("❌ Incorrect flag. Access denied.")
        time.sleep(2)
        sys.exit(1)

if __name__ == "__main__":
    password_protected()
