import streamlit as st
from pytube import YouTube

def download_video(url):
    yt = YouTube(url)
    #st.image(yt.thumbnail_url)
    video = yt.streams.get_highest_resolution()
    st.write(video)

url = st.text_input("Enter Youtube URL")
resolution = st.selectbox("Quality : ",['1080p','720p','480p','360p','144',])
if st.button("Show details :"):
    download_video(url,resolution)
