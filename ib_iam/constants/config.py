REQUIRED_PASSWORD_MIN_LENGTH = '8'
REQUIRED_PASSWORD_SPECIAL_CHARS = '`~!@#$%^&*()+-_[]{}|;:",.<>/?'
RESET_PASSWORD_TOKEN_EXPIRY_TIME_IN_SECONDS = 10000
BASE_URL_FOR_RESET_PASSWORD_LINK \
    = "https://127.0.0.1:8000/api/ib_iam/update_password/v1/?token="
EMAIL_SUBJECT = "Hi User, Here you can reset the password"
# EMAIL_CONTENT = "By using this link "
EMAIL_CONTENT = "Hai User\n, " \
                          "We've received a request to reset your password. " \
                          "if you didn't make the reqeust, " \
                          "just ignore this email. " \
                          "Otherwise, you can reset " \
                          "your password using this link: " \
                          "{{reset_password_link}}\n" \
                          "Thanks,\n" \
                          "The Ib WorkFlow Team"
