from dotenv import find_dotenv, load_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

class BaseClient():
    def get_client():
        raise NotImplementedError("This method should be overridden.")
    
    def generate(self, prompt:str, context:str):
        raise NotImplementedError("This method should be overridden.")
