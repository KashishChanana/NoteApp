import datetime
import openai
import os
from models.client import Client

openai.api_key = os.environ['OPENAI_API_KEY']

class OpenAI(Client):

    def __init__(self):
        self.llm_model = self.get_model()
        self.client = openai.OpenAI()
    
    def generate(self, prompt:str, context:str):
        response = self.client.chat.completions.create(
            model=self.llm_model,
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": context
                }
            ]
        )
        return response

    def get_model(self):
        current_date = datetime.datetime.now().date()
        # Define the date after which the model should be set to "gpt-3.5-turbo"
        target_date = datetime.date(2024, 6, 12)
        if current_date > target_date:
            llm_model = "gpt-3.5-turbo"
        else:
            llm_model = "gpt-3.5-turbo-0301"
        
        return llm_model
    
    def get_client(self):
        return self