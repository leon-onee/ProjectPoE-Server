from app.models.build_model import BuildModel


class BuildController:
    @staticmethod
    def get_xml_from_url(url: str):
        """Получает XML из URL (pastebin или pobb)."""
        if "pastebin.com" in url:
            return BuildModel.fetch_xml_from_url(url)
        elif "pobb.in" in url:
            return BuildModel.get_base64_from_pobb(url)
        else:
            raise ValueError("Поддерживаются только URL с pastebin.com и pobb.in")
