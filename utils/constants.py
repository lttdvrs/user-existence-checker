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
    "spotify" : {
        "link" : "https://open.spotify.com/user/{}"
    }
}