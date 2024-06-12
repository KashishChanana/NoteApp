from dataloaders.base_loader import BaseLoader
from langchain_community.document_loaders import UnstructuredURLLoader

class WebLoader(BaseLoader):

    def load(self, url:str):
        try:
            loader = UnstructuredURLLoader(urls=[url])
        except Exception as e:
            raise RuntimeError(f"Unable to extract data from the given URL {url} \n {e}")
        return loader.load()
