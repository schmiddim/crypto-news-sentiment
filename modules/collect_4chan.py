import basc_py4chan


def fetch_thread(thread_id):
    b = basc_py4chan.Board('biz')
    thread = b.get_thread(thread_id)
    replies = [{'comment': thread.topic.text_comment, 'date': thread.topic.datetime}]
    for reply in thread.replies:  # type: basc_py4chan.Post
        # print(reply.text_comment, reply.datetime)
        replies.append({'comment': reply.text_comment, 'date': reply.datetime})

    op_subject = thread.topic.subject
    if thread.topic is not None and thread.topic.text_comment !='':
        op_comment = thread.topic.text_comment
    else:
        op_comment = op_subject

    return thread, replies, op_comment


