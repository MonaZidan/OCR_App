# LIBs
import io 
import cv2
import numpy as np
import streamlit as st
from PIL import Image
import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Specify the path to the Tesseract and prevent potential errors

# Image to text fun

def image_to_text(img,lang="eng"):
    text = pytesseract.image_to_string(img, lang=lang)
    return text

# Streamlit UI

## Title
st.title("OCR Application")
st.write("**Text Extraction with Tesseract OCR!** ")
st.write("Upload an image and Tesseract will extract the text for you.It's fast, reliable,and accurate—perfect for converting printed content into editable text.")

### About OCR technology
st.sidebar.header("What is OCR ?")
st.sidebar.write("""Optical Character Recognition (OCR) is a technology that automatically extracts text from images and converts it into a machine-readable format.""")
st.sidebar.header("How it works ?")
st.sidebar.write("""OCR involves several steps to accurately recognize and extract text from images:
                 
1-Image Preprocessing
                 
2-Text Detection
                 
3-Character Recognition
                 
4-Post-Processing
""")

## Image upload

input_img = st.file_uploader("Please upload your image :",type=["png","jpg","gif","tiff","webp","jpeg"])

## Lang selection

language = st.selectbox("Please select the language :",["Arabic", "English", "Spanish", "Arabic and English","Arabic and Spanish", "English and Spanish","Arabic , English and Spanish"])

if language == "Arabic":
    language = "ara"

elif language == "English":
    language = "eng"

elif language == "Spanish":
    language = "spa"

elif language == "Arabic and English":
    language = "ara+eng"

elif language == "Arabic and Spanish":
    language = "ara+spa"

elif language == "English and Spanish":
    language = "eng+spa"

else :
    language = "ara+spa+eng"

## Output text

if input_img is not None:
    img = Image.open(input_img)
    st.image(img,use_container_width=True)
    st.header("The extracted text is : ")

    with st.spinner("Text Extraction ....."):
        text = image_to_text(img, language)
        lines = text.splitlines()
        for line in lines:
            st.write(line)


        ## Saving extracted text

        if text.strip():
            text2byte = io.BytesIO(text.encode())

            st.download_button(
                label="Download Extracted Text as .txt File",
                data=text2byte,
                file_name="extracted_text.txt",
                mime="text/plain"
            )
        else:
            st.warning("No text extracted from the image.")

