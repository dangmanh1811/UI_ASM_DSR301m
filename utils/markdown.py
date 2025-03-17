import streamlit as st
import base64
from config import *

def centered_subheader(text):
    st.markdown(f"<h3 style='text-align: center;'>{text}</h3>", unsafe_allow_html=True)
    
def centered_title(text):
    st.markdown(f"<h1 style='text-align: center;'>{text}</h1>", unsafe_allow_html=True)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def add_background():
# Add background
	img_base64 = get_base64(BACKGROUND_IMG_PATH)
	page_bg_img = f'''
	<style>
	.stApp {{
	background-image: url("data:image/jpg;base64,{img_base64}");
	background-size: cover;
	background-position: center;  /* Đặt background ở vị trí trung tâm */
	background-repeat: no-repeat;  /* Không lặp lại background */
	}}
	</style>
	'''
	st.markdown(page_bg_img, unsafe_allow_html=True)