import os
from PyPDF2 import PdfReader
from docx import Document
from interfaces.converter_interface import IConverter

class PdfToWordConverter(IConverter):
    """
    PDF'den Word'e dönüşüm yapan sınıf.
    """

    def convert(self, input_file: bytes) -> str:
        # Temp klasörünü kontrol et ve oluştur
        os.makedirs("temp", exist_ok=True)

        # PDF dosyasını geçici olarak kaydet
        input_file_path = "temp/input_file.pdf"
        with open(input_file_path, "wb") as temp_pdf:
            temp_pdf.write(input_file)

        # PDF'yi oku ve metni çıkar local
        reader = PdfReader(input_file_path)
        document = Document()
        for page in reader.pages:
            text = page.extract_text()
            if text:
                document.add_paragraph(text)

        # Çıkarılan metni Word dosyasına kaydet
        output_file_path = input_file_path.replace(".pdf", ".docx")
        document.save(output_file_path)

        return output_file_path
