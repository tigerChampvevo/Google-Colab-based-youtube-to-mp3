import yt_dlp as youtube_dl
from google.colab import files
import os

# Function to download YouTube video
def download_youtube_video(url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'video.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Replace with your YouTube URL
youtube_url = 'https://www.youtube.com/watch?v=Fw3RB7xnb80'
output_file = 'video.wav'

# Download the video and extract audio
download_youtube_video(youtube_url, output_file)

# Rename the file if it has a double extension
if os.path.exists('video.wav.wav'):
    os.rename('video.wav.wav', 'video.wav')

# Check if the file exists
if os.path.exists(output_file):
    # Download the file
    files.download(output_file)
else:
    print(f"File {output_file} not found.")
