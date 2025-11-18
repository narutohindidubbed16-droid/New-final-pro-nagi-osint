# ===============================
# 📌 lookup.py  
# All API Request Functions
# ===============================

import aiohttp
from utils import clean_json


# ===============================
# 📌 GENERIC GET REQUEST
# ===============================
async def fetch_json(url: str):
    """
    Universal JSON fetcher for all OSINT APIs
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=10) as r:
                return await r.json()
        except:
            return {"error": "API Error or Timeout"}


# ===============================
# 📌 MOBILE LOOKUP
# ===============================
async def lookup_mobile(api_url: str, number: str):
    url = api_url + number
    data = await fetch_json(url)
    return clean_json(data)


# ===============================
# 📌 GST LOOKUP
# ===============================
async def lookup_gst(api_url: str, gst: str):
    url = api_url + gst
    data = await fetch_json(url)
    return clean_json(data)


# ===============================
# 📌 IFSC LOOKUP
# ===============================
async def lookup_ifsc(api_url: str, ifsc: str):
    url = api_url + ifsc
    data = await fetch_json(url)
    return clean_json(data)


# ===============================
# 📌 PINCODE LOOKUP
# ===============================
async def lookup_pincode(api_url: str, pin: str):
    url = api_url + pin
    data = await fetch_json(url)
    return clean_json(data)


# ===============================
# 📌 VEHICLE / RC LOOKUP
# ===============================
async def lookup_vehicle(api_url: str, rc: str):
    url = api_url + rc
    data = await fetch_json(url)
    return clean_json(data)
