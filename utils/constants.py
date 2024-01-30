from fake_useragent import UserAgent
from dotenv import load_dotenv
import os

load_dotenv()

URLS = {
    "instagram": {
        "link": "https://www.instagram.com/{}/",
        "findable": "meta",
        "soup_data": {
            "property": "og:description"
        }
    },
    "tiktok": {
        "link": "https://tiktok.com/@{}/",
        "findable": "script",
        "soup_data": {
             "id": "__UNIVERSAL_DATA_FOR_REHYDRATION__",
        },
        "key": "uniqueId",
    },
    "snapchat": {
        "link": "https://www.snapchat.com/add/{}"
    },
    "pinterest": {
        "link": "https://www.pinterest.com/{}",
        "findable" : "script",
        "soup_data": {
            "type":"application/ld+json",
        },
        "key": "contentUrl",
    },
    "github" : {
        "link" : "https://github.com/{}"
    },
    "reddit" : {
        "link" : "https://www.reddit.com/user/{}/",
        "findable": "faceplate-tracker",
        "soup_data" : {
            "source": "profile"
        }
    },
    # "youtube" : {
    #     "api_key": os.environ.get("YOUTUBE_API_V3_KEY"),
    #     "link" : "https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&maxResults=1&q={}&key={}",
    #     "requires_api_key": 1
    # },
    "spotify": {
        "link" : "https://open.spotify.com/user/{}"
    },
    "wattpad": {
        "link" : "https://wattpad.com/user/{}",
        "headers" : {
            "User-Agent": UserAgent().random
        }
    },
    "twitch": {
        "link" : "https://passport.twitch.tv/usernames/{}",
        "headers": {
            "Connection" : "close"
        }
    },
    "linkedin": {
        "type": 1,
        "link" : "https://www.linkedin.com/in/{}/"
    }
}