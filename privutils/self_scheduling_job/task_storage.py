from abc import ABCMeta, abstractmethod

class TaskStorage(metaclass=ABCMeta):
  @abstractmethod
  def put(self, task):
    pass

  # fetch and delete
  @abstractmethod
  def put_out(self, current_time):
    pass

