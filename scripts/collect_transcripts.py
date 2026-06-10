"""
Collect YouTube transcripts via the Supadata API and save them as Markdown
files organized by expert.

Setup:
    1. Get a free API key at https://supadata.ai (100 credits/month, no card).
    2. Set it as an environment variable (never hardcode keys in a public repo):
         export SUPADATA_API_KEY="your_key_here"        # macOS/Linux
         setx SUPADATA_API_KEY "your_key_here"          # Windows
    3. Add your videos to the VIDEOS dict below.
    4. Run: python collect_transcripts.py

Output:
    research/youtube-transcripts/<expert-slug>/<video-slug>.md
"""

import os
import re
import sys
import time

import requests

API_KEY = os.environ.get("SUPADATA_API_KEY")
BASE_URL = "https://api.supadata.ai/v1/youtube/transcript"
OUTPUT_DIR = os.path.join("research", "youtube-transcripts")

# expert name -> list of (video title, video URL)
VIDEOS = {
    "Nathan Gotch": [
        ("EXAMPLE - replace me", "https://www.youtube.com/watch?v=VIDEO_ID"),
    ],
    "Ross Simmonds": [
        ("EXAMPLE - replace me", "https://www.youtube.com/watch?v=VIDEO_ID"),
    ],
    # Add the rest of your experts here...
}


def slugify(text: str) -> str:
    """Turn 'My Video Title!' into 'my-video-title' for safe filenames."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:80]


def fetch_transcript(video_url: str) -> dict | None:
    """Fetch a transcript from Supadata. Returns the JSON response or None."""
    try:
        response = requests.get(
            BASE_URL,
            params={"url": video_url, "text": "true"},
            headers={"x-api-key": API_KEY},
            timeout=30,
        )
        if response.status_code == 200:
            return response.json()
        print(f"  ERROR {response.status_code}: {response.text[:200]}")
        return None
    except requests.RequestException as exc:
        print(f"  Request failed: {exc}")
        return None


def save_transcript(expert: str, title: str, url: str, data: dict) -> str:
    expert_dir = os.path.join(OUTPUT_DIR, slugify(expert))
    os.makedirs(expert_dir, exist_ok=True)
    path = os.path.join(expert_dir, f"{slugify(title)}.md")

    # With text=true Supadata returns the transcript as a single string in
    # "content"; without it, "content" is a list of timestamped segments.
    content = data.get("content", "")
    if isinstance(content, list):
        content = " ".join(seg.get("text", "") for seg in content)

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"- **Expert:** {expert}\n")
        f.write(f"- **Source:** {url}\n")
        f.write(f"- **Language:** {data.get('lang', 'unknown')}\n")
        f.write(f"- **Collected:** {time.strftime('%Y-%m-%d')}\n\n")
        f.write("## Transcript\n\n")
        f.write(content.strip() + "\n")
    return path


def main() -> None:
    if not API_KEY:
        sys.exit("Missing SUPADATA_API_KEY environment variable. See setup notes at top of file.")

    total, saved = 0, 0
    for expert, videos in VIDEOS.items():
        print(f"\n{expert}")
        for title, url in videos:
            total += 1
            print(f"  Fetching: {title}")
            data = fetch_transcript(url)
            if data:
                path = save_transcript(expert, title, url, data)
                saved += 1
                print(f"  Saved -> {path}")
            time.sleep(1)  # be polite, avoid hammering the API

    print(f"\nDone. {saved}/{total} transcripts saved.")


if __name__ == "__main__":
    main()
