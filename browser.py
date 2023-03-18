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


def pdf_viewer(pdf_bytes):
    data_url = f"data:application/pdf;base64,{base64.b64encode(pdf_bytes).decode()}"
    st.markdown(
        f'<iframe src="{data_url}" width="800" height="1200" style="border: none;"></iframe>', unsafe_allow_html=True,)


# Define Streamlit app


def main():
    st.title("PDF Viewer")

    # Download PDF file from GitHub repository
    download_pdf()
    st.write(PDF_PATH)

    # Display PDF file contents as a PDF viewer
    if os.path.isfile(PDF_PATH):

        with open(PDF_PATH, "rb") as f:
            pdf_bytes = f.read()

        if pdf_bytes:
            data_url = f"data:application/pdf;base64,{base64.b64encode(pdf_bytes).decode()}"
            # st.write("Data_url : ", data_url)
            st.markdown(
                f'<iframe src="{data_url}" width="700" height="1000" style="border: none"></iframe>', unsafe_allow_html=True)

        else:
            st.write("Error while reading the file")


if __name__ == "__main__":
    main()
