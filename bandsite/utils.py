import re

def extract_youtube_video_id(url):
    """
    Extrage ID-ul video-ului YouTube dintr-un URL.
    """
    match = re.match(r'https?://(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)', url)
    if match:
        return match.group(1)
    return None
