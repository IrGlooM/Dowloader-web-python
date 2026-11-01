import io
import streamlit as st
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from pathlib import Path 



def download_video(url):

    download_folder = Path.home() / "Downloads"


    
    try:
      ydl_opts = {
            "format": "best",  # Ambil kualitas terbaik
            "outtmpl": "%(id)s.%(ext)s",
        }

        with YoutubeDL(ydl_opts) as ydl:
          # Ambil info video dulu
          info = ydl.extract_info(url_input, download=True)
          filename = ydl.prepare_filename(info)

        # Baca file yang sudah didownload ke memory
        with open(filename, "rb") as f:
          video_bytes = f.read()

        # Hapus file fisik dari server supaya tidak memenuhi penyimpanan server
        Path(filename).unlink(missing_ok=True)

        st.success("Video berhasil diproses! Silakan klik tombol di bawah:")

        # Tampilkan tombol download agar terunduh ke HP/Laptop *pengguna*
        st.download_button(
            label="📥 Download Video ke Perangkat Anda",
            data=video_bytes,
            file_name=f"{info.get('title', 'video')}.mp4",
            mime="video/mp4",
        )
 
    except DownloadError:
        st.error(
            "Gagal mendownload. Periksa kembali URL YouTube Anda apakah"
            " valid/bisa diakses."
        )
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
