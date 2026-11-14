# src/downloader.py
import yt_dlp
import os

def download_video(url, output_path="downloaded_video.mp4"):
    print(f"📥 Downloading from: {url}")

    # Universal format: best video + best audio, merge automatically
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",  # Best video and audio — merge if needed
        "outtmpl": output_path,              # Output file name
        "noplaylist": True,                  # Don’t download playlists
        "quiet": False,
        "no_warnings": False,
        "retries": 5,
        "fragment_retries": 5,
        "merge_output_format": "mp4",        # Force merge to MP4
        "concurrent_fragment_downloads": 3,
        "geo_bypass": True,
    }

    try:
        # Remove old file if exists
        if os.path.exists(output_path):
            os.remove(output_path)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("🔍 Fetching video info...")
            # Download and automatically merge if needed
            ydl.download([url])

        # Confirm file was created
        if os.path.exists(output_path):
            print(f"✅ Download successful: {output_path}")
            return output_path
        else:
            print("❌ Download failed: File not created.")
            return None

    except Exception as e:
        print(f"❌ Download failed: {e}")
        return None
