import os
import json
from utils.message import Message

HISTORY_DIR = "data/history"

def get_history_path(key): 
    os.makedirs(HISTORY_DIR, exist_ok=True)
    return os.path.join(HISTORY_DIR, f"{key}.json")

def save_channel_history(key, history):
    path = get_history_path(key)
    with open(path, "w", encoding="utf-8") as f:
        json.dump([msg.to_dict() for msg in history], f, indent=2)

def load_channel_history(key):
    path = get_history_path(key)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                return [Message.from_dict(d) for d in json.load(f)]
            except Exception:
                return []
    return []

def wipe_channel_history(key):
    path = get_history_path(key)
    if os.path.exists(path):
        os.remove(path)