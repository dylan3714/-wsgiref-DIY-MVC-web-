
#对用户名和密码进行验证
def auth(username,password):
    import pymysql
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        database='db1',
        charset='utf8'
    )
    print('userinfo',username,password)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from userinfo where username=%s and password=%s;'
    res = cursor.execute(sql, [username, password])
    if res:
        return True
    else:
        return False
