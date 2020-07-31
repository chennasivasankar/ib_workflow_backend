class EmailService:
    @staticmethod
    def send_email_to_user(email: str, subject: str,
                           email_body_template: str, data=None):
        from ib_iam.services.email_service_implementation import \
            EmailSenderImpl
        email_sender_implementation = EmailSenderImpl(
            subject=subject, email_body_template=email_body_template
        )
        email_sender_implementation.send_email(email=email, data=data)
