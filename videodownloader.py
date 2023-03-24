from pytube import YouTube

# Prompt user for the video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object and get the highest resolution video
video = YouTube(url)
stream = video.streams.get_highest_resolution()

# Download the video to the current working directory
print("Downloading...")
stream.download()
print("Download complete!")