# OCR Application

This is an OCR (Optical Character Recognition) application built using Tesseract and Streamlit. The application allows users to upload images and extract text from them using Tesseract OCR.

## Features

- Upload images in various formats (PNG, JPG, GIF, TIFF, WEBP, JPEG)
- Select the language for text extraction (Arabic, English, Spanish, or combinations)
- Display the extracted text
- Download the extracted text as a `.txt` file

## Installation

1. Clone the repository:

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Install Tesseract OCR and the required language packs :

    ```sh
    sudo apt-get install tesseract-ocr tesseract-ocr-eng tesseract-ocr-ara tesseract-ocr-spa
    ```

## Usage

1. Run the Streamlit application:

    ```sh
    streamlit run OCR.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload an image, select the language, and view the extracted text.

or Try the app live here:

[Open OCR App](https://optical-character-recognition-app.streamlit.app/)

