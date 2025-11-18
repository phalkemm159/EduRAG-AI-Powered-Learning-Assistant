import whisper
import json

model = whisper.load_model("large-v2").to("cuda")

result = model.transcribe(audio = "audios/output.mp3", 
                          language="hi", 
                          task="translate",
                          word_timestamps=False)

# print(result)
# print(result[segments])
chunks = []
for segment in result["segments"]:
    chunks.append({
        "start": segment["start"],
        "end": segment["end"],
        "text": segment["text"]
    })

print(chunks)

with open("output.json", "w") as f:
    json.dump(chunks ,f)

