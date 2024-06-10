
class BaseTask():
    def get_prompt(self):
        raise NotImplementedError("This method should be overridden.")
    
    def get_dependent_task(self):
        raise NotImplementedError("This method should be overridden.")
    
    def execute(self):
        raise NotImplementedError("This method should be overridden.")
    