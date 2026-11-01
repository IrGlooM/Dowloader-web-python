import streamlit as st
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from pathlib import Path 



def download_video(url):

    download_folder = Path.home() / "Downloads"


    
    try:
         with YoutubeDL({
                "outtmpl" : str(download_folder / "%(title)s.%(ext)s"),
         }) as ydl:
            ydl.download([url])
            st.write("Video downloaded successfully!")
    
    except DownloadError:
        st.write("Error downloading video. Please check the URL and try again.")

    except Exception :
        st.write("An unexpected error occurred. Please try again.")
