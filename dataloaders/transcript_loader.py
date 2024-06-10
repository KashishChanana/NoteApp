from langchain_community.document_loaders import YoutubeLoader
from dataloaders.base_loader import BaseLoader

class YouTubeLoader(BaseLoader):

    def load(self, youtube_url: str):
        try:
            loader = YoutubeLoader.from_youtube_url(youtube_url, add_video_info=False)
        except Exception as e:
            raise RuntimeError("Unable to load youtube video from the given URL.")
        print(f"Loaded YouTube URL: {youtube_url}")
        return loader.load()
    