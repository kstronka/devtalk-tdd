import logging
from typing import Protocol


def external_api_call(email, message):
    # let's pretend this function calls 3rd party api
    print("External API called!")
    return


class NotificationService(Protocol):
    def send_email(self, email, message):
        raise NotImplementedError


class _NotificationServiceImpl(NotificationService):
    def send_email(self, email, message):
        return external_api_call(email, message)


def create_notification_service() -> NotificationService:
    return _NotificationServiceImpl()
