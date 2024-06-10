from tasks.base_task import BaseTask
from models.client import BaseClient
from tokenizer import recursive_char_splitter
from dataloaders.prompt_loader import _load_prompt

class SummaryTask(BaseTask):
    def __init__(self):
        self.summary = ""
        self.summary_prompt = _load_prompt(self.__class__.__name__)

    def execute(self, model:BaseClient, context:str):
        """
        Generates a summary from the context using the model.

        Args:
            model (Client): The generative model to use.
            context (str): The context to generate the summary from.

        Returns:
            str: The generated summary.
        """
        try:
            splits = recursive_char_splitter.split_text(context)
            for text in splits:
                generated_response = model.generate(self.summary_prompt, text.page_content)
                self.summary += generated_response.choices[0].message.content
            return self.summary
        except Exception as e:
            raise RuntimeError(f"Error executing summary task: {e}")