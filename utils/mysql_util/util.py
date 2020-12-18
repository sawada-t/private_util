#!/usr/bin/env python

import MySQLdb

class MysqlUtility:
  def __init__(self, user, passwd, host, db):
    self.conn = MySQLdb.connect(
      user=user,
      passwd=passwd,
      host=host,
      db=db,
      charset="utf8mb4")

  def __del__(self):
    if getattr(self, 'conn', None):
      self.conn.close()

  def dbproc(self, f):
    cur = self.conn.cursor()
    result = f(cur)
    self.conn.commit()
    cur.close()
    return result

  @classmethod
  def simple_select(
    cls,
    table,
    field=['*'],
    join=[],
    where_and=[],
    limit=None,
    ):
    q = "select "
    q += ', '.join(field)
    q += " from " + table

    def join_statement(e):
      table = e['table']
      cond = ' AND '.join(e['on_and'])
      return f" left join {table} on {cond}"
    q += ' '.join(map(join_statement, join))

    if where_and:
      q += ' WHERE ' + ' AND '.join(where_and)

    if limit:
      q += f" limit {limit}"

    q += ';'
    return q

  @classmethod
  def simple_insert(cls, table, values={}):
    k = ', '.join(list(values.keys()))
    v = ', '.join(map(lambda e: f"'{e}'", list(values.values())))
    return f"insert into {table} ({k}) values ({v});"

  @classmethod
  def simple_delete(cls, table, where_and=[]):
    q = f"delete from {table}"
    if where_and:
      q += ' WHERE ' + ' AND '.join(where_and)
    q += ';'
    return q

