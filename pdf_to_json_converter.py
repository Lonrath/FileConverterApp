import os
from PyPDF2 import PdfReader
from interfaces.converter_interface import IConverter

class PdfToJsonConverter(IConverter):
    """
    PDF'den JSON formatına dönüşüm yapan sınıf.
    """

    def convert(self, input_file: bytes) -> dict:
        # Temp klasörünü kontrol et ve oluştur
        os.makedirs("temp", exist_ok=True)

        # PDF dosyasını geçici olarak kaydet
        input_file_path = "temp/input_file.pdf"
        with open(input_file_path, "wb") as temp_pdf:
            temp_pdf.write(input_file)

        # PDF'yi oku ve metni çıkar
        reader = PdfReader(input_file_path)
        json_output = {}
        for page_num, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            json_output[f"page_{page_num}"] = text

        return json_output
