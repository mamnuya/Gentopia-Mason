from typing import AnyStr
from googlesearch import search
from gentopia.tools.basetool import *

import requests
from pypdf import PdfReader
import io

class PDFReaderArgs(BaseModel):
    url: str = Field(..., description="a url to PDF")


class PDFReader(BaseTool):
    """Tool that adds the capability to read PDFs."""

    name = "pdf_reader"
    description = ("A tool to read from PDFs."
                   "Input should be a pdf url.")

    args_schema: Optional[Type[BaseModel]] = PDFReaderArgs

    def _run(self, url: AnyStr) -> str:
        response = requests.get(url)
        
        if response.status_code != 200:
            return "Please check PDF URL."
        
        # Read the PDF content
        pdf_content = io.BytesIO(response.content)
        pdf_text = ""
        
        try:
            reader = PdfReader(pdf_content)
            for page in reader.pages:
                pdf_text += page.extract_text()
                
            return pdf_text
        
        except Exception as e:
            return f"An error occurred while reading the PDF {str(e)}"

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    ans = PDFReader()._run("Attention for transformer")
    print(ans)

