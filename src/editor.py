# src/editor.py
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.fx.crop import crop
import os

def create_short(video_path, start, end, output_path, title=""):
    try:
        # Load video and cut to range
        clip = VideoFileClip(video_path).subclip(start, end)

        # Resize to 1920px height for vertical video (9:16)
        clip = clip.resize(height=1920)
        w, h = clip.size

        # Center crop to 1080px width (vertical-safe)
        x1 = (w - 1080) // 2
        x2 = x1 + 1080
        clip = crop(clip, x1=x1, x2=x2)

        # Create stylized caption
        txt_clip = TextClip(
            title.upper(),
            fontsize=54,
            color='white',
            font='Arial-Bold',
            stroke_color='black',
            stroke_width=3,
            size=(1000, None),
            method='caption',
            align='center'
        ).set_position(("center", "center")).set_duration(clip.duration)

        # Overlay caption on video
        video = CompositeVideoClip([clip, txt_clip])

        # Export with proper audio sync
        video.write_videofile(
            output_path,
            fps=24,
            codec="libx264",
            audio_codec="aac",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
            threads=4,
            logger=None  # Clean output
        )

        print(f"✅ Saved: {output_path}")

    except Exception as e:
        print(f"❌ Edit failed: {e}")
