import base64
import zlib
import logging
import requests
from bs4 import BeautifulSoup

from app.models.requests import POBUrlRequest

logger = logging.getLogger(__name__)


class BuildParser:
    def __init__(self, url: POBUrlRequest | str):
        self.url = url

    def __decode_xml_from_import_code(self, import_code: str) -> str:
        """Декодирует и распаковывает код импорта Path Of Building (POB)."""
        try:
            base64_decode = base64.urlsafe_b64decode(import_code)
            decompressed_xml = zlib.decompress(base64_decode)
            return decompressed_xml.decode('utf-8')
        except (TypeError, ValueError):
            logger.exception("Ошибка декодирования.")
            raise
        except zlib.error:
            logger.exception("Ошибка декомпрессии.")
            raise

    def fetch_xml_from_url(self, timeout: float = 6.0) -> str:
        """Получает и обрабатывает URL с pastebin.com."""
        if self.url.startswith("https://pastebin.com/"):
            raw = self.url.replace("https://pastebin.com/", "https://pastebin.com/raw/")
            try:
                request = requests.get(raw, timeout=timeout)
                request.raise_for_status()
                return self.__decode_xml_from_import_code(request.text)
            except requests.RequestException as e:
                logger.exception(f"Ошибка при запросе к {self.url}: {e}")
                raise
        else:
            logger.exception(f"{self.url} не является допустимым URL для pastebin.com.")
            raise ValueError("Недопустимый URL.")

    def get_xml_from_pobb(self) -> str:
        """Получает импортированный код Path of Building с pobb.in."""
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            textarea = soup.find('textarea')
            if textarea:
                return self.__decode_xml_from_import_code(textarea.text)
            else:
                logger.error('Тег <textarea> не найден.')
                raise ValueError('Тег <textarea> не найден.')
        else:
            logger.error(f'Ошибка загрузки страницы: {response.status_code}')
            raise ValueError(f'Ошибка загрузки страницы: {response.status_code}')
