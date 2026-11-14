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
