#encoding: utf-8

import json

import MySQLdb

import gconf
import dbutils

SQL_VALIDATE_LOGIN_COLUMNS = ('id', 'name')

SQL_VALIDATE_LOGIN = 'select id, name from user where name = %s and password = md5(%s)'
SQL_USER_SAVE = 'insert into user(name, age, password) values(%s, %s, md5(%s))'

SQL_USER_LIST_COLUMNS = ('id', 'name', 'age')
SQL_USER_LIST = 'select id, name, age from user'

SQL_USER_BY_ID_COLUMNS = ('id', 'name', 'age')
SQL_USER_BY_ID = 'select id, name, age from user where id=%s'

SQL_USER_MODIFY = 'update user set name=%s, age=%s where id=%s'

SQL_VALIDATE_USER_MODIFY = 'select id from user where id != %s and name = %s'

SQL_USER_DELETE = 'delete from user where id = %s'


SQL_MACHINE_ROOM_COLUMNS = ('id', 'name', 'addr', 'ip_ranges')
SQL_MACHINE_ROOM_LIST = 'select id, name, addr, ip_ranges from machine_room'

SQL_MACHINE_ROOM_SAVE = 'insert into machine_room(name, addr, ip_ranges) values(%s, %s, %s)'
SQL_MACHINE_ROOM_DELETE = 'delete from machine_room where id=%s'

SQL_ASSET_LIST_COLUMNS = 'id,sn,hostname,os,ip,machine_room_id,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,status'.split(',')
SQL_ASSET_LIST = 'select id,sn,hostname,os,ip,machine_room_id,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,status from asset where status!=2;'

SQL_ASSET_BY_ID = 'select id,sn,hostname,os,ip,machine_room_id,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,status from asset where status!=2 and id=%s;'
def get_users():
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)

    cursor = conn.cursor()

    cursor.execute(SQL_USER_LIST)
    rt_list = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return [dict(zip(SQL_USER_LIST_COLUMNS, line)) for line in rt_list]


def validate_login(username, password):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)

    cursor = conn.cursor()

    cursor.execute(SQL_VALIDATE_LOGIN, (username, password))
    rt = cursor.fetchone()
    cursor.close()
    conn.close()

    return None if rt is None else dict(zip(SQL_VALIDATE_LOGIN_COLUMNS, rt))


def validate_user_save(username, password, age):
    if username.strip() == '':
        return False, 'username is empty'
    if len(username.strip()) > 25:
        return False, 'username len is not gt 25'
    if password.strip() == '':
        return False, 'password is empty'
    if len(password.strip()) < 6 or len(password.strip()) > 25:
        return False, 'password len is between 6 and 25'

    if not str(age).isdigit() or int(age) < 1 or int(age) > 100:
        return False, 'age is not a between 1 and 100 integer'

    return True, ''


def user_save(username, password, age):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)

    cursor = conn.cursor()

    cnt = cursor.execute(SQL_USER_SAVE, (username, age, password))
    conn.commit()
    cursor.close()
    conn.close()
    return cnt != 0


def get_user_by_id(uid):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)

    cursor = conn.cursor()
    cursor.execute(SQL_USER_BY_ID, (uid,))
    rt = cursor.fetchone()
    cursor.close()
    conn.close()

    return {} if rt is None else dict(zip(SQL_USER_BY_ID_COLUMNS, rt))


def validate_user_modify(uid, username, age):
    if not get_user_by_id(uid):
        return False, 'user is not found'
    if username.strip() == '':
        return False, 'username is empty'
    if len(username.strip()) > 25:
        return False, 'username len is not gt 25'
    if not str(age).isdigit() or int(age) < 1 or int(age) > 100:
        return False, 'age is not a between 1 and 100 integer'

    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)

    cursor = conn.cursor()
    

    cnt = cursor.execute(SQL_VALIDATE_USER_MODIFY, (uid, username.strip()))
    cursor.close()
    conn.close()
    if cnt != 0:
        return False, 'username is same to other'

    return True, ''


def user_modify(uid, username, age):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)

    cursor = conn.cursor()

    cnt = cursor.execute(SQL_USER_MODIFY, (username, age, uid))
    conn.commit()
    cursor.close()
    conn.close()
    return True


def user_delete(uid):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)

    cursor = conn.cursor()

    cnt = cursor.execute(SQL_USER_DELETE, (uid, ))
    conn.commit()
    cursor.close()
    conn.close()
    return True
    return True

def get_machine_rooms():
    rt_cnt, rt_list = dbutils.execute_sql(SQL_MACHINE_ROOM_LIST, (), True)
    return [dict(zip(SQL_MACHINE_ROOM_COLUMNS, rt)) for rt in rt_list]

def validate_machine_room_save(name, addr, ip_ranges):
    if name.strip() == '' or addr.strip() == '' or ip_ranges.strip() == '':
        return False, 'name, addr, ip_ranges is empty'
    return True, ''

def machine_room_save(name, addr, ip_ranges):
    dbutils.execute_sql(SQL_MACHINE_ROOM_SAVE, (name, addr, ip_ranges), False)
    return True

def machine_room_delete(mrid):
    dbutils.execute_sql(SQL_MACHINE_ROOM_DELETE, (mrid, ), False)
    return True

def get_topn(src, topn=10):
    stat_dict = {}
    fhandler = open(src, "rb")

    for line in fhandler:
        line_list = line.split()
        key = (line_list[0], line_list[6], line_list[8])
        stat_dict[key] = stat_dict.setdefault(key, 0) + 1

    fhandler.close()

    result = sorted(stat_dict.items(), key=lambda x:x[1])
    return result[:-topn - 1:-1]

def get_assets():
    rt_cnt, rt_list = dbutils.execute_sql(SQL_ASSET_LIST, (), True)
    assets = []
    for rt in rt_list:
        asset = dict(zip(SQL_ASSET_LIST_COLUMNS, rt))
        for key in 'time_on_shelves,over_guaranteed_date'.split(','):
            if asset[key]:
                asset[key] = asset[key].strftime('%Y-%m-%d')
        assets.append(asset)
    return assets

def get_asset_by_id(aid):
    rt_cnt, rt_list = dbutils.execute_sql(SQL_ASSET_BY_ID, (aid,), True)
    assets = []
    for rt in rt_list:
        asset = dict(zip(SQL_ASSET_LIST_COLUMNS, rt))
        for key in 'time_on_shelves,over_guaranteed_date'.split(','):
            if asset[key]:
                asset[key] = asset[key].strftime('%Y-%m-%d')
        assets.append(asset)
    return assets[0] if assets else {}

if __name__ == '__main__':
    for i in xrange(100):
        user_save('name-%s' % i, '123456', 29)