import pytesseract
from PIL import Image
import io

# Try importing PDF support
try:
    from pdf2image import convert_from_bytes
    PDF_AVAILABLE = True
except:
    PDF_AVAILABLE = False


def extract_text(file_bytes):

    # 📄 Detect PDF
    if file_bytes[:4] == b"%PDF":

        if not PDF_AVAILABLE:
            return "PDF not supported on server"

        try:
            images = convert_from_bytes(file_bytes)
            text = ""

            for img in images:
                text += pytesseract.image_to_string(img) + "\n"

            if not text.strip():
                return "PDF processed but no text found"

            return text

        except Exception as e:
            print("PDF ERROR:", e)
            return "PDF processing failed"


    try:
        image = Image.open(io.BytesIO(file_bytes))
        text = pytesseract.image_to_string(image)

        if not text.strip():
            return "OCR failed: no text detected"

        return text

    except Exception as e:
        print("IMAGE ERROR:", e)
        return "OCR failed: tesseract not available on server"