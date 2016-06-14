#!/usr/bin/python
#coding=utf-8
__author__ = 'linpelvis'

import sys

from impala.dbapi import connect
from impala.util import as_pandas

reload(sys)
getattr(sys, 'setdefaultencoding')('utf8')

class Impala(object):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._conn = connect(host=host ,port=port)

    def do_data(self, sentence, option):
        ''' execute sql sentence '''
        cursor = self._conn.cursor()
        cursor.execute(sentence)
        data = cursor.fetchall() if option else cursor.fetchone()
        cursor.close()
        return data
    
    def cursor(self, sentence, option):
        ''' execute sql sentence '''
        cursor = self._conn.cursor()
        cursor.execute(sentence)
        return cursor

def main():
    HOST='127.0.0.1'
    PORT=21050
    SQL = 'select * from xxx limit 1'
    try:
        impala_cli = Impala(HOST, PORT)
        cur = impala_cli.cursor(SQL, True)
        df = as_pandas(cur)
        print df.test.describe()
    except Exception as e:
        print e.message;

if __name__ == "__main__":
    main()
