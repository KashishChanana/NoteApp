from dataloaders.prompt_loader import _load_prompt
from db import PineconeDB
from models.client import BaseClient
from tasks.base_task import BaseTask

class QATask(BaseTask):
    def __init__(self):
        self.qa_prompt = _load_prompt(self.__class__.__name__)
        self.db = PineconeDB()

    def expand_prompt(self, retrieved_content, question:str):
        self.qa_prompt = f"{self.qa_prompt} {retrieved_content} \n Question: {question}"
    
    def execute(self, model:BaseClient, question:str):
        retrieved_content = self.db.retrieve(question=question)
        self.expand_prompt(retrieved_content=retrieved_content, question=question)
        response = model.generate(self.qa_prompt, question)
        return None, response.choices[0].message.content
    