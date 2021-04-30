import basc_py4chan
import json
from modules.collect_4chan import fetch_thread
from config.db import conn

"""
Extract data from 4chan.org/biz 
"""

b = basc_py4chan.Board('biz')
for thread_id in b.get_all_thread_ids():
    thread, replies, op_comment = fetch_thread(thread_id)
    json_data = json.dumps(replies, default=str)

    sql = """REPLACE   INTO threads 
                (date_modified, date_created_4chan,date_last_modified_4chan, thread_id, topic, replies) 
                VALUES (current_timestamp(), %s, %s,%s,%s, %s);
        """
    cur = conn.cursor()
    cur.execute(sql, [thread.topic.datetime, replies[-1].get("date"), thread_id, op_comment, json_data])
    conn.commit()
