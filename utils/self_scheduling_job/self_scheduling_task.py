
class SelfSchedulingTask():
  function_id = ""
  params = {}
  execute_time = None

  def __init__(
    self,
    function_id,
    params,
    execute_time):
    self.function_id = function_id
    self.params = params
    self.execute_time = execute_time

