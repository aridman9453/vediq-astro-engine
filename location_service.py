import requests
from timezonefinder import TimezoneFinder
from zoneinfo import ZoneInfo
from datetime import datetime

tf = TimezoneFinder()

def resolve_location(place: str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": place, "format": "json", "limit": 1}
    headers = {"User-Agent": "vedIQ-Astro-AI/1.0"}
    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    results = response.json()
    if not results:
        raise ValueError(f"Location not found: {place}")

    latitude = float(results[0]["lat"])
    longitude = float(results[0]["lon"])
    timezone_name = tf.timezone_at(lat=latitude, lng=longitude)
    if timezone_name is None:
        raise ValueError(f"Timezone not found for: {place}")

    return {
        "latitude": latitude,
        "longitude": longitude,
        "timezone_name": timezone_name
    }

def birth_datetime_to_utc(birth_date: str, birth_time: str, timezone_name: str) -> datetime:
    """birth_date: 'YYYY-MM-DD', birth_time: 'HH:MM' (24hr, local to birth place)"""
    local_dt = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    local_dt = local_dt.replace(tzinfo=ZoneInfo(timezone_name))
    return local_dt.astimezone(ZoneInfo("UTC"))
