from pymongo import MongoClient

import json


with open('db_config.json') as config_f:
    conf = json.load(config_f)

from datetime import datetime

timeformat = "%Y-%m-%d_%H:%M:%S"

def timeparse(timestring: str):
    return datetime.strptime(timestring, timeformat)

def timestamp() -> str:
    return datetime.now().strftime(timeformat)

client = MongoClient(conf['mongo_db_url'])

sessions = client[conf['mongo_db_name']].sessions

def push_snapshot(session):
    try:
        state = session.history[-1]
        position = session.progress[state]
    except:
        current = None
    else:
        current = f"{state}:{position}"

    session_state = {
        'history': session.history,
        'progress': session.progress,
        'vars': session.var._data
    }

    session_snapshot = {
             'time': timestamp(),
             'current': current,
             'players_number': hasattr(session, 'players') and len(session.players)
            }

    sessions.update_one(
        {"chat_id": session.chat_id},
        {"$push": {'snapshots': session_snapshot},
         "$set": {'state': session_state}},
        upsert=True)