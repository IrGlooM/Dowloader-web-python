import streamlit as st
import system


url = st.text_input("Input Your URL :")

if url.startswith("http://") or url.startswith("https://"):
    st.write("Valid URL")
    if st.button("Download Video"):
         system.download_video(url)
else:
    st.write("Invalid URL")