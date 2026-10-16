import sys
import os
import requests

f = sys.argv[1]
t = os.environ["TG_TOKEN"]
c = os.environ["TG_CHAT"]

if os.path.getsize(f) > 49_000_000:
    requests.post(
        f"https://api.telegram.org/bot{t}/sendMessage",
        data={
            "chat_id": c,
            "text": f"Archivo muy grande: {os.path.basename(f)}"
        }
    )
else:
    with open(f, "rb") as fh:
        requests.post(
            f"https://api.telegram.org/bot{t}/sendDocument",
            data={"chat_id": c},
            files={"document": fh},
            timeout=300
        )
