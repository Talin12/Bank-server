from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from loguru import logger

def send_otp_email(email_address, otp):
    subject = str(_('Your OTP Code for Login'))
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email_address]
    
    context = {
        'otp': otp,
        'expiry_time': int(settings.OTP_EXPIRATION.total_seconds() // 60),
        'site_name': str(settings.SITE_NAME),
    }
    html_email = render_to_string("emails/otp_email.html", context)
    plain_email = strip_tags(html_email)

    email_message = EmailMultiAlternatives(subject, plain_email, from_email, recipient_list)
    email_message.attach_alternative(html_email, "text/html")

    try:
        email_message.send()
        logger.info(f"OTP Email sent successfully to: {email_address}")
    except Exception as e:
        logger.error(f"Failed to send OTP email to {email_address}: ERROR: {str(e)}")
        raise

def send_account_locked_email(self):
    subject = str(_("Your account has been locked"))
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [self.email]
    context = {
        "user": self,
        "lockout_duration": int(settings.LOCKOUT_DURATION.total_seconds() // 60),
        "site_name": str(settings.SITE_NAME),
    }
    html_email = render_to_string("emails/account_locked.html", context)
    plain_email = strip_tags(html_email)
    email = EmailMultiAlternatives(subject, plain_email, from_email, recipient_list)
    email.attach_alternative(html_email, "text/html")
    try:
        email.send()
        logger.info(f"Account locked email sent to: {self.email}")
    except Exception as e:
        logger.error(f"Failed to send account locked email to {self.email}: Error: {str(e)}")