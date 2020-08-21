import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.conf import settings
from ib_users.interactors.third_party.email_sender import EmailSender

logger = logging.getLogger(__name__)


class EmailSenderImpl(EmailSender):
    def __init__(self, subject: str, email_body_template: str):
        self.subject = subject
        self.email_body_template = email_body_template
        print(email_body_template,"asd")

    def send_email(self, email: str, data: dict):
        from django.template import Template
        from django.template import Context

        template_ = self.email_body_template
        serializer_template = Template(template_)
        print('template_: ', template_)
        print('serializer_template: ', serializer_template)
        print('data: ', data)
        context = Context(data)
        html_content = serializer_template.render(context)
        print('html_content: ', html_content)
        subject = self.subject

        msg = MIMEMultipart('alternative')

        msg['Subject'] = subject
        msg['From'] = '"{}" <{}>'.format(
            settings.DEFAULT_SENDER_NAME, settings.DEFAULT_SENDER_EMAIL
        )
        msg['To'] = email

        # part1 = MIMEText("", 'plain')
        part2 = MIMEText(html_content, 'html')

        # msg.attach(part1)
        msg.attach(part2)

        self._send_mail_over_smtp(
            receiver=email,
            msg=msg
        )

    @classmethod
    def _send_mail_over_smtp(cls, receiver, msg):
        try:
            cls._send_mail_over_smtp_with_ssl(receiver, msg)
        except Exception:
            cls._send_mail_over_smtp_without_ssl(receiver, msg)

    @staticmethod
    def _send_mail_over_smtp_with_ssl(receiver, msg):
        import socket
        socket.setdefaulttimeout(2)

        server = settings.EMAIL_HOST
        port = settings.EMAIL_PORT
        username = settings.EMAIL_HOST_USER
        password = settings.EMAIL_HOST_PASSWORD
        sender = settings.DEFAULT_SENDER_EMAIL

        try:
            s = smtplib.SMTP_SSL(server, port)
            s.login(username, password)
            s.sendmail(sender, receiver, msg.as_string())
            s.quit()
        except Exception as error:
            logger.error(error)
            raise error

    @staticmethod
    def _send_mail_over_smtp_without_ssl(receiver, msg):
        import socket
        socket.setdefaulttimeout(2)

        server = settings.EMAIL_HOST
        port = settings.EMAIL_PORT
        username = settings.EMAIL_HOST_USER
        password = settings.EMAIL_HOST_PASSWORD
        sender = settings.DEFAULT_SENDER_EMAIL

        try:
            s = smtplib.SMTP(server, port)
            s.starttls()
            s.login(username, password)
            s.sendmail(sender, receiver, msg.as_string())
            s.quit()
        except Exception as error:
            logger.error(error)
            raise error
