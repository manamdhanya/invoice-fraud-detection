import pytesseract
from PIL import Image
import io

try:
    from pdf2image import convert_from_bytes
    PDF_AVAILABLE = True
except:
    PDF_AVAILABLE = False


def extract_text(file_bytes):

    # Detect PDF
    if file_bytes[:4] == b"%PDF":

        if not PDF_AVAILABLE:
            return "PDF processing not available on server. Please upload image."

        try:
            images = convert_from_bytes(file_bytes)
            text = ""

            for img in images:
                text += pytesseract.image_to_string(img) + "\n"

            return text

        except Exception as e:
            print("PDF ERROR:", e)
            return "Error processing PDF. Try uploading image."

    # Otherwise → image
    try:
        image = Image.open(io.BytesIO(file_bytes))
        return pytesseract.image_to_string(image)

    except Exception as e:
        print("IMAGE ERROR:", e)
        return "Error processing image."