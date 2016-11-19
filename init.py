#encoding: utf-8

if __name__ == '__main__':
    import gconf
    import dbutils
    with open('mysql.sql', 'rb') as h:
        sql = h.read()
        dbutils.execute_sql(sql, (), False)

    rt = dbtuils.execute_sql('select count(*) from user where name=%s', ('kk',), True)
    if rt and rt[0] == 0:
        dbutils.execute_sql('insert into user(`name`, `password`, `age`) values(%s, md5(%s), %s)', ('kk', '123456', 29), False)
