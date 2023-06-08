import re


def validate_email(data):
    gmail_pattern = r'\b[A-Za-z0-9._%+-]+@gmail\.com\b'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_addresses = re.findall(email_pattern, data.get_text())
    return email_addresses
