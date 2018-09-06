import logging

import requests

from django.conf import settings

logger = logging.getLogger()

ADMIN_NAME='vilmibm'
EXTERNAL_FROM='tildetown@protonmail.ch'

def send_email(to, body, subject='a message from tilde.town'):
    """Sends an email using mailgun. Logs on failure."""
    response =  requests.post(
        settings.MAILGUN_URL,
        auth=('api', settings.MAILGUN_KEY),
        data={
            'from': EXTERNAL_FROM,
            'to': to,
            'subject': subject,
            'text': body
        }
    )

    success = response.status_code == 200

    if not success:
        logger.error('{}: failed to send email "{}" to {}'.format(
            response.status_code,
            subject,
            to))

    return success
