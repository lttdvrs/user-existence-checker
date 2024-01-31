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
    "discord" : {
        "type": 1,
        "link" : "https://discord.com/register"
    },
    "reddit" : {
        "link" : "https://www.reddit.com/user/{}/",
        "findable": "faceplate-tracker",
        "soup_data" : {
            "source": "profile"
        }
    },
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
    },
}