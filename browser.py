import streamlit as st
import requests
import os
import base64




# Define GitHub repository URL and PDF file name
REPO_URL = "https://github.com/mr-vishwet/Demo"
PDF_FILE = "blockchain.pdf"
PDF_PATH = os.path.join(os.getcwd(), PDF_FILE)

# Define function to download PDF file from GitHub repository


def download_pdf():
    pdf_url = f"{REPO_URL}/blob/main/{PDF_FILE}?raw=true"
    st.write("File URL : ",pdf_url)
    response = requests.get(pdf_url)
    pdf_data = response.content
    st.write("Remote File Path : ",PDF_PATH)
    with open(PDF_PATH, "wb") as f:
        f.write(pdf_data)

# Define Streamlit app

st.title("PDF Viewer")

# Download PDF file from GitHub repository
download_pdf()
# st.write(PDF_PATH)
# with fitz.open(PDF_PATH) as doc:
#     for page in doc:
#         st.image(page.getPixmap().tobytes(), use_column_width=True)
    
if os.path.isfile(PDF_PATH):
    with open(PDF_PATH, "rb") as f:
        pdf_bytes = f.read()

    if pdf_bytes:
        data_url = f"data:application/pdf;base64,{base64.b64encode(pdf_bytes).decode()}"
        #st.write("Data_url : ", data_url)
        st.write(" Showing PDF in PDF Viewer ")
        st.markdown(f'<iframe src="{data_url}" allowfullscreen allow="autoplay; encrypted-media; picture-in-picture" style="width:100%; height:800px;" frameborder="0"></iframe>', unsafe_allow_html=True)


