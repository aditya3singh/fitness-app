import yt_dlp
from yt_dlp.utils import DownloadError

def get_info(url):
    try:
        # Configure yt-dlp options
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=False)
        
        if "entries" in result:
            video = result["entries"][0]
        else:
            video = result
            
        # Extract required information with fallbacks
        infos = {
            'video_id': video.get('id', ''),
            'title': video.get('title', 'Unknown Title'),
            'channel': video.get('uploader', 'Unknown Channel'),
            'view_count': video.get('view_count', 0),
            'like_count': video.get('like_count', 0),
            'channel_id': video.get('uploader_id', ''),
            'duration': video.get('duration', 0),
            'categories': video.get('categories', []),
            'tags': video.get('tags', [])
        }
        
        return infos
        
    except DownloadError as e:
        print(f"YouTube extraction error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None