from tasks.base_task import BaseTask
from models.client import BaseClient
from tokenizer import recursive_char_splitter
from langchain.docstore.document import Document
from dataloaders.prompt_loader import _load_prompt
from tasks.summary_task import SummaryTask

class BlogTask(BaseTask):
    def __init__(self):
        self.blog = ""
        self.blog_prompt = _load_prompt(self.__class__.__name__)
    
    def get_dependent_task(self):
        return SummaryTask()

    def execute(self, model:BaseClient, context:str):
        _, summary = self.get_dependent_task().execute(model=model, context=context)
        doc =  Document(page_content=summary, metadata={"source": "local"})
        summary_splits = recursive_char_splitter.split_text([doc], chunk_overlap=0)
        for split in summary_splits:
            response = model.generate(self.blog_prompt, split.page_content)
            self.blog += response.choices[0].message.content

        return summary_splits, self.blog
    