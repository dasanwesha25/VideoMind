# coverts the video to mp3
import os
import subprocess

files = os.listdir("video")
print(files)

for file in files:
    tutorial_number = file.split(" [")[1].split("]")[0]
    file_name = file.split(" .")[0].split(" [")[0]
    print(tutorial_number, " | ", file_name)
    subprocess.run(["ffmpeg", "-i", f"video/{file}", f"audio/{tutorial_number} _ {file_name}.mp3"])