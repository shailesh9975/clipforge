import argparse
import os
from .downloader import download_video
from .transcriber import transcribe_local
from .moment_picker import MomentPicker
from .editor import create_short

def main():
    parser = argparse.ArgumentParser(description="ClipForge – Create Shorts from YouTube")
    parser.add_argument("url", help="YouTube URL")
    args = parser.parse_args()

    print("🎥 ClipForge Activated...")

    video_path = download_video(args.url)
    if not video_path or not os.path.exists(video_path):
        print("❌ Failed to download.")
        return

    transcript = transcribe_local(video_path)
    print("📝 Transcript done")

    picker = MomentPicker()
    clips = picker.find_clips(video_path, transcript, num_clips=3)

    for i, c in enumerate(clips):
        output = f"short_output_{i+1}.mp4"
        create_short(video_path, c['start'], c['end'], output, title=c['reason'])

    print("🎉 All done! Check: short_output_*.mp4")

if __name__ == "__main__":
    main()
