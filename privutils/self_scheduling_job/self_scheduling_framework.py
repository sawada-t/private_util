import os
from abc import ABCMeta, abstractmethod
import datetime
import fcntl

class SelfSchedulingFramework(metaclass=ABCMeta):
  task_storage = None

  def __init__(self, task_storage, success_handler, failure_handler):
    self.task_storage = task_storage
    self.success_handler = success_handler
    self.failure_handler = failure_handler

  def __exclusive_execution(self, f):
    name = os.path.basename(__file__)
    f_lock = open(f"/var/run/{name}.lock", "w")
    fcntl.flock(f_lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    result = f()
    fcntl.flock(f_lock.fileno(), fcntl.LOCK_UN)
    f_lock.close()
    return result

  @abstractmethod
  def _do(self, task):
    pass

  def put(self, task):
    self.task_storage.put(task)

  def finish_tasks(self):
    def f():
      tc = datetime.datetime.now()
      lt = self.task_storage.put_out(tc)
      while lt:
        for t in lt:
          try:
            self._do(t)
            self.success_handler(t)
          except Exception as e:
            self.failure_handler(t, e)
        lt = self.task_storage.put_out(tc)
    self.__exclusive_execution(f)

