import os
import requests


def extract_video_id(url):
    """
    Supports:
    https://youtu.be/xxxxx
    https://www.youtube.com/watch?v=xxxxx
    """

    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]

    if "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]

    raise ValueError("Invalid YouTube URL")


def get_transcript(youtube_url):

    video_id = extract_video_id(youtube_url)

    headers = {
        "x-api-key": os.getenv("SUPADATA_API_KEY")
    }

    response = requests.get(
        f"https://api.supadata.ai/v1/youtube/transcript?videoId={video_id}",
        headers=headers,
        timeout=60
    )

    response.raise_for_status()

    return response.json()