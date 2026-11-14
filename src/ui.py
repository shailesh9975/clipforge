# src/ui.py - ClipForge AI Agent Dashboard
import gradio as gr
import os
import tempfile
import time
from pathlib import Path

# Reuse your core functions
from .downloader import download_video
from .transcriber import transcribe_local
from .moment_picker import MomentPicker
from .editor import create_short

# Paths
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def generate_shorts(url_or_file, progress=gr.Progress()):
    # Clear old outputs
    os.system(f"rm -f {OUTPUT_DIR}/short_*.mp4")

    yield "🤖 **ClipForge Agent Activated!** Let's make something viral...", []

    # Handle input
    if url_or_file is None and not isinstance(url_or_file, str):
        yield "❌ Please provide a YouTube link or upload a video.", []
        return

    video_path = None

    # Step 1: Download or use uploaded file
    if isinstance(url_or_file, str):
        if url_or_file.strip().startswith(("http", "www")):
            progress(0.1, "Downloading video...")
            yield "🔍 Downloading video...", []
            video_path = download_video(url_or_file, "downloaded_video.mp4")
            if not video_path:
                yield "❌ Failed to download video.", []
                return
        else:
            yield "❌ Please enter a valid YouTube URL.", []
            return
    else:
        yield "📁 Using uploaded video...", []
        video_path = url_or_file.name

    if not os.path.exists(video_path):
        yield "❌ Video file not found.", []
        return

    yield "🗣️ Transcribing audio for context...", []
    try:
        transcript = transcribe_local(video_path)
        yield "✅ Transcribed! Now searching for viral moments...", []
    except Exception as e:
        transcript = ""
        yield f"⚠️ Could not transcribe: {e}", []

    # Step 2: Find best clips
    yield "🧠 AI is picking the top 3 viral moments...", []
    try:
        picker = MomentPicker()
        clips = picker.find_clips(video_path, transcript, num_clips=3)
        if not clips:
            yield "❌ No clips could be selected.", []
            return
    except Exception as e:
        yield f"❌ AI error: {e}", []
        return

    # Step 3: Generate videos
    outputs = []
    for i, c in enumerate(clips):
        output_path = OUTPUT_DIR / f"short_{i+1}.mp4"
        progress((i + 1) * 0.3 + 0.3, f"Creating Short #{i+1}")
        yield f"🎬 Creating Short #{i+1}: {c['reason']}", outputs

        create_short(
            video_path=video_path,
            start=c["start"],
            end=c["end"],
            output_path=str(output_path),
            title=c["reason"]
        )

        if output_path.exists():
            outputs.append(str(output_path))
        time.sleep(0.5)  # UX delay

    # Final result
    yield f"🎉 **All done!** Generated {len(outputs)} Shorts ready to post 👇", outputs

# 🎨 Gradio UI
with gr.Blocks(theme=gr.themes.Soft(), title="🤖 ClipForge AI Agent") as demo:
    gr.Markdown("""
    # 🎬 🔥 **ClipForge AI Agent**
    ### 🌟 Turn Long Videos Into Viral Shorts — **100% Free & Open-Source**
    Enter a YouTube link or upload any video → let AI pick the best moments!
    """)

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📥 Input Video")
            input_type = gr.Radio(
                ["YouTube URL", "Upload Video"],
                label="Choose Input Type",
                value="YouTube URL"
            )

            youtube_url = gr.Textbox(
                label="🔗 YouTube URL",
                placeholder="https://youtube.com/watch?v=..."
            )
            video_upload = gr.File(
                label="📁 Upload Video",
                file_types=["video"],
                visible=False
            )

            run_btn = gr.Button("🚀 Generate Shorts", variant="primary")

        with gr.Column(scale=1):
            status = gr.Textbox(label="💬 AI Agent Says", lines=10)
            results = gr.Gallery(label="🎥 Generated Shorts", columns=1, object_fit="contain")

    # Toggle input
    def toggle_input(choice):
        return {
            "youtube_url": gr.update(visible=choice == "YouTube URL"),
            "video_upload": gr.update(visible=choice == "Upload Video")
        }

    input_type.change(toggle_input, inputs=input_type, outputs=[youtube_url, video_upload])

    # Run on click
    run_btn.click(
        fn=generate_shorts,
        inputs=youtube_url,
        outputs=[status, results]
    )

    gr.Markdown("""
    ---
    ✅ Powered by `yt-dlp`, `Whisper`, `MoviePy`, `Gradio`  
    🐙 Open source: [GitHub @yourname/clipforge](https://github.com/yourname/clipforge)  
    💬 Made with ❤️ for creators.
    """)

# Launch
if __name__ == "__main__":
    print("🌟 Starting ClipForge AI Agent Web UI...")
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True  # Gives you a public link
    )
