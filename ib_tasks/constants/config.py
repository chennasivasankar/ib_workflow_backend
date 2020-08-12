import re

DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"

VALID_EMAIL_REGEX = '[^@]+@[^@]+\.[^@]+'

VALID_URL_REGEX_PATTERN = re.compile(
    r'^https?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # 
    # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

STRONG_PASSWORD_REGEX = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[" \
                        "A-Za-z\d@$!#%*?&]{6,20}$"

"""
        validations in strong password::
        * Should have at least one number.
        * Should have at least one uppercase and one lowercase character.
        * Should have at least one special symbol.
        * Should be between 6 to 20 characters long.
"""
