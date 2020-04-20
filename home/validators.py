from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.validators import ASCIIUsernameValidator

regex_validator = [RegexValidator(regex='^[a-zA-Z0-9]*$', message='Username must be Alphanumeric', code='invalid_username')]

email_validator = [EmailValidator('Please enter a valid email!')]

ascii_validator = [ASCIIUsernameValidator()]