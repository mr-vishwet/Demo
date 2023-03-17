import streamlit as st
from pytube import YouTube

def download_video(url, resolution):
    yt = YouTube(url)
    #st.image(yt.thumbnail_url)
    st.write(" Title : "+yt.title)
    streams = yt.streams.filter(progressive=True, file_extension='mp4', res=resolution)
    st.write(streams)
    if streams:
        stream = streams.order_by('resolution').desc().first()
        st.write(stream)

url = st.text_input("Enter Youtube URL")
resolution = st.selectbox("Quality : ",['1080p','720p','480p','360p','144',])
if st.button("Show details :"):
    download_video(url,resolution)
