from fastapi import APIRouter, File, UploadFile, HTTPException
from services.pdf_to_word_converter import PdfToWordConverter
from services.pdf_to_json_converter import PdfToJsonConverter
from services.pdf_to_image_converter import PdfToImageConverter
from services.pdf_to_excel_converter import PdfToExcelConverter

router = APIRouter()

# PdfToWordConverter sınıfını kullan
word_converter = PdfToWordConverter()

@router.post("/convert/word")
async def convert_to_word(file: UploadFile = File(...)):
    """
    PDF'den Word dosyasına dönüşüm yapan endpoint.
    """
    # Sadece PDF dosyalarını kabul et
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    try:
        # Dönüşüm işlemini çağır
        converted_file_path = word_converter.convert(file.file.read())

        return {
            "message": "File converted successfully!",
            "converted_file": converted_file_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during file conversion: {str(e)}")


# PdfToJsonConverter sınıfını kullan
json_converter = PdfToJsonConverter()

@router.post("/convert/json")
async def convert_to_json(file: UploadFile = File(...)):
    """
    PDF'den JSON formatına dönüşüm yapan endpoint.
    """
    # Sadece PDF dosyalarını kabul et
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    try:
        # JSON dönüşüm işlemini çağır
        json_result = json_converter.convert(file.file.read())
        return {
            "message": "File converted successfully!",
            "result": json_result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during conversion: {str(e)}")

image_converter = PdfToImageConverter()

@router.post("/convert/image")
async def convert_to_image(file: UploadFile = File(...), format: str = "jpg"):
    """
    PDF'den görüntü (JPG/PNG) formatına dönüşüm yapan endpoint.
    """
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    if format not in ["jpg", "png"]:
        raise HTTPException(status_code=400, detail="Only 'jpg' and 'png' formats are supported.")

    try:
        output_files = image_converter.convert(file.file.read(), output_format=format)
        return {
            "message": "File converted successfully!",
            "converted_files": output_files
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during conversion: {str(e)}")


excel_converter = PdfToExcelConverter()

@router.post("/convert/excel")
async def convert_to_excel(file: UploadFile = File(...)):
    """
    PDF'den Excel'e dönüşüm yapan endpoint.
    """
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    try:
        output_file = excel_converter.convert(file.file.read())
        return {
            "message": "File converted successfully!",
            "converted_file": output_file
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during conversion: {str(e)}")