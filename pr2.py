import re

def validate_email(email):

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


# Test cases
if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "john.doe@company.co.uk",
        "invalid.email@",
        "missing@domain",
        "no-at-sign.com",
        "user+tag@domain.org",
        "test@test.c",
        "aaaaaaa@ddd.com"
    ]
    
    for email in test_emails:
        result = validate_email(email)
        print(f"{email}: {result}")
