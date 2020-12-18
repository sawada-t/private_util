import unittest
from utils.batch_util import BatchUtility
from datetime import datetime, timedelta

class TestBatchUtility(unittest.TestCase):
  def setUp(self):
    self.tgt = BatchUtility()

  def tearDown(self):
    del self.tgt

  def test_for_each_times(self):
    l = []
    self.tgt.for_each_times(
      datetime.strptime('2020-12-1 00:00:00', '%Y-%m-%d %H:%M:%S'),
      datetime.strptime('2020-12-1 00:06:00', '%Y-%m-%d %H:%M:%S'),
      dt = timedelta(minutes=3),
      f = lambda t: l.append(t.strftime('%Y-%m-%d %H:%M:%S')))
    self.assertEqual(l, ['2020-12-01 00:00:00', '2020-12-01 00:03:00', '2020-12-01 00:06:00'])

  def test_for_each_days(self):
    l = []
    self.tgt.for_each_days(
      datetime.strptime('2020-12-1 05:00:00', '%Y-%m-%d %H:%M:%S'),
      datetime.strptime('2020-12-3 05:00:00', '%Y-%m-%d %H:%M:%S'),
      lambda t: l.append(t.strftime('%Y-%m-%d %H:%M:%S'))
    )
    self.assertEqual(l, ['2020-12-01 05:00:00', '2020-12-02 05:00:00', '2020-12-03 05:00:00'])

    l = []
    self.tgt.for_each_days(
      datetime.strptime('2020-12-1 05:00:00', '%Y-%m-%d %H:%M:%S'),
      datetime.strptime('2020-12-3 00:00:00', '%Y-%m-%d %H:%M:%S'),
      lambda t: l.append(t.strftime('%Y-%m-%d %H:%M:%S'))
    )
    self.assertEqual(l, ['2020-12-01 05:00:00', '2020-12-02 05:00:00'])

