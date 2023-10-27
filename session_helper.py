# Use Regular expression to extract the session information

import re


def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_session = match.group(0)
        return extracted_session

    return ""
