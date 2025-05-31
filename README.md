# KSextract

Extract text from images, PDFs, and DOCX files using EasyOCR.

## Features

- **Extract text from PDF files** (including scanned and digital PDFs)
- Extract handwritten and printed text from images
- Extract text from DOCX documents
- Unified interface for multiple file types

## Installation

```bash
pip install KSextract
```
# Usage

```bash
from KSextract import extract_text

# Extract text from a PDF file
print(extract_text("sample.pdf"))

# Extract text from an image
print(extract_text("image.png"))

# Extract text from a DOCX file
print(extract_text("document.docx"))
```
# Supported Formats

Images: .jpg, .jpeg, .png, .bmp, .tiff
PDF: .pdf
Word: .docx
More Coming Soon..
