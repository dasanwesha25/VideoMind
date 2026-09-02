import whisper
import json

model = whisper.load_model("base")

# model = whisper.load_model("large") could have been used for better accuracy but it is slower and requires more resources and more space. The base model is a good trade-off between speed and accuracy.

result = model.transcribe(audio = "audio/Tutorial 3 _ 3.Stack overflow video.mp3",
                          language = "hindi",
                          task = "translate",
                          word_timestamps=False
                          )
# print(result["text"])    #prints the text of the audio file in the target language (English in this case)

# print (result)   #print the entire result dictionary which contains the text, segments, and other information about the transcription.

# print(result["segments"])    #prints the segments of the audio file with their start and end times and the text of each segment.
 
chunks = []

for segment in result["segments"]:
    chunks.append({"start":segment["start"], "end":segment["end"], "text":segment["text"]})

print(chunks)

with open("output.json", "w") as f:
    json.dump(chunks,f)