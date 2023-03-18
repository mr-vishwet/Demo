import streamlit as st
import requests
from io import BytesIO
import base64

# Define GitHub repository URL and PDF file name
REPO_URL = "https://github.com/mr-nani/Demo"
PDF_FILE = "blockchain.pdf"

# Define function to download PDF file from GitHub repository
def download_pdf():
    pdf_url = f"{REPO_URL}/blob/main/{PDF_FILE}?raw=true"
    response = requests.get(pdf_url)
    pdf_data = BytesIO(response.content)
    return pdf_data

# Define Streamlit app
def main():
    st.title("PDF Viewer")

    # Download PDF file from GitHub repository
    pdf_data = download_pdf()

    # Display PDF file contents
    pdf_base64 = base64.b64encode(pdf_data.read()).decode("utf-8")
    pdf_display = f'<embed src="data:application/pdf;base64,{pdf_base64}" width="100%" height="600px"/>'
    st.markdown(pdf_display, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

