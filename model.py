#创建表，插入数据
def createtable():
    import pymysql
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='666',
        database='db1',
        charset='utf8'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''
        -- 创建表
        create table userinfo(id int primary key auto_increment,username char(20) not null unique,password char(20) not null);
        -- 插入数据
        insert into userinfo(username,password) values('chao','666'),('sb1','222');
    '''
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
