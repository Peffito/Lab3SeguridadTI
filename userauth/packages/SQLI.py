import re

def sql_injection_check(query):
    # Common SQL injection patterns and keywords
    patterns = [
        r'\bUNION\b',
        r'\bSELECT\b',
        r'\bINSERT\b',
        r'\bUPDATE\b',
        r'\bDELETE\b',
        r'\bDROP\b',
        r'\b OR \b',
        r'\b1=1\b',
        r'\b--\s',
    ]

    for pattern in patterns:
        if re.search(pattern, query):
            return True

    return False

# Example usage:
#query = "SELECT * FROM users WHERE username = 'admin' AND password = 'password'"
#if is_sql_injection(query):
#    print("Potential SQL injection detected!")
#else:
#    print("Query appears safe.")
