def validate_email(email: str) -> bool:
    return "@" in email

def validate_phone(phone: str) -> bool:
    return len(phone) >= 10
