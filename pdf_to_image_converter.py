import fitz  # PyMuPDF
import os


class PdfToImageConverter:
    def convert(self, input_file: bytes, output_format: str = "jpg") -> list:
        if output_format not in ["jpg", "png"]:
            raise ValueError("Only 'jpg' and 'png' formats are supported.")

        # Temp klasörünü oluştur
        os.makedirs("temp", exist_ok=True)

        # PDF'yi aç
        pdf_document = fitz.open("pdf", input_file)

        output_files = []
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap()
            output_file_path = f"temp/page_{page_num + 1}.{output_format}"
            pix.save(output_file_path)
            output_files.append(output_file_path)

        return output_files
