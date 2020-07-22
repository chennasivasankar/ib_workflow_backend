class EmailService:
    def send_email_to_user(self, email: str, subject: str, content: str):
        from ib_iam.adapters.email_service_implementation import EmailSenderImpl
        email_sender_implementation = EmailSenderImpl(
            subject=subject, email_body_template=content
        )
        email_sender_implementation.send_email(email=email, data={})
