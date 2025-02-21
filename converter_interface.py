from abc import ABC, abstractmethod


class IConverter(ABC):
    """
    Tüm dönüştürücüler için temel arayüz.
    """

    @abstractmethod
    def convert(self, input_file: bytes) -> str:
        """
        Dosya dönüşüm işlemini gerçekleştirir.

        Args:
            input_file (bytes): Girdi dosyası (örneğin, PDF içeriği).

        Returns:
            str: Dönüştürülen dosyanın yolu.
        """
        pass
