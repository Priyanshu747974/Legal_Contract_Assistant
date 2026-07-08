from app.core.interfaces.pdf_parser import PDFparserInterface
from app.core.model.parsed_document import ParsedDocument
# pyrefly: ignore [missing-import]
from pypdf import PdfReader
# pyrefly: ignore [missing-import]
import pdfplumber 
# pyrefly: ignore [missing-import]
import fitz 
import os

class PyPDFParser(PDFparserInterface):
    # now decide what parse() should do
    def parse(self, pdf_path: str) -> ParsedDocument:

        extracted_text = self._extract_text(pdf_path)
        extracted_tables = self._extract_tables(pdf_path)
        extracted_images = self._extract_images(pdf_path)

        document_payload = ParsedDocument(
            text=extracted_text,
            tables=extracted_tables,
            images=extracted_images
        )
        return document_payload

    def _extract_text(self, pdf_path: str)->str:    
                   
        reader = PdfReader(pdf_path) 
        all_pages_text = [] 
        for page in reader.pages: 
            text = page.extract_text() 
            if text: all_pages_text.append(text) 
        combined_text = "\n".join(all_pages_text)

        return combined_text
    
    def _extract_tables(self, pdf_path: str)->list:
        
        all_tables = []
        with pdfplumber.open(pdf_path)as pdf:
            for page in pdf.pages:
                tables=page.extract_tables()
                if tables:
                    all_tables.extend(tables)
        return all_tables
    
    def _extract_images(self, pdf_path: str) -> list[str]:
        image_paths = []
        pdf = fitz.open(pdf_path)

        output_folder = "extracted_images"
        os.makedirs(output_folder, exist_ok=True)

        for page_number in range(len(pdf)):
            page = pdf.load_page(page_number)
            images = page.get_images(full=True)
            for image_index, image in enumerate(images):
                xref = image[0]
                image_data = pdf.extract_image(xref)
                image_bytes = image_data["image"]
                image_extension = image_data["ext"]
                image_name = (
                    f"page_{page_number + 1}_image_{image_index + 1}.{image_extension}"
                )
                image_path = os.path.join(output_folder, image_name)
                with open(image_path, "wb") as image_file:
                    image_file.write(image_bytes)
                image_paths.append(image_path)

        pdf.close()
        return image_paths

    