import pymysql


def get_all_threads(conn: pymysql.connect):
    sql = """SELECT * FROM threads WHERE 1"""

    cur = conn.cursor()
    cur.execute(sql, [])
    return cur.fetchall()


def store_rating(conn: pymysql.connect, result, reply_count, thread_id):
    sql = """REPLACE INTO ratings (thread_id, reply_count, has_results, top1, top2, top3, top4, top5, count1, count2,count3, count4, count5 )
            values (%s,%s,%s,%s,%s,%s,%s, %s, %s, %s, %s, %s, %s);
    
    """
    has_results = False
    top1 = None
    top2 = None
    top3 = None
    top4 = None
    top5 = None
    count1 = None
    count2 = None
    count3 = None
    count4 = None
    count5 = None

    if len(result) >= 1:
        has_results = True
        top1 = list(result.keys())[0]
        count1 = result.get(top1)
        if len(result) > 1:
            top2 = list(result.keys())[1]
            count2 = result.get(top2)
        if len(result) > 2:
            top3 = list(result.keys())[2]
            count3 = result.get(top3)
        if len(result) > 3:
            top4 = list(result.keys())[3]
            count4 = result.get(top4)
        if len(result) > 4:
            top5 = list(result.keys())[4]
            count5 = result.get(top5)
    cur = conn.cursor()
    cur.execute(sql, [thread_id,
                      reply_count,
                      has_results,
                      top1, top2, top3, top4, top5,
                      count1, count2, count3, count4, count5
                      ])
    conn.commit()
