#!/bin/bash

# Create src/ directory if missing
mkdir -p src

# Create src/downloader.py
cat > src/downloader.py << 'EOL'
import yt_dlp
import os

def download_youtube_video(url, output_dir=".", filename="downloaded_video.mp4"):
    ydl_opts = {
        "format": "mp4",
        "outtmpl": os.path.join(output_dir, filename),
        "noplaylist": True,
        "quiet": False,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"📥 Downloading from: {url}")
            ydl.download([url])
            video_path = os.path.join(output_dir, filename)
            print(f"✅ Download saved to: {video_path}")
            return video_path
    except Exception as e:
        print(f"❌ Download failed: {e}")
        return None
EOL

# Create src/transcriber.py
cat > src/transcriber.py << 'EOL'
from faster_whisper import WhisperModel

def transcribe_local(video_path):
    print("🗣️ Transcribing audio (using tiny CPU model)...")
    model = WhisperModel("tiny", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(video_path, beam_size=3)
    text = " ".join([seg.text for seg in segments])
    return text
EOL

# Create src/scene_detector.py
cat > src/scene_detector.py << 'EOL'
from scenedetect import open_video, detect, AdaptiveDetector

def detect_scenes(video_path, threshold=25):
    try:
        video = open_video(video_path)
        scene_list = detect(video, AdaptiveDetector(threshold=threshold))
        video.release()
        return scene_list
    except Exception as e:
        print(f"❌ Scene detection failed: {e}")
        return []
EOL

# Create src/moment_picker.py (mock AI for now)
cat > src/moment_picker.py << 'EOL'
import json
import random

class MomentPicker:
    def __init__(self, model_name=None):
        print("🧠 Using mock AI to simulate clip selection (replace later with Qwen)")

    def find_clips(self, video_path, transcript, num_clips=3):
        # Simulate viral moments
        duration = 600  # Assume 10-min video
        mock_clips = [
            {
                "start": random.randint(45, 120),
                "end": random.randint(60, 150),
                "reason": "Hook: 'You won't believe this AI trick...'"
            },
            {
                "start": random.randint(180, 300),
                "end": random.randint(195, 330),
                "reason": "Punchline or twist reveal"
            },
            {
                "start": random.randint(400, 550),
                "end": random.randint(415, 580),
                "reason": "Emotional closing or final tip"
            }
        ]
        return mock_clips[:num_clips]
EOL

# Create src/editor.py
cat > src/editor.py << 'EOL'
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, crop
import os

def create_short(video_path, start, end, output_path, title=""):
    print(f"✂️ Editing {start:.1f}s → {end:.1f}s for {output_path}")
    try:
        clip = VideoFileClip(video_path).subclip(start, end)
        # Resize & crop to 9:16 (vertical)
        clip = clip.resize(height=1920)
        w, h = clip.size
        x1 = (w - 1080) // 2
        x2 = x1 + 1080
        clip = crop(clip, x1=x1, x2=x2)

        # Add title
        txt_clip = TextClip(
            title.upper(),
            fontsize=50,
            color='white',
            font="Arial-Bold",
            stroke_color='black',
            stroke_width=3,
            size=(1000, None)
        ).set_position("center").set_duration(clip.duration)

        video = CompositeVideoClip([clip, txt_clip])
        video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")
        print(f"✅ Saved: {output_path}")
    except Exception as e:
        print(f"❌ Failed: {e}")
EOL

# Create src/cli.py (with correct relative imports)
cat > src/cli.py << 'EOL'
import argparse
import os
from .downloader import download_youtube_video
from .transcriber import transcribe_local
from .moment_picker import MomentPicker
from .editor import create_short

def main():
    parser = argparse.ArgumentParser(description="ClipForge – Turn long videos into Shorts")
    parser.add_argument("url", help="YouTube URL")
    args = parser.parse_args()

    print("🎥 ClipForge Activated...")

    video_path = download_youtube_video(args.url)
    if not video_path or not os.path.exists(video_path):
        print("❌ Failed to download video.")
        return

    transcript = transcribe_local(video_path)
    print("🎙️ Transcript done:", transcript[:200] + "..." if transcript else "None")

    picker = MomentPicker()
    clips = picker.find_clips(video_path, transcript, num_clips=3)

    for i, c in enumerate(clips):
        output = f"short_output_{i+1}.mp4"
        create_short(
            video_path=video_path,
            start=c['start'],
            end=c['end'],
            output_path=output,
            title=c['reason']
        )
    print("✅ Done! Check: short_output_*.mp4")

if __name__ == "__main__":
    main()
EOL

# Create __init__.py
touch src/__init__.py

# Create assets folder
mkdir -p assets/music

echo "✅ All files created successfully!"
echo "Now run:"
echo "python -m src.cli 'https://www.youtube.com/watch?v=UvSWMcOEx10'"
