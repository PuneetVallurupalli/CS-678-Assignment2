import PyPDF2
import requests
from gentopia.tools.basetool import *

class PDFReaderArgs(BaseModel):
    pdf_url: str = Field(..., description="The URL of the PDF file")

class PDFReader(BaseTool):
    name = "pdf_reader"
    description = "Reads a PDF file from a URL and returns its text content"

    args_schema: Optional[Type[BaseModel]] = PDFReaderArgs

    def _run(self, pdf_url: str) -> str:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.get(pdf_url, headers=headers)
            response.raise_for_status()  # Check for HTTP errors
            
            with open("temp.pdf", 'wb') as f:
                f.write(response.content)

            with open("temp.pdf", 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                return text[:500] + "..."  # Return the first 500 characters as a summary
        except Exception as e:
            return f"Error downloading or reading PDF: {str(e)}"

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

