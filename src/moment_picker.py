import random

class MomentPicker:
    def __init__(self, model_name=None):
        self.duration = 488

    def find_clips(self, video_path, transcript, num_clips=3):
        try:
            from moviepy.editor import VideoFileClip
            self.duration = VideoFileClip(video_path).duration
        except Exception as e:
            print(f"⚠️ Could not get duration: {e}")

        clips = []
        for _ in range(num_clips):
            duration = int(self.duration)
            start = random.randint(10, max(20, duration - 60))
            end = min(start + random.randint(15, 35), duration)
            clips.append({
                "start": start,
                "end": end,
                "reason": f"Best moment #{len(clips)+1}"
            })
        return clips
