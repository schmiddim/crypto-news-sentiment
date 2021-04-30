import basc_py4chan
import json

from config.db import conn

"""
Extract data from 4chan.org/biz 
"""

b = basc_py4chan.Board('biz')

for thread_id in b.get_all_thread_ids():
    thread = b.get_thread(thread_id)
    ids = b.get_all_thread_ids()
    try:
        replies = [{'comment': thread.topic.text_comment, 'date': thread.topic.datetime}]

        for reply in thread.replies:  # type: basc_py4chan.Post
            # print(reply.text_comment, reply.datetime)

            replies.append({'comment': reply.text_comment, 'date': reply.datetime})

        json_data = json.dumps(replies, default=str)
        sql = """REPLACE   INTO threads 
                    (date_modified, date_created_4chan,date_last_modified_4chan, thread_id, topic, replies) 
                    VALUES (current_timestamp(), %s, %s,%s,%s, %s);
            """
        cur = conn.cursor()
        cur.execute(sql, [thread.topic.datetime, replies[-1].get("date"), thread_id, thread.topic.text_comment, json_data])
        conn.commit()
    except Exception as e:
        print("thread id  {}".format(thread_id))
        print(e)
