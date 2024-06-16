from langchain.docstore.document import Document
from pypdf import PdfReader
from dataloaders.base_loader import BaseLoader


class PDFLoader(BaseLoader):
    def load(self, pdf: str):
            try:
                pdf_reader = PdfReader(pdf)
                content = ""
                for page in pdf_reader.pages:
                    content += page.extract_text()
                documents = [Document(page_content=content, metadata={"source": "local"})]
            except Exception as e:
                raise RuntimeError(f"Unable to read PDF. {e}")
            return documents