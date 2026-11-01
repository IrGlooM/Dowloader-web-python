import streamlit as st
import system

st.title("Downloader Video\n")

url = st.text_input("Input Your URL :")

if url.startswith("http://") or url.startswith("https://"):
    st.write("Valid URL")
    if st.button("Download Video"):
         system.download_video(url)
elif url == None :
    st.write("URL None")
else:
    st.write("Invalid URL")
