import streamlit as slt
from PIL import Image
import cv2 
from pytesseract import image_to_string
import numpy as np

file = slt.file_uploader("Please select a file to upload", type=['png', 'jpg'])

if file is not None:
    image_bytes = file.getvalue()
    decoded = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
    text = slt.text_area("The translated text: \n", image_to_string(decoded))
    