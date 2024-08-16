import yt_dlp
import tkinter as tk
from tkinter import filedialog

def downloader(url, save_path):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',  # Download best quality audio
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save with the video title
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("Music downloaded successfully.")
    except Exception as e:
        print(f"Error: {e}")

def open_file_dialogue():
    folder = filedialog.askdirectory()
    if folder:
        print(f'Selected folder: {folder}')
    return folder

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    song_url = input('Please enter a YouTube URL: ')
    save_dir = open_file_dialogue()

    if save_dir:
        print("Started download...")
        downloader(song_url, save_dir)
    else:
        print('Invalid save location.')

downloader(song_url, save_dir)


