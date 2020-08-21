# write your essentials_kit settings
RESET_PASSWORD_EMAIL_BODY_TEMPLATE = """
Hi User,<br>
<br>
We've received a request to reset your password. if you didn't make the reqeust, just ignore this email. Otherwise, you can reset your password using below link<br>
<br>
<a href="{{reset_password_link}}">Reset You PAssword</a><br>
<br>
For any queries mail to <a href="mailto:anuj.singhvi@ibhubs.co" target="_top">anuj.singhvi@ibhubs.co</a> or call +91-9427647531<br>
Thanks,<br>
Ib WorkFlow Team<br>
iB Hubs<br>
"""
EMAIL_SUBJECT = "Reset your password"
VERIFY_USER_EMAIL_SUBJECT = "Verification of your email"
VERIFY_USER_EMAIL_BODY_TEMPLATE = """
Hi 
Verify your email by using below link,
<br>
<a href="{verification_url}">Verify Your Email</a><br>
<br>
Thank you
"""

USER_VERIFICATION_EMAIL_EXPIRY_IN_SECONDS = 1800
