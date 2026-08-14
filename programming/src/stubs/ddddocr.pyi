"""Type stubs for ddddocr - OCR library for CAPTCHA recognition."""

class DdddOcr:
    def __init__(
        self,
        show_ad: bool = True,
        det: bool = False,
        ocr: bool = True,
        import_onnx_path: str = "",
        charsets_path: str = "",
    ) -> None: ...
    def classification(self, img: bytes, png_fix: bool = False) -> str: ...
    def detection(self, img: bytes) -> list[list[int]]: ...
