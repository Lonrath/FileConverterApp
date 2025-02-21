import os
import pandas as pd
from PyPDF2 import PdfReader
from interfaces.converter_interface import IConverter

class PdfToExcelConverter(IConverter):
    """
    PDF'den Excel (XLSX) formatına dönüşüm yapan sınıf.
    """

    def convert(self, input_file: bytes) -> str:
        """
        PDF'deki metni okuyarak Excel'e çevirir.

        :param input_file: PDF dosyasının byte içeriği
        :return: Oluşturulan XLSX dosyasının yolu
        """
        # Temp klasörünü oluştur
        os.makedirs("temp", exist_ok=True)

        # PDF'yi geçici olarak kaydet
        input_file_path = "temp/input_file.pdf"
        with open(input_file_path, "wb") as temp_pdf:
            temp_pdf.write(input_file)

        # PDF'den metni çıkar
        reader = PdfReader(input_file_path)
        data = []
        for page_num, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            if text:
                for line in text.split("\n"):
                    data.append([f"Page {page_num}", line])  # Sayfa numarasını da ekliyoruz

        # Pandas DataFrame'e dönüştür
        df = pd.DataFrame(data, columns=["Page", "Text"])

        # Excel dosyasını oluştur
        output_file_path = "temp/output.xlsx"
        df.to_excel(output_file_path, index=False, engine="openpyxl")

        return output_file_path
