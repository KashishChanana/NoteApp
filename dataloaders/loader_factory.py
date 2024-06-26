
from dataloaders.pdf_loader import PDFLoader
from dataloaders.transcript_loader import YouTubeLoader
from dataloaders.web_loader import WebLoader

class DataLoaderFactory:
    _loaders = {
        "YouTubeURL": YouTubeLoader,
        "FileUpload": PDFLoader,
        "WebURL": WebLoader
    }

    @staticmethod
    def get_dataloader(upload_type:str):
        loader_class = DataLoaderFactory._loaders.get(upload_type)
        if loader_class is None:
            raise ValueError(f"Model '{loader_class}' not recognized")
        return loader_class()