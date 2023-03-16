import appdirs
import os
import streamlit as st

# Get the path to the user's application data directory
app_data_dir = appdirs.user_data_dir()

# Append the name of the Google Chrome download folder to the path
chrome_download_dir = os.path.join(
    app_data_dir, "Google", "Chrome", "User Data", "Default", "Downloads")

# Print the Google Chrome download folder path
st.write("Download Folder : "+chrome_download_dir)
