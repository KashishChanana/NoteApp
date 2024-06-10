from models.client import Client
from tasks.base_task import BaseTask

class KeyConceptsTask(BaseTask):
    def execute(self, model:Client, context:str):
        pass
    
    def get_dependent_task(self):
        pass

    def get_prompt(self):
        pass
    
