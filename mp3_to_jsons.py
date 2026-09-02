import whisper
import json
import os

model = whisper.load_model("base")

os.makedirs("jsons", exist_ok=True)    #That creates the folder if it's missing and does nothing if it already exists (exist_ok=True prevents an error on reruns).
audios = os.listdir("audio")

for audio in audios:
    number = audio.split(".")[0].split("_")[1]
    title = audio.split(".")[1]
    print(number, title)

    result = model.transcribe(f"audio/{audio}", 
                              fp16=False, 
                              language="hi",
                              task = "translate",
                              word_timestamps = False)

    chunks = []
    for segment in result["segments"]:
        chunks.append({"number": number, "title": title, "start":segment["start"], "end":segment["end"], "text":segment["text"]})

    chunks_with_metadata = {"chunks": chunks, "text": result["text"]}

    with open(f"jsons/{audio}.json", "w") as f:
        json.dump(chunks_with_metadata, f)