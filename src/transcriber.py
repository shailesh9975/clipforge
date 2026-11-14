import whisper

def transcribe_local(video_path):
    print("🗣️ Transcribing audio...")
    model = whisper.load_model("tiny")
    result = model.transcribe(video_path, beam_size=3)
    return result["text"]
