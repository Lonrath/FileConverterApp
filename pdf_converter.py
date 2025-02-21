import os

def pdf_to_word(pdf_file):
    """
    Basit bir PDF'den Word'e dönüşüm simülasyonu.
    Gerçek dönüşüm işlemi için bir PDF kütüphanesi entegre edilebilir.
    """
    # Yüklenen dosyayı bir temp klasörüne kaydet
    input_file_path = f"temp/{pdf_file.filename}"
    with open(input_file_path, "wb") as temp_file:
        temp_file.write(pdf_file.file.read())

    # Word dosyası yolunu simüle et
    word_file_path = input_file_path.replace(".pdf", ".docx")

    # Gerçek dönüşüm işlemi burada yapılacak (şimdilik simülasyon)
    with open(word_file_path, "w") as word_file:
        word_file.write("This is a simulated Word file converted from PDF.")

    return word_file_path
