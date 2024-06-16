from dataloaders.prompt_loader import _load_prompt
from models.client import BaseClient
from tasks.base_task import BaseTask

class QATask(BaseTask):
    def __init__(self):
        self.qa_prompt = _load_prompt(self.__class__.__name__)

    def expand_prompt(self, retrieved_content, question:str):
        self.qa_prompt = f"{self.qa_prompt} {retrieved_content} \"\"\" Question: {question}"
    
    def execute(self, model:BaseClient, question:str):
        return model.generate(self.expand_prompt, question)
    