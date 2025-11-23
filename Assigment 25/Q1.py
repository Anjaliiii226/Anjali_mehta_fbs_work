import re

def censor_text(text, forbidden_words):
    pattern = r"\b(" + "|".join(map(re.escape, forbidden_words)) + r")\b"

    def replace_with_stars(match):
        return "*" * len(match.group())

    return re.sub(pattern, replace_with_stars, text, flags=re.IGNORECASE)
