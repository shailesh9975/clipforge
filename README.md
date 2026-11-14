# 🎬 ClipForge – AI-Powered Short Video Generator 🚀

> 🔁 **Turn long videos into viral Shorts — automatically.**  
> 🎯 Create TikTok/Reels-ready clips with AI-selected moments, styled captions, and vertical crop.  
> 🌱 Open-source. Offline. Free. No API costs.  
> 🔧 Made for creators, by AI.

![ClipForge Banner](assets/banner.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-FF4B00?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBmaWxsPSIjZmZmZmZmIiBkPSJNMTIsMGMwLDAsLTgsMi4yNCwtOCw4djBjMCw1Ljc2LDgsMTIsOCwxMnM4LTUuNzYsOC0xMnYwQzIxLjcsMi4yNCwxMiwwLDEyLDB6IE0xMiwyYzIuNzUsMCw1LjIyLDIuMTUsNi4zMSw1LjA4QzE3LjU4LDUuMjIsMTUsNC4yNCwxNSw0YzAsMC43Nyw3LjUsMC43Nyw3LjUsMi4zOHY4LjE2YzAtMS42OCw3LjUtMC44MSw3LjUtMi4zOHYtMC4yOGMtMS4wOS0yLjkzLTMyLjQyLTguNDItNi4zMS0xMi4wNmMtMi41Ni0xLjM3LTUuNTUtMi4wNi04LjQ5LTIuMDZzLTYuODMsMC42OS05LjQsMi4wNkM0LjcyLDIuNzQsMS42NCwzLjQzLDQuMiwyLjA2QzYuNzcsMC42OSwxMC40OSwwLDEyLDAseiBNOTYuMDEsMjUuMjRjLTUuMzIsMCwtOS42Ni00LjM0LTkuNjYtOS42NlYyNGgtNGMtMi4yOCwwLTQuMSwxLjgyLTQuMSw0LjF2MTUuODhjMCwyLjI4LDQuMTIsNC4xLDkuNjYsNC4xcTAsMCwwLDAgNzAuOSwwcTUuODAsMCw5LjY2LTQuMTA0djBjNC41NiwwLDkuNi00LjYsOS42LTEwLjN2LTE1LjI4YzAsLTUuNzItNC40NC05LjktOS42Ni05LjlzLTkuNjYsNC4yOC05LjY2LDkuNlYyNCZuYnNwO2g0di0xLjdjMiw0Ljk4LDQuODMsOC4xNyw4LjQxLDguMTdDLDE5LjYyLDIwLjg1LDIwLDE0LjM4LDIwLDEzLjE4di0uMTg2aDR2LjA0MWMwLDEuMDIsLTEuOTQsNi4yMy0zLjk5LDguMDRoMGgtMEgxMS44NWgwLTQuNDNoN20tOC45Niw0LjUySDExLjQxdjUuNDRoMi4xNGw1LjY1LTEuNTRjMS43MS0uNTgsMy4wNC0xLjA2LDQuMDUtMS40NCAxLjYwNC0uNjAsMi4xNi0uMzIsMi4xNiwxLjA0VjM3aC4wOGgxaDN2LThoLTNxLTEuNDgsMC0xLjI0LTQuMTQ2Yy4yNC00LjAzNCwyLjUtNi4wMSw1LjctNi4wMWgzSDEwdjhoM2gzdi0yLjU2Yy0zLjA0LDAtNC44OCwyLjI0LTUuOSw0LjIyLTExLjgtdDEuMTYtMTEuODQsOC42YzAsMy42OCwyLjI0LDYuNTgsNS45LDguMDQgMy45OCwxLjY0LDcuMDQsMi40Miw4Ljg0LDIuNDJoMWw4LjA4LDBoMUwwLDB6Ii8+PC9zdmc+)](https://huggingface.co/spaces/yourname/clipforge)

---

## 📹 Demo: How It Works

ClipForge automatically:
1. 🖥️ Downloads your video (YouTube, TikTok, etc.)
2. 🧠 Analyzes for **most engaging moments** (hooks, jokes, emotion)
3. ✂️ Cuts & crops to 9:16 Shorts
4. 🔤 Adds **customizable AI captions**
5. 💾 Exports ready-to-post MP4s

![Flow](assets/flow.png)

---

## 🛠️ Get Started

### ✅ Prerequisites

- Python ≥3.9
- OS: Linux/macOS/WSL (Windows support possible)
- RAM: 4+ GB (8+ recommended)
- Optional: GPU for future AI upgrades (Qwen2.5-VL)
- FFmpeg & ImageMagick (see setup below)

### 1. Clone the Repo

```bash
git clone https://github.com/shailesh9975/clipforge.git
cd clipforge

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

3. Install Dependencies
pip install -r requirements.txt
Installs: yt-dlp, whisper, moviepy, gradio, pillow, numpy

4. Fix ImageMagick (for caption rendering)
MoviePy uses ImageMagick to render subtitles. Fix security policy:
sudo sed -i 's/policy domain="coder" rights="none" pattern="TXT"/policy domain="coder" rights="read|write" pattern="TXT"/g' /etc/ImageMagick-6/policy.xml

🌐 Run the Web UI (No Code Needed)
Launch the AI agent dashboard:

python -m src.ui


Features:
📥 Paste YouTube URL or drag & drop video
🎨 Customize font, size, color, outline, background
🚀 One-click "Generate Shorts"
🎉 See all clips in browser

📝 Custom Subtitle Options
Full user control:

Setting	Options	Default
Font	Arial-Bold, Impact, Open-Sans	Arial-Bold
Text Size	Small (40), Medium (54), Large (72)	Medium
Text Color	White, Red, Blue, Green, Yellow, Purple, Pink, Orange	White
Outline Color	Black, White, None	Black
Outline Width	1–5 px	3
Text Position	Top, Center, Bottom	Center
Background Bar	[ ] Show behind text	Off

🧪 Example Output
Files created:
outputs/short_1.mp4
outputs/short_2.mp4
outputs/short_3.mp4

With:

✅ 9:16 vertical format
✅ Styled captions
✅ Clean audio sync
✅ High quality H.264 + AAC

👨‍💻 Maintained By
Shailesh
GitHub: @shailesh9975
Builds AI tools for creators.
