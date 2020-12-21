import unittest
from unittest import mock
from privutils.mysql_util import MysqlUtility

mocked_close = mock.Mock()
mocked_commit = mock.Mock()
mocked_cursor_init = mock.Mock()
mocked_cursor_close = mock.Mock()
mocked_execute = mock.Mock()

class MockConnection:
  def close(self):
    mocked_close()

  def cursor(self):
    class MockCursor:
      def __init__(self):
        mocked_cursor_init()

      def close(self):
        mocked_cursor_close()

      def execute(self, query):
        mocked_execute(query)
    return MockCursor()

  def commit(self):
    mocked_commit()

def mocked_connect(*args, **kwargs):
  return MockConnection()



class TestMysqlUtilityMeta(unittest.TestCase):
  def setUp(self):
    mocked_close.reset_mock()
    mocked_commit.reset_mock()
    mocked_cursor_init.reset_mock()
    mocked_cursor_close.reset_mock()
    mocked_execute.reset_mock()

  @mock.patch('MySQLdb.connect', side_effect=mocked_connect)
  def test_meta(self, mocked_connect):
    db = MysqlUtility('user1', 'password2', 'host3', 'db4')
    mocked_connect.assert_called_once_with(
        user='user1',
        passwd='password2',
        host='host3',
        db='db4',
        charset="utf8mb4")
    mocked_close.assert_not_called()
    del db
    mocked_close.assert_called_once()



class TestMysqlUtility(unittest.TestCase):
  @mock.patch('MySQLdb.connect', side_effect=mocked_connect)
  def setUp(self, mocked_connect):
    self.tgt = MysqlUtility('user1', 'password2', 'host3', 'db4')
    mocked_close.reset_mock()
    mocked_commit.reset_mock()
    mocked_cursor_init.reset_mock()
    mocked_cursor_close.reset_mock()
    mocked_execute.reset_mock()

  def tearDown(self):
    del self.tgt

  def test_dbproc(self):
    mocked_cursor_init.assert_not_called()
    mocked_execute.assert_not_called()
    mocked_commit.assert_not_called()
    mocked_cursor_close.assert_not_called()

    self.tgt.dbproc(lambda db_cur: db_cur.execute('test_query'))
    mocked_cursor_init.assert_called_once()
    mocked_execute.assert_called_once_with('test_query')
    mocked_commit.assert_called_once()
    mocked_cursor_close.assert_called_once()

  def test_select_query(self):
    self.assertEqual(
        MysqlUtility.simple_select(
            table='table1',
            field=['*'],
            join=[],
            where_and=[],
            limit=None),
        'select * from table1;')
    self.assertEqual(
        MysqlUtility.simple_select(
            table='t1',
            field=['t1.id1, t1.id2'],
            join=[{'table': 't2', 'on_and': ['t1.id1=t2.uid', 't1.id2=t2.pid']}],
            where_and=['t1.id1>10', 't2.pid>10'],
            limit=3),
        'select t1.id1, t1.id2 from t1 left join t2 on t1.id1=t2.uid AND t1.id2=t2.pid WHERE t1.id1>10 AND t2.pid>10 limit 3;')

  def test_insert_query(self):
    self.assertEqual(
        MysqlUtility.simple_insert(
            table='t1',
            values={'id': 1, 'name': 'freemason'}),
        "insert into t1 (id, name) values ('1', 'freemason');")

  def test_delete_query(self):
    self.assertEqual(
        MysqlUtility.simple_delete(
            table='t1',
            where_and=['id>10', 'id<20']),
        "delete from t1 WHERE id>10 AND id<20;")

