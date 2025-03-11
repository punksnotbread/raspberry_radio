from typing import Any

RADIOS: dict[str, dict[str, Any]] = {
    "Off": {"id": 0},
    "Palanga Street Radio": {
        "id": 1,
        "url": "https://stream.palanga.live:8443/palanga128.mp3",
    },
    "LRT Opus": {
        "id": 2,
        "url": "https://stream-live.lrt.lt/radio_opus/320k/lrt_opus.m3u8",
    },
    "NTS Live 1": {
        "id": 3,
        "url": "http://stream-relay-geo.ntslive.net/stream",
    },
    "NTS Live 2": {
        "id": 4,
        "url": "http://stream-relay-geo.ntslive.net/stream2",
    },
    "Radio Vilnius": {
        "id": 5,
        "url": "http://radio.audiomastering.lt:8000/radiovilnius-mp3",
    },
}
