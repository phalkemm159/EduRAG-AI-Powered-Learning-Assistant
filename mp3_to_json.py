import whisper 
import json
import os

os.makedirs("jsons", exist_ok=True)

model = whisper.load_model("large-v2").to("cuda")

audios = os.listdir("audios")

for audio in audios:
    if audio.endswith(".mp3"):
        parts = audio.split("_", 1)   # split only at the first underscore
        number = parts[0]             # before first underscore
        title = parts[1].rsplit(".", 1)[0]   # after first underscore, remove .mp3
        print(number, title)
            
        # result = model.transcribe(audio = f"audios/output.mp3",
        result = model.transcribe(audio = f"audios/{audio}",
                            language="hi",
                            task="translate",
                            word_timestamps=False)
    
        chunks = []
        for segment in result["segments"]:
            chunks.append({
                "number": number,
                "title": title,
                "start": segment["start"],
                "end": segment["end"],
                "text": segment["text"]
            })
            
        chunks_with_metadata = {"chunks": chunks, "text": result["text"]}
        
         # remove .mp3 from filename before saving JSON
        filename = os.path.splitext(audio)[0]
        with open(f"jsons/{audio}.json", "w") as f:
            json.dump(chunks_with_metadata, f, ensure_ascii=False, indent=2)   
            
                                 