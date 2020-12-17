#!/usr/bin/env python

import datetime

class BatchUtility:
  def __init__(self):
    pass

  def __date_iterator_generator(begin, end, dt):
    date_cursor = begin
    while date_cursor <= end:
      yield date_cursor
      date_cursor += dt

  def for_each_times(begin, end, dt, f):
    date_cursor = begin
    return map(
      lambda d: f(d),
      self.__date_iterator_generator(begin, end, dt))

  def for_each_days(begin, end, f):
    delta = datetime.timedelta(days=1)
    return self.for_each_times(begin, end, delta, f)

