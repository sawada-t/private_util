#!/usr/bin/env python

import MySQLdb

class MysqlUtility:

  def dbproc(
    user,
    passwd,
    host,
    db,
    f):
    conn = MySQLdb.connect(
      user=user,
      passwd=passwd,
      host=host,
      db=db,
      charset="utf8mb4")
    cur = conn.cursor()
    result = f(cur)
    cur.close
    conn.close
    return result

  def simple_query(
    field=['*'],
    table,
    join=[],
    where_and=[],
    limit=None,
    ):
    q = "select "
    q += ', '.join(field)
    q += " from " + table + " "

    def join_statement(e):
      cond = ' AND '.join(e.on_and)
      f"join {e.table} on {cond} "
    q += ' '.join(map(join_statement, join))

    if where_and:
      q += 'WHERE ' + ' '.join(where)

    if limit:
      q += f"limit {limit}"

    return q

class AfternoonProductionMysqlUtility(MysqlUtility):
  def dbproc(f):
    return super().dbproc(
      user='matching',
      passwd='Iu5W735S2oJ',
      host='matching-prd-aurora-cluster.cluster-cxltz3ekvlyr.ap-northeast-1.rds.amazonaws.com',
      db='matching'
      f=f)

class AfternoonStageMysqlUtility(MysqlUtility):
  def dbproc_afternoon_stg(f):
    return self.dbproc(
      user='matching',
      passwd='Xi10!Wpnt7hu',
      host='matching-stg-aurora-cluster.cluster-csvrigkze2fw.ap-northeast-1.rds.amazonaws.com',
      db='matching'
      f=f)

