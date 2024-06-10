from models.openai import OpenAI

class ModelFactory:
    _models = {
        "GPT-3.5": OpenAI,
    }

    @staticmethod
    def get_model(model_name):
        model_class = ModelFactory._models.get(model_name)
        if model_class is None:
            raise ValueError(f"Model '{model_name}' not recognized")
        return model_class()
    