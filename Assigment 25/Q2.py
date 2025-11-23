import re

def extract_dates(text):

    pattern = r"""
        (                           
            \b\d{2}/\d{2}/\d{4}\b        
            |
            \b\d{2}-\d{2}-\d{4}\b        
            |
            \b(?:January|February|March|April|May|June|
                  July|August|September|October|November|December)
            \s+\d{1,2},\s*\d{4}\b        
        )
    """
    return re.findall(pattern, text, flags=re.IGNORECASE | re.VERBOSE)
