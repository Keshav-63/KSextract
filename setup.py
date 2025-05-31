from setuptools import setup, find_packages

setup(
    name="KSextract",
    version="0.1.0",
    description="Extract text from PDF files (including scanned PDFs), images (handwritten/printed), and DOCX documents using EasyOCR.",
    author="Keshav Suthar",
    author_email="keshavdv241@gmail.com",
    packages=find_packages(),
    install_requires=[
        "easyocr",
        "pdf2image",
        "numpy",
        "Pillow",
        "python-docx"
    ],
    python_requires=">=3.7",
    url="https://github.com/Keshav-63/KSextract",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)