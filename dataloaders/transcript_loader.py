from langchain.document_loaders import YoutubeLoader
from dataloaders.loader import Loader

class YouTubeLoader(Loader):

    def load(self, youtube_url: str):
        try:
            loader = YoutubeLoader.from_youtube_url(youtube_url, add_video_info=False)
        except Exception as e:
            raise RuntimeError("Unable to load youtube video from the given URL.")
        print(f"Loaded YouTube URL: {youtube_url}")
        return loader
    
    def generate_transcript(self, youtube_url:str):
        loader = self.load(youtube_url=youtube_url)
        return loader.load()