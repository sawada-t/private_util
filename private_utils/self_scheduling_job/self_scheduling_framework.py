import os
from abc import ABCMeta, abstractmethod
import datetime

class SelfSchedulingFramework(metaclass=ABCMeta):
  task_storage = None

  def __init__(self, task_storage):
    self.task_storage = task_storage

  def __exclusive_execution(self, f):
    name = os.path.basename(__file__)
    f_lock = open(f"/var/run/{name}.lock", "w")
    fcntl.flock(f_lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    result = f()
    fcntl.flock(f_lock.fileno(), fcntl.LOCK_UN)
    f_lock.close()
    return result

  @abstractmethod
  def __do(self, task):
    pass

  def put(self, task):
    self.task_storage.put(task)

  def finish_tasks(self):
    def f():
      tc = datetime.now()
      lt = self.task_storage.put_out(tc)
      while lt:
        map(self.__do, lt)
        lt = self.task_storage.put_out(tc)
    self.__exclusive_execution(f)

