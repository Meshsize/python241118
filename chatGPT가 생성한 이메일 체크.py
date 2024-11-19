import re

# Email validation function
def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

# Sample email addresses
email_samples = [
    "user@example.com",
    "firstname.lastname@domain.com",
    "email@subdomain.example.com",
    "1234567890@example.com",
    "email+tag@example.co.uk",
    "invalid-email@.com",
    "@missingusername.com",
    "plainaddress",
    "user.name@domain..com",
    "email@domain@domain.com"
]

# Validate and display results
email_validation_results = {email: validate_email(email) for email in email_samples}
import ace_tools as tools; tools.display_dataframe_to_user(name="Email Validation Results", dataframe=email_validation_results) 
