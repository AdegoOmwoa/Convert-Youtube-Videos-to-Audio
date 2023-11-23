import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import VideoFileClip

def convert_video_to_audio():
    try:
        video_url = url_entry.get()

        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        status_label.config(text=f"Downloading '{yt.title}'...")
        video_path = f"{output_path}/{yt.title}.mp4"
        video_stream.download(output_path)

        # Convert video to audio using moviepy
        clip = VideoFileClip(video_path)
        audio = clip.audio
        audio_path = f"{output_path}/{yt.title}.mp3"
        audio.write_audiofile(audio_path)

        status_label.config(text=f"Conversion complete. Audio saved to: {audio_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        status_label.config(text="Error occurred")

# Create the main window
window = tk.Tk()
window.title("YouTube Video to Audio Converter")

# Create and pack the widgets
url_label = ttk.Label(window, text="Enter YouTube Video URL:")
url_label.pack(pady=5)

url_entry = ttk.Entry(window, width=40)
url_entry.pack(pady=5)

convert_button = ttk.Button(window, text="Convert to Audio", command=convert_video_to_audio)
convert_button.pack(pady=10)

status_label = ttk.Label(window, text="")
status_label.pack(pady=5)

# Set the output path (change as needed)
output_path = "C:/Users/Priest/Video"

# Run the Tkinter event loop
window.mainloop()
