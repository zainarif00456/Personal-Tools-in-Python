import re

def validate_pan_number(pan_number):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
    match = re.match(pattern, pan_number)
    if match:
        return True
    return False

# Example usage
pan_number = 'ABCDE1234F'
is_valid = validate_pan_number(pan_number)
print("Is PAN card number valid?", is_valid)