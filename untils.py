# ===============================
# 📌 utils.py  
# Auto-Detect + JSON Cleaner
# ===============================

import re
import json


# ===============================
# 📌 AUTO-DETECT USER QUERY TYPE
# ===============================
def detect_query_type(text: str):
    text = text.strip().upper()

    # 10-digit mobile number
    if re.fullmatch(r"\d{10}", text):
        return "mobile"

    # 15-digit GST number
    if re.fullmatch(r"[0-9A-Z]{15}", text):
        return "gst"

    # 11-character IFSC
    if re.fullmatch(r"[A-Z]{4}0[A-Z0-9]{6}", text):
        return "ifsc"

    # 6-digit PINCODE
    if re.fullmatch(r"\d{6}", text):
        return "pincode"

    # Vehicle Number (MH12DE1433)
    if re.fullmatch(r"[A-Z]{2}\d{2}[A-Z]{1,3}\d{3,4}", text):
        return "vehicle"

    return None


# ===============================
# 📌 JSON Beautifier
# ===============================
def clean_json(data):
    """
    Converts raw API JSON into clean readable format
    """
    try:
        return json.dumps(data, indent=2, ensure_ascii=False)
    except:
        return str(data)


# ===============================
# 📌 Validate Inputs (Extra Safety)
# ===============================
def validate_input(mode, text):
    text = text.strip().upper()

    patterns = {
        "mobile": r"^\d{10}$",
        "gst": r"^[0-9A-Z]{15}$",
        "ifsc": r"^[A-Z]{4}0[A-Z0-9]{6}$",
        "pincode": r"^\d{6}$",
        "vehicle": r"^[A-Z]{2}\d{2}[A-Z]{1,3}\d{3,4}$",
    }

    if mode in patterns and re.fullmatch(patterns[mode], text):
        return True
    return False
