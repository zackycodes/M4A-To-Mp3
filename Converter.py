from pydub import AudioSegment

# Replace 'input.m4a' with the path to your M4A file
m4a_file = AudioSegment.from_file("input.m4a", format="m4a")

# Replace 'output.mp3' with the desired output path and filename
# You can set the bitrate here, e.g., bitrate="192k"
m4a_file.export("output.mp3", format="mp3")

print("Conversion complete: output.mp3 created.")