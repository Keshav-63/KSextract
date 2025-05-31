import easyocr
from pdf2image import convert_from_path
import numpy as np
from PIL import Image
import docx
import os

def extract_text_from_image(image_path, lang='en'):
    reader = easyocr.Reader([lang])
    result = reader.readtext(image_path, detail=0)
    return "\n".join(result)

def extract_text_from_pdf(pdf_path, lang='en'):
    reader = easyocr.Reader([lang])
    images = convert_from_path(pdf_path)
    text = []
    for img in images:
        result = reader.readtext(np.array(img), detail=0)
        text.extend(result)
    return "\n".join(text)

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(file_path, lang='en'):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']:
        return extract_text_from_image(file_path, lang)
    elif ext == '.pdf':
        return extract_text_from_pdf(file_path, lang)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")