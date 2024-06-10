from dataloaders.transcript_loader import YouTubeLoader
from models.model_factory import ModelFactory
from tasks.task_factory import TaskFactory

class Workflow():
    def run(self, youtube_url:str, model:str, task:str):
        self.youtube_url = youtube_url
        self.model = ModelFactory.get_model(model).get_client()
        self.task = TaskFactory.get_task(task)

        transcript = YouTubeLoader().generate_transcript(youtube_url=youtube_url)
        return self.task.execute(model=self.model, context=transcript)
        

        




