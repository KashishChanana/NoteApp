from db import PineconeDB
from models.model_factory import ModelFactory
from tasks.task_factory import TaskFactory
from dataloaders.loader_factory import DataLoaderFactory

class Workflow():

    def __init__(self) -> None:
        self.vector_db = PineconeDB()
        
    def run(self, input_io:str, model:str, task:str, upload_type:str):
        self.model = ModelFactory.get_model(model_name=model)
        self.task = TaskFactory.get_task(task_name=task)
        self.loader = DataLoaderFactory.get_dataloader(upload_type=upload_type)

        context = self.loader.load(input_io)
        return self.task.execute(model=self.model, context=context)

    def save(self, documents:str):
        self.vector_db.upsert(documents=documents)
    